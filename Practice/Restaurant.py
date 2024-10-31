total_Order = {}
execute = 0
attempts = 3
userMenu = True
total_debt = 0

while execute < attempts:

    # Main Menu
    print("----Bienvenido a nuestro restaurante----")
    print("---------Program created by Ed----------")
    nameUser = input("Ingrese su nombre:  ")
        
    # Validate input
    if nameUser.isalpha():
        execute = 0
    else:
        print("Ingrese su nombre de nuevo")
        execute += 1
        continue 

    while userMenu:
            
        # Initial menu
        print(f"Hola {nameUser}")
        print("¿Que deseas hacer?")
        print("1. Ver menú")
        print("2. Ver factura")
        print("3. Pagar")
        print("4. Salir")

        option = input()

        # Option verifity
        if not option.isdigit() or not (1 <= int(option) <= 4):
            print("Ingrese un valor válido entre 1 y 4")
            continue

        option = int(option)

        # Option 1
        if option == 1:
            print("--------------Menu---------------")
            #Menu
            print("Los platos disponibles son:")
            print("1. Arroz de coco y pescado $8000")
            print("2. Arroz de pollo $7000")
            print("3. Sopa de mondongo $6000")
            print("4. Sopa de guandul $5000")
            print("5. Ojo de gato $4000")
            print("6. Mote de ñame $5000")
            print("7. Puré de papa $3000")
            print("---------------------------------")
            print("Las bebidas disponibles son:")
            print("1. Agua de panela $1000")
            print("2. Coca-Cola $1000")
            print("3. Limonada $1200")
            print("4. Agua $500")
            print("5. Leche $1500")
            print("6. Avena $2000")
            print("7. Jugo de naranja $1000")
            print("---------------------------------")
            print("¿Desea comprar algo?")
            purchase_option = input("Ingrese si o no:  ")

            # Option validation
            if purchase_option.isalpha() and purchase_option == "si":
                print("Ok")

                # Shipping method
                print("Elija un metodo de envío")
                print("1. Recoger en tienda")
                print("2. Domicilio gratis")
                shipMeth = input()

                if not shipMeth.isdigit() or int(shipMeth) == 1 and int(shipMeth) == 2:
                    print("Por favor, escoja una opcion correcta.")
                    continue
                
                # Method option
                if shipMeth == 1:
                    shipMeth = "Le enviaremos una notificación cuando el pedido este disponible para recoger"
                elif shipMeth == 2:
                    print("Por favor ingrese su dirección:")
                    dir = input("Introduce una dirección (ej. 123 Calle Principal): ")
                        
                    parts = dir.split()

                    if len(parts) < 2:
                        print("Dirección no válida. Asegúrate de incluir un número y un nombre de calle.")
                    else:
                        if not parts[0].isdigit():
                            print("Dirección no válida. La primera parte debe ser un número.")
                        else:
                            is_Valid = True
                            for parte in parts[1:]:
                                if not (parts.isalpha() or parts.replace("-", "").isalpha()):
                                    is_Valid = False
                                    break
                                
                            if is_Valid:
                                print("Su pedido se enviará dentro de poco.")
                            else:
                                print("Dirección no válida. Asegúrate de que el nombre de la calle contenga solo letras.")

                numPeople = input("Ingrese la cantidad de personas a pedir: ")

                if not numPeople.isdigit() or int(numPeople) <= 0:
                    print("Por favor, ingrese un número válido de personas.")
                    continue

                numPeople = int(numPeople)
                total_debt = 0  

                for i in range(1, numPeople + 1):
                    print(f"\n--- Pedido para la persona {i} ---")

                    # Dishes
                    print("Los platos disponibles son:")
                    print("1. Arroz de coco y pescado $8000")
                    print("2. Arroz de pollo $7000")
                    print("3. Sopa de mondongo $6000")
                    print("4. Sopa de guandul $5000")
                    print("5. Ojo de gato $4000")
                    print("6. Mote de ñame $5000")
                    print("7. Puré de papa $3000")
                    dish_Option = input("Escoja un plato: ")

                    # dish option
                    if dish_Option == "1":
                        dish_price = 8000
                        dish_name = "Arroz de coco y pescado"
                    elif dish_Option == "2":
                        dish_price = 7000
                        dish_name = "Arroz de pollo"
                    elif dish_Option == "3":
                        dish_price = 6000
                        dish_name = "Sopa de mondongo"
                    elif dish_Option == "4":
                        dish_price = 5000
                        dish_name = "Sopa de guandul"
                    elif dish_Option == "5":
                        dish_price = 4000
                        dish_name = "Ojo de gato"
                    elif dish_Option == "6":
                        dish_price = 5000
                        dish_name = "Mote de ñame"
                    elif dish_Option == "7":
                        dish_price = 3000
                        dish_name = "Puré de papa"
                    else:
                        print("Opción de plato inválida.")
                        continue  

                    # Drinks
                    print("Las bebidas disponibles son:")
                    print("1. Agua de panela $1000")
                    print("2. Coca-Cola $1000")
                    print("3. Limonada $1200")
                    print("4. Agua $500")
                    print("5. Leche $1500")
                    print("6. Avena $2000")
                    print("7. Jugo de naranja $1000")
                    drink_Option = input("Escoja una bebida: ")

                    # Drink option
                    if drink_Option == "1":
                        drink_price = 1000
                        drink_name = "Agua de panela"
                    elif drink_Option == "2":
                        drink_price = 1000
                        drink_name = "Coca-Cola"
                    elif drink_Option == "3":
                        drink_price = 1200
                        drink_name = "Limonada"
                    elif drink_Option == "4":
                        drink_price = 500
                        drink_name = "Agua"
                    elif drink_Option == "5":
                        drink_price = 1500
                        drink_name = "Leche"
                    elif drink_Option == "6":
                        drink_price = 2000
                        drink_name = "Avena"
                    elif drink_Option == "7":
                        drink_price = 1000
                        drink_name = "Jugo de naranja"
                    else:
                        print("Opción de bebida inválida.")
                        continue  

                    # Save
                    total_Order[i] = (dish_name, drink_name)
                    total_debt += dish_price + drink_price  

                    print("Pedido registrado para la persona", i)
                    print("Por favor revise su factura y espere mientras hacemos su pedido")
            elif purchase_option.isalpha() and purchase_option == "no":
                print("Ok")
                continue
            else:
                print("Ingrese una opcion valida.")

        # Option 2
        if option == 2:
            if not total_Order:  
                print("No hay pedidos registrados.")
            else:
                for person in total_Order:  
                    dish, drink = total_Order[person]
                    print(f"Persona {person}: Plato: {dish}, Bebida: {drink}")

                # Calcular IVA y propina
                iva = total_debt * 0.19
                propina = total_debt * 0.10
                total_final = total_debt + iva + propina
                
                print(f"El total de la cuenta es: {total_debt}")
                print(f"IVA (19%): {iva}")
                print(f"Propina (10%): {propina}")
                print(f"Total a pagar: {total_final}")

        # Option 3

        if option == 3:
            if not total_Order:  
                print("No hay pedidos para pagar.")
            else:
                iva = total_debt * 0.19
                propina = total_debt * 0.10
                total_final = total_debt + iva + propina

                print(f"El total a pagar es: {total_final}")
                print("Por favor escoja un método de pago")
                print("1. Nequi")
                print("2. Bancolombia")
                
                pay_Option = input()
                
                if pay_Option == "1" or pay_Option == "2":
                    numAccount = input("Ingrese el número de su cuenta (10 dígitos): ")

                    if numAccount.isdigit() and len(numAccount) == 10 and numAccount != "0000000000":
                        print("Número de cuenta recibido correctamente")
                        
                        cash_Pay = input("Ingrese la cantidad de dinero sin decimales: ")
                                        
                        if cash_Pay.isdigit():
                            cash_Pay = int(cash_Pay)
                            if cash_Pay < total_final:
                                print("Error: Pago insuficiente, intente nuevamente")
                            elif cash_Pay > total_final:
                                print("Error: Pago mayor al total, intente nuevamente")
                            else:
                                print("---------Pago exitoso---------")
                                if pay_Option == "1":
                                    payment_method = "Nequi"
                                elif pay_Option == "2":
                                    payment_method = "Bancolombia"
                                print(f"Método de pago: {payment_method}")
                                print(f"Valor pagado: {cash_Pay}")
                                total_Order.clear()
                                total_debt = 0  
                        else:
                            print("Ingrese un valor válido para la cantidad de dinero")
                    else:
                        print("Ingrese un valor válido para el número de cuenta")
                else:
                    print("Ingrese una opción correcta")

        # Option 4
        if option == 4:
            if total_Order and total_debt > 0:
                print("No puede salir sin pagar.")
            else:
                print("Gracias por usar nuestra app del restaurante")
                exit()

if execute == attempts:
    print("Ha exedido el número máximo de intentos. La app se cerrará")
