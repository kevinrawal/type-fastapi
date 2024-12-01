import typer
from type_fastapi.commands.standard import standard

app = typer.Typer()

app.command(name="standard")(standard)

# Current version
__version__ = "0.1.7"


def version_callback(value: bool):
    """
    Stop the application and print the version number if `value` is True.
    """

    if value:
        print(f"type-fastapi: {__version__}")
        raise typer.Exit()


@app.callback()
def common(
    ctx: typer.Context,
    version: bool = typer.Option(None, "--version", "-v", callback=version_callback),
):
    """
    Handle the CLI application's global options.

    Args:
        ctx: The Typer context object.
        version: Whether to print the version number and exit. The default is False.
    """


if __name__ == "__main__":
    app()
