import hashlib

from app.db.models.tag_model import Tag
from app.db.models.skill_tag_model import SkillTag
from app.ingestion.folder_scanner import FolderScanner
from app.ingestion.file_reader import FileReader
from app.ingestion.markdown_parser import MarkdownParser
from app.llm.metadata_extractor import MetadataExtractor

from app.db.session import SessionLocal
from app.db.repositories.skill_repository import SkillRepository


class IngestionPipeline:
    def __init__(self):
        self.reader = FileReader()
        self.parser = MarkdownParser()
        self.extractor = MetadataExtractor()

    def run(self, folder_path: str):
        print(f"\n[PIPELINE] Scanning folder: {folder_path}")

        files = FolderScanner(folder_path).scan()

        print(f"[PIPELINE] Files found: {files}")

        session = SessionLocal().get_session()
        repo = SkillRepository(session)

        processed = 0

        for file_path in files:
            print(f"\n[PIPELINE] Processing file: {file_path}")

            raw = self.reader.read(file_path)
            parsed = self.parser.parse(raw)
            meta = self.extractor.extract(parsed)

            content_hash = self._generate_hash(raw)

            # 🔍 DEBUG OUTPUT (IMPORTANT)
            print("HASH:", content_hash)
            existing = repo.get_by_hash(content_hash)

            print("EXISTS RAW:", existing)

            # IMPORTANT FIX: check explicitly
            if existing is not None:
                print("[PIPELINE] SKIPPING duplicate skill")
                continue

            # if existing:
            #     print("[PIPELINE] SKIPPING (duplicate detected)")
            #     continue

            skill = repo.create({
                "title": meta["title"],
                "summary": meta["summary"],
                "content_hash": content_hash,
                "file_path": file_path,
                "raw_markdown": raw
            })
            # ----------------------------
            # TAG PROCESSING
            # ----------------------------
            tags = meta.get("tags", [])

            for tag_name in tags:
                tag = session.query(Tag).filter_by(name=tag_name).first()

                if not tag:
                    tag = Tag(id=tag_name, name=tag_name)
                    session.add(tag)
                    session.commit()

                session.add(SkillTag(
                    skill_id=skill.id,  # ✅ IMPORTANT FIX
                    tag_id=tag.id
                ))

            session.commit()

            print("[PIPELINE] INSERTED SUCCESSFULLY")

            processed += 1

        print(f"\n[PIPELINE] DONE. Processed = {processed}")

        return {"processed": processed}

    def _generate_hash(self, content: str) -> str:
        return hashlib.sha256(content.encode()).hexdigest()