def main() -> None:
    b: list[str] = a
    f(a)
    g()
    print(a)
    print(b[0])

def f(a: list[str]) -> None:
    a[0] = "w"
    a = ["k", "j"]

def g() -> None:
    global a
    a[1] = "m"
    a = ["y", "p"]

a: list[str] = ["u", "g"]

if __name__ == "__main__":
    main()