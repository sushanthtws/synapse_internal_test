from app.ingestion.markdown_parser import MarkdownParser


def test_markdown_parser_extracts_structure():
    md_content = """
# My Skill Title

## Introduction
This is intro content.

## Setup
This is setup content.

## Usage
How to use it.
"""

    parser = MarkdownParser()

    result = parser.parse(md_content)

    assert result["title"] == "My Skill Title"
    assert result["structure"]["h1"] == "My Skill Title"

    assert "Introduction" in result["structure"]["content_map"]
    assert "Setup" in result["structure"]["content_map"]
    assert "Usage" in result["structure"]["content_map"]

    assert "intro content" in result["structure"]["content_map"]["Introduction"]