
print("\nBienvenidos a la aplicacion de gestion de sueldos:")
print("1. Registrar trabajador")
print("2. Lista todos los trabajadores")
print("3. Imprimir planilla de sueldos")
print("4. Salir del programa")
opcion = input("Seleccione una opcion:")

match opcion:
    case 1:
      with open("homero.txt","r") as ArchivoEmpresas:
         nombre = input("Ingrese nombre y apellido del trabajador: ")
         cargo = input("Ingrese el cargo del trabajador: ")
         sueldo_bruto = float(input("Ingrese el sueldo bruto del trabajador: "))
         desc_salud = sueldo_bruto * 0.07
         desc_afp = sueldo_bruto * 0.12
         liquido_pagar = sueldo_bruto - desc_salud - desc_afp

         print("Trabajador registrado:")
         print("Nombre y apellido:", nombre)
         print("Cargo:", cargo)
         print("Sueldo bruto:", sueldo_bruto)
         print("Descuento salud:", desc_salud)
         print("Descuento AFP:", desc_afp)
         print("Liquido a pagar:", liquido_pagar)
        

            
    case 2:
        def ArchivoEmpresas(nombre):
            print("Lista de trabajadores:")
            for trabajador in nombre:
                print(trabajador)
    case 3:
        def imprimir_planilla(trabajadores, cargo=None):
            if cargo:
                filename = f"planilla_{cargo}.txt"
                with open(filename, "w") as file:
                    for trabajador in trabajadores:
                        if trabajador[1] == cargo:
                            file.write("Nombre y apellido: {}\n" .format(trabajador[0]))
                            file.write("Cargo: {}\n" .format(trabajador[1]))
                            file.write("Sueldo bruto: {}\n" .format(trabajador[2]))
                            file.write("Descuento salud: {}\n" .format(trabajador[3]))
                            file.write("Descuento AFP: {}\n" .format(trabajador[4]))

            else:
                filename = "Planilla_todos.txt"
                with open(filename, "w") as file:
                    for trabajador in trabajadores:
                        file.write("Nombre y apellido: {}\n".format(trabajador[0]))
                        file.write("Cargo: {}\n".format(trabajador[1]))
                        file.write("Sueldo bruto: {}\n".format(trabajador[2]))
                        file.write("Descuento salud: {}\n".format(trabajador[3]))
                        file.write("Descuento AFP: {}\n".format(trabajador[4]))
                        file.write("Liquido a pagar:{}\n\n".format(trabajador[5]))



        def main():
            trabajadores = []
            while True:
                if opcion == "1":
                    trabajadores == ArchivoEmpresas.txt(ArchivoEmpresas)
                    trabajadores.append(trabajadores)
                elif opcion == "2":
                    ArchivoEmpresas(trabajadores)
                elif opcion == "3":
                    cargo = input("Ingrese el cargo para imprimir la planilla (O dejar en blanco para todos): ")
                    print("Planilla de sueldos generada.")
                elif opcion == "4":
                    print("Saliendo del programa...")
                    break
                else:
                    print("Opcion invalida. Por favor, seleccione una opcion valida.")