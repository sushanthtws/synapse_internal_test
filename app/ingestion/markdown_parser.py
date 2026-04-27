import re
from typing import Dict, Any


class MarkdownParser:
    def parse(self, content: str) -> Dict[str, Any]:
        lines = content.split("\n")

        title = ""
        structure = {
            "h1": "",
            "h2": [],
            "content_map": {}
        }

        current_heading = None
        buffer = []

        for line in lines:
            line = line.strip()

            if not line:
                continue

            # H1
            if line.startswith("# "):
                if buffer and current_heading:
                    structure["content_map"][current_heading] = "\n".join(buffer).strip()
                    buffer = []

                title = line[2:].strip()
                structure["h1"] = title
                current_heading = title

            # H2
            elif line.startswith("## "):
                if buffer and current_heading:
                    structure["content_map"][current_heading] = "\n".join(buffer).strip()
                    buffer = []

                current_heading = line[3:].strip()
                structure["h2"].append(current_heading)

            # content
            else:
                buffer.append(line)

        # flush last buffer
        if current_heading and buffer:
            structure["content_map"][current_heading] = "\n".join(buffer).strip()

        return {
            "title": title,
            "structure": structure
        }