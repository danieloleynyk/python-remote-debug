"""Console module."""
import click


@click.group()
def main() -> None:
    """The main function."""
    click.echo("main")


@click.command()
def start() -> None:
    """The start command."""
    click.echo("start command")


@click.command()
def stop() -> None:
    """The stop command."""
    click.echo("stop command")


main.add_command(start)
main.add_command(stop)
