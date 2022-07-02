class MikeInterpreter:
    def __init__(self):
        self.pointer = 0
        self.mem = [0] * 2048

    def interpret(self, code):
        cursor = 0
        
        while cursor < len(code):
            cur = code[cursor]
            if cur == "쿼":
                if self.pointer+1 < len(self.mem):
                    self.pointer += 1
            elif cur == "쿠":
                self.pointer -= 1
            elif cur == "자":
                self.mem[self.pointer] += 1
            elif cur == "조":
                self.mem[self.pointer] -= 1
            elif cur == "스":
                print(chr(self.mem[self.pointer]), end="")
            elif cur == "수":
                self.mem[self.pointer] = ord(input())
            elif cur == "마":
                if self.mem[self.pointer] == 0:
                    while code[cursor] != "잌":
                        cursor += 1
            elif cur == "잌":
                if self.mem[self.pointer] != 0:
                    while code[cursor] != "마":
                        cursor -= 1
                        
            cursor += 1