from todoapp.task  import Task
import pytest

# que pasa si el texto es muy largo
# ¿Puede estar repetida una tarea?
# ¿Deberia tener un metodo para hacer un toggle entre estados?
# ¿Deberia crear una factoria de tareas?
# El status deberia ser un enum
# El status deberia ser por defecto

def test_dado_un_label_y_un_estado_deberia_crear_una_tarea():
    label = "ir a comprar puchos"
    status = "Done"
    task = Task(label = label, status = status)
    assert task.title() == label

def test_la_tarea_puede_tener_2_estados():
    label = "ir a comprar puchos"
    status = "Done"
    task = Task(label = label, status = status)
    assert task.status() in ["Done", "Pending"]

def test_el_label_debe_tener_255_caracteres():
    label = "label" * 500
    status = "Done"
    with pytest.raises(ValueError):
        task = Task(label = label, status = status)


