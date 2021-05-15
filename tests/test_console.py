import click
import pytest
from click.testing import CliRunner

from src import console


@pytest.fixture
def runner():
    return CliRunner()


@pytest.mark.parametrize("function", [console.start, console.stop])
def test_basic_commands_success(runner: CliRunner, function: click.BaseCommand):
    result = runner.invoke(function)
    assert result.exit_code == 0
