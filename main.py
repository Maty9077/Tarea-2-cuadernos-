print("Matias Osorio 4°B")
iva=0
subtotal=0
print("vendemos cuadernos ")

print("tienen un valor de 500$ cada uno sin IVA")

numero=int(input("Cuantos desea comprar:"))
while numero < 0:  
 print ( "¡Ha escrito un número negativo! Inténtelo de nuevo")
 numero = int ( input ( "Escriba un número positivo: "))
 print ( "Gracias por su colaboración")
print("--------------------------")
print("cuadernos:",numero )

subtotal=500*numero
print( "precio sin IVA:", subtotal, "$")

iva= subtotal*0.19
print("IVA:",iva,"$")

total= subtotal+iva

print("Total de su compra:",total,"$")
print("gracias por su compra")
print("--------------------------")