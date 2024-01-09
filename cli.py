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
    print(fromFile, toFile, future, coupon, first, last)
    # basket = asyncio.run(Basket.from_file(fromFile))
    basket = Basket.from_file(fromFile)

    if basket is None:
        typer.echo('Could not create basket.')
        typer.Exit(1)

    if toFile and basket:
        basket_str = basket.serialize()

    if printdlv and basket:
        basket.future = future

    # if basket.serialze('tests/ulh4.basket.yaml') == True:
        # print('Basket successfully serialized')

    # print(basket.get('912828XW5'))

    # usbf = BondFuture(
    #     coupon=6.0,
    #     delivery=(dt(2020,9,1), dt(2020,10,5)),
    #     basket=[t[0] for t in basket.values()], # type: ignore
    #     calc_mode='ust_short',
    # )
    
    # df = usbf.dlv(
    #     future_price=110 + ((11+3/8)/32),
    #     prices=[t[1] for t in basket.values()],
    #     repo_rate=0.172,
    #     settlement=dt(2020,6,23),
    #     delivery=dt(2020,10,5),
    #     convention='Act360',
    # )

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