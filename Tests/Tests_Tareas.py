import unittest
from datetime import date
from Gestor import agregar_tarea, eliminar_tarea, modificar_tarea, mostrar_tareas, tareas, categorias, etiquetas, Tarea, TareaConFechaLimite

class TestGestorTareas(unittest.TestCase):

    def setUp(self):
        tareas.clear()
        categorias.clear()
        etiquetas.clear()

    def test_agregar_tarea(self):
        agregar_tarea()
        self.assertEqual(len(tareas), 1)
        self.assertIn('Trabajo', categorias)
        self.assertIn('urgente', etiquetas)

    def test_eliminar_tarea(self):
        agregar_tarea()
        eliminar_tarea()
        self.assertEqual(len(tareas), 0)

    def test_modificar_tarea(self):
        agregar_tarea()
        modificar_tarea()
        self.assertEqual(tareas[0]['nombre'], 'Tarea Actualizada 1')

    def test_mostrar_tareas(self):
        agregar_tarea()
        mostrar_tareas()
        self.assertEqual(len(tareas), 1)

    def test_clase_tarea(self):
        tarea = Tarea("Tarea 1", "Trabajo", (2023, 10, 1), {"urgente"})
        self.assertEqual(str(tarea), "Nombre: Tarea 1, Categoría: Trabajo, Fecha de Vencimiento: 2023-10-01, Etiquetas: {'urgente'}")

    def test_clase_tarea_con_fecha_limite(self):
        tarea = TareaConFechaLimite("Tarea 1", "Trabajo", (2023, 10, 1), {"urgente"}, (2023, 10, 5))
        self.assertEqual(str(tarea), "Nombre: Tarea 1, Categoría: Trabajo, Fecha de Vencimiento: 2023-10-01, Etiquetas: {'urgente'}, Fecha Límite: 2023-10-05")

if __name__ == '__main':
    unittest.main()