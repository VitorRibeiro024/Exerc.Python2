a=int(input("Lado A: "))
b=int(input("Lado B: "))
c=int(input("Lado C: "))
if a>b+c or b>a+c or c>a+b:
    print("O triangulo não existe!")
else:
    if a==b==c:
        print("O triangulo é equilátero")
    if a!=b==c:
        print("O triangulo é isósceles")
    if a!=b!=c:
        print("O triangulo é escaleno")
