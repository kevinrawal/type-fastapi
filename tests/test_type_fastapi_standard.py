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


def test_type_fastapi_standard_directory_exists():
    """
    Test the `standard` subcommand when the directory already exists.
    """
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        current_dir = os.getcwd()
        os.chdir(temp_dir)

        # Create the directory `tests` and an empty __init__.py file
        os.makedirs("tests", exist_ok=True)
        with open("tests/__init__.py", "w", encoding="utf-8") as f:
            f.write("")

        # create requirements.txt file
        with open("requirements.txt", "w", encoding="utf-8") as f:
            f.write("fastapi\nuvicorn\n")

        try:
            # Run the CLI command
            runner = CliRunner()
            result = runner.invoke(app, ["standard"])

            print("current_dir == ", current_dir)
            # Check CLI exit code
            assert result.exit_code == 0

            # Check if the warning message appears in the output
            assert (
                f"Warning: Directory already exists: {os.path.join(temp_dir, 'tests')}"
                in result.stdout
            ), f"Expected warning message not found in output: {result.stdout}"

            # Check if the warning message appears in the output for already existing file  # noqa: E501
            assert (
                f"Warning: File already exists: {os.path.join(temp_dir, 'requirements.txt')}"  # noqa: E501
                in result.stdout
            ), f"Expected warning message not found in output: {result.stdout}"

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
