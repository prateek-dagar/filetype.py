from .base import Type


class Wasm(Type):
    """Implements the Wasm image type matcher."""

    MIME = "application/wasm"
    EXTENSION = "wasm"

    def __init__(self):
        super().__init__(mime=Wasm.MIME, extension=Wasm.EXTENSION)

    def match(self, buf):
        return buf[:8] == bytearray([0x00, 0x61, 0x73, 0x6D, 0x01, 0x00, 0x00, 0x00])
class Class(Type):
    """
    Implements the Java Class file type matcher.
    """

    MIME = "application/java-byte-code"
    EXTENSION = "class"

    def __init__(self):
        super().__init__(mime=Class.MIME, extension=Class.EXTENSION)

    def match(self, buf):
        return len(buf) > 3 and buf[0:4] == b"\xca\xfe\xba\xbe"


class Dex(Type):
    """
    Implements the Dalvik Executable file type matcher.
    """

    MIME = "application/vnd.android.dex"
    EXTENSION = "dex"

    def __init__(self):
        super().__init__(mime=Dex.MIME, extension=Dex.EXTENSION)

    def match(self, buf):
        return len(buf) > 3 and buf[0:4] == b"dex\n"

