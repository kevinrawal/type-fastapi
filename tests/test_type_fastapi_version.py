from typer.testing import CliRunner
from type_fastapi.main import app


def test_version():
    """
    Test the --version flag prints the correct version number.
    """

    runner = CliRunner()
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert "type-fastapi: 0.1.7" in result.stdout


def test_version_with_short_flag():
    """
    Test the -v flag does not print the version number when not passed.
    """

    runner = CliRunner()
    result = runner.invoke(app, ["-v"])
    assert result.exit_code == 0
    assert "type-fastapi: 0.1.7" in result.stdout
