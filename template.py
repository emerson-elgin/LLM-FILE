import os
from pathlib import Path

# Root directory structure
project_structure = {
    "project_root": {
        "backend": {
            "app": {
                "__init__.py": "# Marks the folder as a Python module",
                "main.py": "# Entry point for FastAPI application",
                "routes": {
                    "__init__.py": "",
                    "file_operations.py": "# File operation APIs (search, duplicate check)",
                    "summarization.py": "# Summarization APIs",
                },
                "models": {
                    "__init__.py": "",
                    "file_model.py": "# Models for file-related data",
                },
                "services": {
                    "__init__.py": "",
                    "semantic_search.py": "# Semantic search implementation",
                    "summarizer.py": "# Summarization logic",
                    "duplicate_checker.py": "# Duplicate detection logic",
                },
            },
            "tests": {
                "__init__.py": "",
                "test_routes.py": "# Tests for API endpoints",
                "test_services.py": "# Tests for business logic",
            },
        },
        "rust_core": {
            "src": {
                "lib.rs": "// Rust library entry point",
                "file_ops.rs": "// File operation logic (renaming, deletion, etc.)",
                "metadata.rs": "// File metadata handling",
            },
            "Cargo.toml": "# Rust project dependencies",
            "tests": {
                "file_ops_test.rs": "// Test cases for file operations",
                "metadata_test.rs": "// Test cases for metadata handling",
            },
        },
        "db": {
            "migrations": {},
            "db_schema.sql": "# Initial schema for metadata storage",
            "db_config.py": "# Python database configuration",
        },
        "frontend": {
            "react-app": {
                "src": {},
                "public": {},
            },
            "tkinter": {
                "main.py": "# Entry point for Tkinter app",
            },
        },
        "scripts": {
            "setup_env.sh": "# Script to set up environment",
            "deploy_docker.sh": "# Script to deploy using Docker",
        },
        "docs": {
            "architecture.md": "# High-level architecture design",
            "api_docs.md": "# API endpoint documentation",
        },
        "config": {
            "settings.py": "# Python configurations (e.g., API keys)",
            "rust_config.toml": "# Rust configurations",
        },
        "logs": {
            "app.log": "# Logs for Python backend",
            "rust.log": "# Logs for Rust backend",
        },
        "tests": {
            "e2e_test.py": "# End-to-end test cases",
        },
        "Dockerfile": "# Dockerfile for containerizing the app",
        "docker-compose.yml": "# Docker Compose file",
        "README.md": "# Project overview and setup instructions",
        "requirements.txt": "# Python dependencies",
        ".gitignore": "# Git ignore rules",
        "LICENSE": "# Project license",
    }
}

def create_structure(base_path, structure):
    for name, content in structure.items():
        path = base_path / name
        if isinstance(content, dict):
            # Create directories
            path.mkdir(parents=True, exist_ok=True)
            create_structure(path, content)
        else:
            # Create files
            with path.open("w") as f:
                f.write(content)

if __name__ == "__main__":
    base_directory = Path("project_root")
    create_structure(base_directory, project_structure)
    print(f"Project template created successfully at {base_directory.resolve()}")
