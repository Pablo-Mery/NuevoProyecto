from os import system
system ("cls")
total=0
des=0
cantT=0
Pi=0
Ot=0
Pv=0
Ae=0
Pf=0
salir=True
otro=True
cod=True
def seguir(sal):
    if sal ==1:
        salir=True
    elif sal ==2:
        salir=False
print("Hola Muy buenas Que sushis va a pedir\n")
while otro==True:
    while salir==True:
        elec=int(input("Los Rolls disponibles son: 1.Pikachu Roll $4500\n 2.Otaku Roll $5000\n 3.Pulpo Venenoso Roll $5200\n 4.Anguila Eléctrica Roll $4800\n 5.Pollo Frito $5000\nCual desea elegir ingrese la opcion: "))
        print()

        if elec == 1:

            num=int(input("Cuantos rolls de tipo Pikachu lleva: "))
            print()
            cant = num*4500
            total = total+cant
            cantT= cantT+num
            Pi=Pi+num
            sal=int(input(f"Usted Lleva {num} de Rolls de Pikachu\nDesea algo más\n 1.Si\n 2.No\nIngrese Opcion: "))

        elif elec ==2:

            num=int(input("Cuantos rolls de tipo Otaku lleva: "))
            print()
            cant = num*5000
            total = total+cant
            cantT= cantT+num
            Ot=Ot+num
            sal=int(input(f"Usted Lleva {num} de Rolls de Otaku\nDesea algo más\n 1.Si\n 2.No\nIngrese Opcion: "))
            if sal ==1:
                salir=True
            elif sal ==2:
                salir=False
        elif elec ==3:

            num=int(input("Cuantos rolls de tipo Pulpo Venenoso lleva: "))
            print()
            cant = num*5200
            total = total+cant
            cantT= cantT+num
            Pv=Pv+num
            sal=int(input(f"Usted Lleva {num} de Rolls de Pulpo Venenoso\nDesea algo más\n 1.Si\n 2.No\nIngrese Opcion: "))
            if sal ==1:
                salir=True
            elif sal ==2:
                salir=False        
        elif elec ==4:

            num=int(input("Cuantos rolls de tipo Anguila Eléctrica lleva: "))
            print()
            cant = num*4800
            total = total+cant
            cantT= cantT+num
            Ae=Ae+num
            sal=int(input(f"Usted Lleva {num} de Rolls de Anguila Eléctrica\nDesea algo más\n 1.Si\n 2.No\nIngrese Opcion: "))
            if sal ==1:
                salir=True
            elif sal ==2:
                salir=False
        elif elec ==5:
            num=int(input("Cuantos Pollos Fritos lleva: "))
            print()
            cant=num*5000
            total =total+cant
            cantT=cantT+num
            Pf=Pf+num
            sal =int(input(f"Ustes Lleva {num} de Pollo Frito\nDeea algo mas\n 1.si\n 2.No\nIngrese Opcion: "))
            if sal ==1:
                salir=True
            elif sal ==2:
                salir=False
    system ("cls")
    while cod==True:
        Descu=str(input("Si usted Tiene Un codigo Ingreselo:\n"))
        if Descu =="soyotaku":
            print("Por este Codigo se le ara un descuento de 10%")
            des=round(total*0.1)
            cod=False
        else:
            print("No es un codigo valido")
            pru=str(input("Si desea volver a ingresar ponga X\n"))
            if pru=="X":
                cod=True
                
            else:
                cod=False
                print("Continue")
    system ("cls")        
    print()    
    print("*************************************************")
    print(f"Total de productos: {cantT} ")
    print("*************************************************")
    print(f"Pikachu Rolls:{Pi}")
    print(f"Otaku Roll:{Ot} ")
    print(f"Pulpo Venenoso:{Pv}")
    print(f"Anguila ELectrica: {Ae}")
    print("*************************************************")

    print(f"Subtotal a pagar: ${total}")
    print (f"Descuento por Codigo: ${des}")
    print(f"Total: ${total-des}")
    input()
    rep=int(input("Quieres hacer otro pedido\n 1.S1\n 2.No\nIngrese Opcion: "))
    if rep ==1:
        total=0
        des=0
        cantT=0
        Pi=0
        Ot=0
        Pv=0
        Ae=0
        Pf=0
        salir=True
        otro=True
        cod=True
    elif rep ==2:
        otro=False