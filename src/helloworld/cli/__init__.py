import click
from helloworld.cli.say import say_command

# minor fix
@click.group(
    help="HelloWorld",
    context_settings={"help_option_names": ["-h", "--help"]},
)
@click.version_option(package_name="helloworld")
def helloworld() -> None:
    pass


helloworld.add_command(say_command)
