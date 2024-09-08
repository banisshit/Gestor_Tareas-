from datetime import date
from typing import List, Dict, Tuple, Set

#Estructuras de Datos
tareas: List[Dict] = []
categorias: Dict[str, List[Dict]] = {}
etiquetas: Set[str] = set()

#Funciones

def agregar_tarea():
    nombre = input("Ingrese el nombre de la tarea: ")
    categoria = input("Ingrese la categoría de la tarea: ")
    fecha_vencimiento = tuple(map(int, input("Ingrese la fecha de vencimiento (AAAA MM DD): ").split()))
    etiquetas_tarea = set(input("Ingrese las etiquetas (separadas por comas): ").split(","))

    tarea = {
        'nombre': nombre,
        'categoria': categoria,
        'fecha_vencimiento': date(*fecha_vencimiento),
        'etiquetas': etiquetas_tarea
    }
    tareas.append(tarea)
    if categoria not in categorias:
        categorias[categoria] = []
    categorias[categoria].append(tarea)
    etiquetas.update(etiquetas_tarea)

def eliminar_tarea():
    if not hay_tareas():
        print("Debe agregar una tarea primero")
        return
    nombre = input("Ingrese el nombre de la tarea a eliminar: ")
    if not tarea_existe(nombre):
        print("No existen tareas con ese nombre")
        return
    global tareas
    tareas = [tarea for tarea in tareas if tarea['nombre'] != nombre]
    for categoria in categorias.values():
        categoria[:] = [tarea for tarea in categoria if tarea['nombre'] != nombre]

def modificar_tarea():
    if not hay_tareas():
        print("Debe agregar una tarea primero")
        return
    nombre = input("Ingrese el nombre de la tarea a modificar: ")
    if not tarea_existe(nombre):
        print("No existen tareas con ese nombre")
        return
    nuevo_nombre = input("Ingrese el nuevo nombre de la tarea (deje en blanco para mantener actual): ")
    nueva_categoria = input("Ingrese la nueva categoría de la tarea (deje en blanco para mantener actual): ")
    nueva_fecha_vencimiento = input("Ingrese la nueva fecha de vencimiento (AAAA MM DD, deje en blanco para mantener actual): ")
    nuevas_etiquetas = input("Ingrese las nuevas etiquetas (separadas por comas, deje en blanco para mantener actual): ")
    for tarea in tareas:
        if tarea['nombre'] == nombre:
            if nuevo_nombre:
                tarea['nombre'] = nuevo_nombre
            if nueva_categoria:
                categoria_antigua = tarea['categoria']
                tarea['categoria'] = nueva_categoria
                categorias[categoria_antigua].remove(tarea)
                if nueva_categoria not in categorias:
                    categorias[nueva_categoria] = []
                categorias[nueva_categoria].append(tarea)
            if nueva_fecha_vencimiento:
                tarea['fecha_vencimiento'] = date(map(int, nueva_fecha_vencimiento.split()))
            if nuevas_etiquetas:
                tarea['etiquetas'] = set(nuevas_etiquetas.split(","))
                etiquetas.update(tarea['etiquetas'])

def mostrar_tareas():
    if not hay_tareas():
        print("Debe agregar una tarea primero")
        return
    for tarea in tareas:
        print(f"Nombre: {tarea['nombre']}, Categoría: {tarea['categoria']}, Fecha de Vencimiento: {tarea['fecha_vencimiento']}, Etiquetas: {tarea['etiquetas']}")

def tarea_existe(nombre: str) -> bool:
    return any(tarea['nombre'] == nombre for tarea in tareas)

def hay_tareas() -> bool:
    return len(tareas) > 0

#Clases
class Tarea:
    def init(self, nombre: str, categoria: str, fecha_vencimiento: Tuple[int, int, int], etiquetas_tarea: Set[str]):
        self.nombre = nombre
        self.categoria = categoria
        self.fecha_vencimiento = date(fecha_vencimiento)
        self.etiquetas = etiquetas_tarea

    def str(self):
        return f"Nombre: {self.nombre}, Categoría: {self.categoria}, Fecha de Vencimiento: {self.fecha_vencimiento}, Etiquetas: {self.etiquetas}"

class TareaConFechaLimite(Tarea):
    def init(self, nombre: str, categoria: str, fecha_vencimiento: Tuple[int, int, int], etiquetas_tarea: Set[str], fecha_limite: Tuple[int, int, int]):
        super().init(nombre, categoria, fecha_vencimiento, etiquetas_tarea)
        self.fecha_limite = date(*fecha_limite)

    def str(self):
        return super().str() + f", Fecha Límite: {self.fecha_limite}"