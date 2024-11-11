import msvcrt

def menu_gastos():
    
    gastos = {
        "alojamiento": 0,
        "comida": 0,
        "transporte": 0
    }
    
    while True:
        print("\n---- CALCULADORA GASTOS VIAJE----\n")
        print("1) Ingresar gasto en alojamiento")
        print("2) Ingresar gasto en comida")
        print("3) Ingresar gasto en transporte")
        print("4) Mostrar resumen y total de gastos")
        print("5) Salir")
        
        opcion = input("Selecciona una opción: ")
        if opcion not in ["1","2","3","4","5"]:
            print("* ERROR * Ingrese una opción válida")
            continue
        
        if opcion == "1":
            gastos["alojamiento"] += obtener_gasto("alojamiento")
        elif opcion == "2":
            gastos["comida"] += obtener_gasto("comida")
        elif opcion == "3":
            gastos["transporte"] += obtener_gasto("transporte")
        elif opcion == "4":
            mostrar_resumen(gastos)
        elif opcion == "5":
            print("Usted ha salido del programa c:")
            break

def obtener_gasto(categoria):
    while True:
        gasto = input(f"Ingrese el gasto en {categoria}: ")
        if gasto.isdigit() and int(gasto) >= 0:
            return int(gasto)      
        else: 
            print("El gasto debe ser una cifra válida, intente nuevamente")
            
def mostrar_resumen(gastos):
    print("\n--- RESUMEN DE GASTOS ---")

    totalGastos = sum(gastos.values())
    for categoria, monto in gastos.items():
        print(f"{categoria}: ${monto}")
    
    print(f"* TOTAL DE GASTOS: ${totalGastos}")
    
    print("Presione cualquier tecla para continuar...")
    msvcrt.getch() 

def main_menu():
    menu_gastos()
    
main_menu()
