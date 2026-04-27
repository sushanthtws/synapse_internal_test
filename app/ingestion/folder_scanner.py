import os


class FolderScanner:
    def __init__(self, root_path: str):
        self.root_path = root_path

    def scan(self):
        md_files = []

        for root, _, files in os.walk(self.root_path):
            for file in files:
                if file.endswith(".md"):
                    full_path = os.path.join(root, file)
                    md_files.append(full_path)

        return md_files