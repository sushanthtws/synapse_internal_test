from app.llm.metadata_extractor import MetadataExtractor


def test_metadata_extractor_generates_structure():
    input_data = {
        "title": "PDF Processing Skill",
        "structure": {
            "h1": "PDF Processing Skill",
            "h2": ["Introduction", "Setup"],
            "content_map": {
                "Introduction": "This skill helps process PDFs using Python.",
                "Setup": "Install dependencies and run pipeline."
            }
        }
    }

    extractor = MetadataExtractor()

    result = extractor.extract(input_data)

    assert "title" in result
    assert "summary" in result
    assert isinstance(result["tags"], list)
    assert isinstance(result["tech"], list)
    assert isinstance(result["domain"], list)