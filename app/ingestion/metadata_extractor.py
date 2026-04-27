import re


class MetadataExtractor:
    """
    Extracts structured metadata from markdown skill files.
    Works with or without YAML frontmatter.
    """

    def extract(self, content: str) -> dict:
        return {
            "title": self._extract_title(content),
            "summary": self._extract_summary(content),
            "tags": self._extract_tags(content)
        }

    # -------------------------
    # TITLE EXTRACTION
    # -------------------------
    def _extract_title(self, content: str) -> str:
        # Try YAML frontmatter first
        match = re.search(r"title:\s*(.*)", content)
        if match:
            return match.group(1).strip()

        # fallback: first heading
        match = re.search(r"#\s+(.*)", content)
        if match:
            return match.group(1).strip()

        return "Untitled Skill"

    # -------------------------
    # SUMMARY EXTRACTION
    # -------------------------
    def _extract_summary(self, content: str) -> str:
        match = re.search(r"summary:\s*(.*)", content)
        if match:
            return match.group(1).strip()

        # fallback: first paragraph
        paragraphs = content.split("\n\n")
        for p in paragraphs:
            if len(p.strip()) > 20:
                return p.strip()

        return "No summary available"

    # -------------------------
    # TAG EXTRACTION
    # -------------------------
    def _extract_tags(self, content: str) -> list:
        match = re.search(r"tags:\s*(.*)", content)
        if match:
            tags = match.group(1)
            return [t.strip() for t in tags.split(",")]

        return []