from typing import List


def asciiDecode(data: List[int]) -> str:
    message = ""
    for d in data:
        message += chr(d)

    return message


def hexDecode(data: str) -> str:
    return bytes.fromhex(data).decode()


def b64Decode(data: str) -> str:
    from base64 import b64decode
    return b64decode(data)
