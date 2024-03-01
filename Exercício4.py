n1=float(input("Número 1: "))
n2=float(input("Número 2: "))
n3=float(input("Número 3: "))
if n1>n2>n3 or n1>n3>n2:
    print(n1, "é maior.")
if n2>n1>n3 or n2>n3>n1:
    print(n2, "é maior.")
if n3>n1>n2 or n3>n2>n1:
    print(n3, "é maior.")
