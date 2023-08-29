from todoapp.task  import Task
import pytest

# ¿Puede estar repetida una tarea?
# ¿Deberia tener un metodo para hacer un toggle entre estados?
# ¿Deberia crear una factoria de tareas?
# El status deberia ser un enum


@pytest.fixture
def setup():
    label = "ir a comprar puchos"
    task = Task(label = label)
    return task
    

def test_dado_un_label_y_un_estado_deberia_crear_una_tarea(setup):
    assert setup.title() == "ir a comprar puchos"

def test_la_tarea_puede_tener_2_estados(setup):
    assert setup.status() in ["Done", "Pending"]

def test_el_label_debe_tener_255_caracteres():
    label = "label" * 500
    with pytest.raises(ValueError):
        task = Task(label = label)

def test_status_debe_ser_por_defecto():
    task = Task(label="some random content")
    assert task.status() == "Pending"

def test_fallar():
    assert False
