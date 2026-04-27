from app.ingestion.file_reader import FileReader


def test_file_reader_reads_markdown(tmp_path):
    file_path = tmp_path / "skill.md"
    file_path.write_text("# Title\nSome content here")

    reader = FileReader()

    content = reader.read(str(file_path))

    assert "# Title" in content
    assert "Some content" in content