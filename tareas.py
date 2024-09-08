from Gestor import agregar_tarea, eliminar_tarea, modificar_tarea, mostrar_tareas

def main():
    while True:
        print("\nGestor de Tareas")
        print("1. Agregar Tarea")
        print("2. Eliminar Tarea")
        print("3. Modificar Tarea")
        print("4. Mostrar Tareas")
        print("5. Salir")
        opcion = input("Ingrese su opción: ")

        if opcion == '1':
            agregar_tarea()
        elif opcion == '2':
            eliminar_tarea()
        elif opcion == '3':
            modificar_tarea()
        elif opcion == '4':
            mostrar_tareas()
        elif opcion == '5':
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()