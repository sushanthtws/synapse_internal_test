from app.ingestion.folder_scanner import FolderScanner


def test_folder_scanner_finds_markdown_files(tmp_path):
    # Arrange: create fake folder structure
    (tmp_path / "skill1.md").write_text("# Skill 1")
    (tmp_path / "skill2.md").write_text("# Skill 2")
    (tmp_path / "ignore.txt").write_text("ignore")

    subfolder = tmp_path / "sub"
    subfolder.mkdir()
    (subfolder / "skill3.md").write_text("# Skill 3")

    scanner = FolderScanner(root_path=str(tmp_path))

    # Act
    files = scanner.scan()

    # Assert
    assert len(files) == 3
    assert any("skill1.md" in f for f in files)
    assert any("skill2.md" in f for f in files)
    assert any("skill3.md" in f for f in files)