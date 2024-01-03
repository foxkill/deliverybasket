#
# dlv:cli
#
from typing import Annotated, Optional
import typer
from dlv import __app_name__, __version__, Basket

def version(value: bool) -> None:
    if value:
        typer.echo(__app_name__ + ' v' + __version__)
        raise typer.Exit()

app = typer.Typer(help=__app_name__)

@app.command()
def dlv(
    fromFile: Annotated[str, typer.Option(help='The file to read the cusip''s of the treasuries from')] = '',
):
    basket = Basket().from_file(fromFile)
    print(basket)

@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show application version and exit",
        callback=version,
        is_eager=True
    )
) -> None:
    return None