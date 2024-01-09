#
# dlv:cli
#
import asyncio
import typer
from typing import Annotated, Optional
from dlv import __app_name__, __version__, Basket, Future
from dlv.future import NOTIONAL_COUPON

def version(value: bool) -> None:
    if value:
        typer.echo(__app_name__ + ' v' + __version__)
        raise typer.Exit(0)

app = typer.Typer(help=__app_name__)

@app.command()
def read_cusips():
    pass

@app.command()
def dlv(
    fromFile: Annotated[
        str, 
        typer.Option(
            '--from-file',
            '-f',
            help='The file to read the cusip''s of the treasuries from')
        ],
    future: Annotated[
        str, 
        typer.Option(
            '--future',
            '-t',
            help='Name of the future the basket is deliverable to. Examples are: TUU2, FVH4 etc.')
        ],
    printdlv: Annotated[Optional[bool], typer.Option(
        '--print',
        '-p',
        help='Print the basket like bloombergs dlv function', 
    )] = False,
    toFile: Annotated[Optional[str], typer.Option(
        '--serialize',
        '-s',
        help='Write gathered informations about treasuries to basket file')
    ] = None, 
    coupon: Annotated[Optional[float], typer.Option(help='The notianal coupon of the future')] = NOTIONAL_COUPON,
    first: Annotated[Optional[str], typer.Option(help='The notianal coupon of the future')] = '',
    last: Annotated[Optional[str], typer.Option(help='The notianal coupon of the future')] = '',
):
    # print(fromFile, toFile, future, coupon, first, last)
    # basket = asyncio.run(Basket.from_file(fromFile))
    basket = Basket.from_file(fromFile)

    if basket is None:
        typer.echo('Could not create basket.')
        typer.Exit(1)

    if toFile and basket:
        basket.future = future
        basket_str = basket.serialize()

    if printdlv and basket:
        basket.future = future
        basket.print()

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