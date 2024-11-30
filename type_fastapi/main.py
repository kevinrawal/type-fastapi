import typer
from type_fastapi.commands.standard import standard

app = typer.Typer()

app.command(name="standard")(standard)


@app.callback()
def callback():
    """
    Create a FastAPI app
    """


if __name__ == "__main__":
    app()
