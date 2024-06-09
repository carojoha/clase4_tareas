# Lista para almacenar las tareas
tareas = []

# Agregar tareas
tareas.insert(0, {'nombre': 'Tarea 1', 'descripcion': 'Descripción de la Tarea 1', 'estado': 'pendiente'})
tareas.insert(1, {'nombre': 'Tarea 2', 'descripcion': 'Descripción de la Tarea 2', 'estado': 'completada'})
tareas.insert(2, {'nombre': 'Tarea 3', 'descripcion': 'Descripción de la Tarea 3', 'estado': 'pendiente'})

# Mostrar tareas
print("Tareas ingresadas:")
for i, tarea in enumerate(tareas):
    print(f"Tarea {i+1}: {tarea['nombre']}, {tarea['descripcion']}, {tarea['estado']}")

# Eliminar una tarea
eliminada = tareas.pop(1)

# Mostrar tareas restantes
print("\nTareas restantes después de eliminar una:")
for i, tarea in enumerate(tareas):
    print(f"Tarea {i+1}: {tarea['nombre']}, {tarea['descripcion']}, {tarea['estado']}")