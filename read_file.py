import sys
from pathlib import Path


def read_file(path: str) -> str:
    return Path(path).expanduser().read_text()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python read_file.py <path>", file=sys.stderr)
        sys.exit(1)
    print(read_file(sys.argv[1]))
