import click


@click.group()
def main():
    click.echo("main")


@click.command()
def start():
    click.echo("start command")


@click.command()
def stop():
    click.echo("stop command")


main.add_command(start)
main.add_command(stop)
