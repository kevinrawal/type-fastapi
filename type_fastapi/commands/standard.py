import typer
import os

from type_fastapi.utils import create_structure


def standard():
    """
    Create a standard FastAPI setup
    """
    base_dir = os.getcwd()  # Current working directory
    structure = [
        {
            "app": [
                "__init__.py",
                "main.py",
                {"routers": ["__init__.py"]},
                {"services": ["__init__.py"]},
                {"schemas": ["__init__.py"]},
                {"models": ["__init__.py"]},
                {"external_services": ["__init__.py"]},
                {"config": ["__init__.py", "database.py"]},
                {"utils": ["__init__.py"]},
            ]
        },
        {"tests": ["__init__.py"]},
        ".gitignore",
        "requirements.txt",
        "README.md",
    ]

    create_structure(base_dir, structure)
    typer.echo("FastAPI project structure has been created successfully.")
