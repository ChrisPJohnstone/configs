from re import fullmatch


def is_valid_hex(string: str) -> bool:
    if fullmatch(r"#([0-9a-fA-F]{2}){3}", string):
        return True
    return False
