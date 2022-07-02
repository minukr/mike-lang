from interpreter import MikeInterpreter
import sys

with open(sys.argv[1], encoding="utf-8") as file:
    try:
        code = file.read()
    except:
        pass

mike = MikeInterpreter()
mike.interpret(code)
