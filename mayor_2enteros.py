# programa para verificar cual de dos numeros enteros  es el mayor
print("--------------------------")
print("-----MAYOR 2 ENTEROS------")
print("--------------------------")


# input
x= int(input("dijite el valor de x: "))
y= int(input("dijite el valor de y: "))
#processing

if x == y:
    #output
    print("los numeros son iguales...")
else:
    if x > y:
        mayor=x
    else:
        mayor =y



# output
print("el mayor entre" + str(x) + " y " + str(y)) + " es " + str(mayor)