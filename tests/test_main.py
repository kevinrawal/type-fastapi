from typer.testing import CliRunner
from type_fastapi.main import app  # Replace 'your_script_name' with the actual name of your Python file.

runner = CliRunner()

def test_create_simple():
    # Run the `create-simple` command
    result = runner.invoke(app, ["create-simple"])
    
    # Assert the command exits successfully
    assert result.exit_code == 0
    
    # Assert the expected output
    assert "Create a simple FastAPI app\n" == result.output
