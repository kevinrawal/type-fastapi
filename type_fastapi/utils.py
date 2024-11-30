import os
import typer


def create_structure(base, items):
    """
    Recursively create files and directories based on the given items.

    Args:
        base (str): The base directory to create the files and directories in.
        items (list[Union[str, dict]]): The list of items to create. If an item is a
            string, it is created as a file with the name being the value of the
            string. If an item is a dictionary, it is created as a directory with
            the key being the name of the directory and the value being the list of
            subitems to create inside the directory.

    Returns:
        None
    """
    for item in items:
        if isinstance(item, str):
            # Create files
            file_path = os.path.join(base, item)
            if os.path.exists(file_path):
                typer.secho(
                    f"Warning: File already exists: {file_path}", fg=typer.colors.YELLOW
                )
            else:
                with open(file_path, "w", encoding="utf-8") as f:
                    if item == "README.md":
                        f.write("# FastAPI Project\n\nThis is a FastAPI project.")
                    elif item == "requirements.txt":
                        f.write("fastapi\nuvicorn\n")  # Example dependencies
                    elif item == ".gitignore":
                        f.write("*.pyc\n__pycache__/\n.env\n")

        elif isinstance(item, dict):
            # Create directories recursively
            for folder, subitems in item.items():
                folder_path = os.path.join(base, folder)
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path, exist_ok=True)
                    create_structure(folder_path, subitems)
                else:
                    typer.secho(
                        f"Warning: Directory already exists: {folder_path}",
                        fg=typer.colors.YELLOW,
                    )
