import os
import tempfile
from typer.testing import CliRunner
from type_fastapi.main import app

def test_type_fastapi_standard():
    """
    Test the `standard` subcommand creates the expected files and directories.
    """
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Change the current working directory to the temporary directory
        current_dir = os.getcwd()
        os.chdir(temp_dir)

        try:
            # Run the CLI command
            runner = CliRunner()
            result = runner.invoke(app, ["standard"])
            assert result.exit_code == 0

            # Check if all files and directories are created
            expected_paths = [
                "app/__init__.py",
                "app/main.py",
                "app/routers/__init__.py",
                "app/services/__init__.py",
                "app/schemas/__init__.py",
                "app/models/__init__.py",
                "app/external_services/__init__.py",
                "app/config/__init__.py",
                "app/config/database.py",
                "app/utils/__init__.py",
                "tests/__init__.py",
                ".gitignore",
                "requirements.txt",
                "README.md",
            ]

            for path in expected_paths:
                assert os.path.exists(path), f"File {path} was not created."

        finally:
            # Clean up: Restore the original working directory
            os.chdir(current_dir)

if __name__ == "__main__":
    test_type_fastapi_standard()
