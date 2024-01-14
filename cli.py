#
# dlv:cli
#
import asyncio
import datetime
import typer
from typing import Annotated, Optional
from dlv import __app_name__, __version__, Basket, Future
from dlv.cache import Cache

def version(value: bool) -> None:
    if value:
        typer.echo(f'{__app_name__} v{__version__}')
        raise typer.Exit(0)

app = typer.Typer(help=__app_name__)

@app.command()
def set(
    future: Annotated[
        str, 
        typer.Option(
            '--future',
            '-t',
            help='Name of the future the basket is deliverable to. Examples are: TUU2, FVH4 etc.')
        ],
    cusip: Annotated[str, typer.Option(help='Set the price of the treasury with the given cusip number.')],
    price: Annotated[float, typer.Option(help='The price to set for the given asset.')],
):
    c = Cache()
    basket = None
    try:
        basket = c.get(future)
    except Exception as e:
        typer.echo(f'Could not read basket from ({c.get_filename(future)})')
        typer.Exit(2)

    if basket is None:
        typer.echo(f'Could not read basket file for the given future: {future}')
        typer.Exit(2)
    else:
        treasury = basket.get(cusip)
        if treasury is None:
            typer.echo(f'Treasury with the cusip of {cusip} was not found')
            typer.Exit(3)
        else:
            treasury.price = price
            c.put(basket)
            typer.echo('Price was successfully set.')

@app.command()
def init(
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
    noserialize: Annotated[Optional[bool], typer.Option(
        '--no-serialize',
        help='Do not write gathered informations about treasuries to a basket file')
    ] = False, 
):
    basket = Basket.from_file(fromFile)
    if not basket is None:
        asyncio.run(basket.build())
        if noserialize:
            typer.echo('Data was read from treasury.gov but not serialized as --no-serialize option was given.')
            typer.Exit(1)
        else:
            basket.future = future
            c = Cache()
            c.put(basket)
            typer.echo('Tresuries were successfully read. Call dlv print next to see the contents of the basket of deliverables.')
            typer.Exit(0)
        
@app.command()
def print(
    future: Annotated[
        str, 
        typer.Option(
            '--future',
            '-t',
            help='Name of the future the basket is deliverable to. Examples are: TUU2, FVH4 etc.')
        ],
    price: Annotated[str, typer.Option(help='The current price of the future')],
    repoRate: Annotated[
        float, 
        typer.Option('--repo-rate', '-r', help='The current repo rate')
    ],
    settlement: Annotated[
        str, 
        typer.Option(
            '--trade',
            '-d',
            help='The date of the trade. Like trade: --date=2022-10-1'
        )
    ] = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d'),
    ldd: Annotated[
        Optional[str],
        typer.Option(
            '--ldd',
            help='The last delivery day of the future contract'
        )
    ] = None
):
    c = Cache()
    basket = None
    f = Future.parse(future)
    invalid_message = f'Could not read basket from cache file {c.get_filename(f.long_code)}. Does it exist?'
    try:
        basket = c.get(future_name=future)
        if basket is None:
            typer.echo(invalid_message)
            typer.Exit(1)
        else:
            basket.print(price, repoRate, settlement)
    except ValueError as e:
        typer.echo(invalid_message)
        typer.Exit(1)

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