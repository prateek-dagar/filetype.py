#!/usr/bin/env python


import filetype


def main():
    f = open("tests/fixtures/sample.jpg", "rb")
    data = f.read()

    kind = filetype.guess(data)
    if kind is None:
        print("Cannot guess file type!")
        return

    print(f"File extension: {kind.extension}")
    print(f"File MIME type: {kind.mime}")


if __name__ == "__main__":
    main()
