

import ctypes
from pathlib import Path



BASE_DIR = Path(__file__).parent


LIBRARY_PATH = BASE_DIR / "Native" / "f1.so"


native = ctypes.CDLL(str(LIBRARY_PATH))



native.String_Check.argtypes = [
    ctypes.c_char_p,
    ctypes.c_char_p,
    ctypes.c_char_p
]


native.String_Check.restype = ctypes.c_char_p

def String_Check(username, password, email):

    result = native.String_Check(
        username.encode("utf-8"),
        password.encode("utf-8"),
        email.encode("utf-8")
    )

    return result.decode("utf-8")

