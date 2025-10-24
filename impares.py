while True:  
    try:
        numero = int(input("Ingrese un número: "))
        
        if numero % 2 == 0:
            print(f"El número {numero} es PAR.")
        else:
            print(f"El número {numero} es IMPAR.")

    except ValueError:
        print("Por favor ingrese un número válido.")

    except KeyboardInterrupt:  
        print("\nPrograma finalizado por el usuario.")
        break
