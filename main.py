#!/usr/bin/env python3
from pixly.cli.parser import build_parser
from pixly.cli.runner import run

def main():
    parser = build_parser()
    args = parser.parse_args()
    run(args)

if __name__ == "__main__":
    main()
