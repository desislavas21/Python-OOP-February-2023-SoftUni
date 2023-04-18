# Fix the code, so it returns the expected output. Submit the fixed code in the judge syste
# Example
# Current Output Expected Output
# global
# outer: local
# inner: nonlocal
# outer: local
# global
# Expected Output
# global
# outer: local
# inner: nonlocal
# outer: nonlocal
# global: changed!

x = "global"


def outer():
    x = "local"

    def inner():
        x = "nonlocal"
        print("inner:", x)
        return x

    def change_global():
        x = "global: changed!"
        print(x)
        return x

    print("outer:", x)
    x = inner()
    print("outer:", x)
    x = change_global()

print(x)
outer()
