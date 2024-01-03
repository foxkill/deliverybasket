#
# bond
#
from dlv import __app_name__
import cli

def main() -> None:
    cli.app(prog_name=__app_name__)

if __name__ == "__main__":
    main()