import click


@click.group()
def main() -> None:
    click.echo("main")


@click.command()
def start() -> None:
    click.echo("start command")


@click.command()
def stop() -> None:
    click.echo("stop command")


main.add_command(start)
main.add_command(stop)
