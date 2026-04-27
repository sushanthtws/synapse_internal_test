from app.ingestion.folder_scanner import FolderScanner
from app.ingestion.file_reader import FileReader
from app.ingestion.markdown_parser import MarkdownParser
from app.llm.metadata_extractor import MetadataExtractor
from app.core.logger import logger



def test_real_markdown_pipeline_smoke():
    folder = "data/skills"

    scanner = FolderScanner(folder)
    reader = FileReader()
    parser = MarkdownParser()
    extractor = MetadataExtractor()


    files = scanner.scan()
    assert len(files) > 0

    file_path = files[0]
    raw = reader.read(file_path)

    parsed = parser.parse(raw)
    assert "title" in parsed

    meta = extractor.extract(parsed)

    logger.info(f"Found files: {files}")
    logger.info(f"Reading: {file_path}")
    logger.info(f"Parsed title: {parsed['title']}")
    logger.info(f"LLM output: {meta}")

    assert meta["title"] != ""
    assert isinstance(meta["tags"], list)

