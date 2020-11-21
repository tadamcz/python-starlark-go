from pystarlark.starlark import lib, ffi
import json
from ast import literal_eval


def ExecCallEval(preamble, statement, raw=False):
    if isinstance(preamble, str):
        preamble = preamble.encode()
    if isinstance(statement, str):
        statement = statement.encode()

    response = lib.ExecCallEval(preamble, statement)
    value = json.loads(ffi.string(response))
    if raw:
        return value
    return literal_eval(value["value"])