#!/usr/bin/python3
print("".join(
    "{} = 0x{:x}\n".format(i, i) for i in range(99)
), end="")
