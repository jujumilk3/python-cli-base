import sys
import click

__version__ = "0.0.1"


@click.group(invoke_without_command=True)
@click.option("-c", "--check", help="check1")
@click.option("-c2", "--check2", help="check2")
@click.option("-c3", "--check3", help="check3")
@click.version_option(version=__version__, message=f"%(prog)s %(version)s")
@click.pass_context
def cli(ctx, check, check2, check3):
    if check:
        click.echo(f"check: {check}")

    if check2:
        click.echo(f"check2: {check2}")

    if check3:
        click.echo(f"check3: {check3}")

    if check is None and check2 is None:
        click.echo("This is a CLI built with Click")
        click.echo(ctx.__dict__)
        sys.exit(0)

    click.echo(ctx.params)
    sys.exit(0)


if __name__ == "__main__":
    cli()
