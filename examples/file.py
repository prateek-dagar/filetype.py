#!/usr/bin/env python


import filetype


def main():
    kind = filetype.guess("tests/fixtures/sample.jpg")
    if kind is None:
        print("Cannot guess file type!")
        return

    print(f"File extension: {kind.extension}")
    print(f"File MIME type: {kind.mime}")


if __name__ == "__main__":
    main()
