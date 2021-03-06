"""Console script for bordertale_3d."""
import argparse
import sys

import bordertale_3d


def main():
    """Console script for bordertale_3d."""
    parser = argparse.ArgumentParser()
    parser.add_argument("_", nargs="*")
    args = parser.parse_args()

    print("Arguments: " + str(args._))
    print("Replace this message by putting your code into " "bordertale_3d.cli.main")
    bordertale_3d.main()
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
