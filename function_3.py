def fact(h):
    if h == 1:
        return 1
    else:
        return h * fact(h-1)

m = int(input("What number?"))

if m < 0:
    print("Choose a different number.")
elif m == 0:
    print("1")
else:
    print(fact(m))
