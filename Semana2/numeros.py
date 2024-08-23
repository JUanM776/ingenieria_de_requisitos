primer_numero= float(input("digite el primer numero: "))
segundo_numero= float(input("digite el segundo numero: " ))

if primer_numero > segundo_numero:
    print("el numero mayor es:", primer_numero)
elif segundo_numero > primer_numero:
    print("el numero mayor es:", segundo_numero)
else:
    print("ambos numeros tienen el mismo valor")