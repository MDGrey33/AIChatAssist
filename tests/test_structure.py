"""Tests for project structure and file existence."""

import os
import pytest

# Define the expected structure
EXPECTED_STRUCTURE = [
    "tests/test_structure.py",
    ".pre-commit-config.yaml",
    "pyproject.toml",
    ".gitignore",
    ".env",
    "LICENSE",
    "README.md",
    "poetry.lock",
    "docker-compose.yml",
    "context_retrieval_service",
    "conversation_assistant_service",
    "shared",
    "slack_auth_service",
    "slackbot_integration",
]


@pytest.mark.parametrize("path", EXPECTED_STRUCTURE)
def test_file_structure(path):
    """Test if the expected file structure exists."""
    assert os.path.exists(path), f"Missing: {path}"
