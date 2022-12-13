import click


@click.command("say", short_help="Says Hello.")
@click.option("name", "--name", type=str, help="Name of person to greet", default="World")
def say_command(
    name: str | None,
) -> None:
    """Says hello to someone"""
    print(f"Hello {name}")
