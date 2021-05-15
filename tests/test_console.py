import click
from click.testing import CliRunner
import pytest

from src import console


@pytest.fixture
def runner() -> CliRunner:
    return CliRunner()


@pytest.mark.parametrize("function", [console.start, console.stop])
def test_basic_commands_success(runner: CliRunner, function: click.BaseCommand) -> None:
    result = runner.invoke(function)
    assert result.exit_code == 0
