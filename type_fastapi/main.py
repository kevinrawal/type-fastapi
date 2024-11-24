import typer


app = typer.Typer()


@app.callback()
def callback():
    """
    Create a FastAPI app
    """


@app.command()
def create_simple():
    """
    Create a simple FastAPI app
    """
    print("Create a simple FastAPI app")
    pass
