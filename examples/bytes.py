#!/usr/bin/env python


import filetype


def main():
    buf = bytearray([0xFF, 0xD8, 0xFF, 0x00, 0x08])
    kind = filetype.guess(buf)

    if kind is None:
        print("Cannot guess file type!")
        return

    print(f"File extension: {kind.extension}")
    print(f"File MIME type: {kind.mime}")


if __name__ == "__main__":
    main()
