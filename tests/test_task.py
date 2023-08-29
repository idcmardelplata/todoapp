from todoapp.task  import Task, TaskStatus
import pytest
from tests.helpers import MakeTask

# ¿Puede estar repetida una tarea?

@pytest.fixture
def task():
    return MakeTask().with_default_values()
    

def test_dado_un_label_y_un_estado_deberia_crear_una_tarea(task):
    assert task.title() == "Default task"

def test_la_tarea_puede_tener_2_estados(task):
    assert task.status() in [TaskStatus.Pending, TaskStatus.Done]

def test_el_label_debe_tener_255_caracteres():
    with pytest.raises(ValueError):
        task = MakeTask().with_long_title("very long title").build()

def test_status_debe_ser_por_defecto(task):
    assert task.status() == TaskStatus.Pending

def test_el_status_debe_ser_un_enum(task):
    assert type(task.status()) == TaskStatus

def test_debe_hacer_toggle_entre_estados(task):
    status = task.status()
    task.toggle_task()
    assert task.status() != status

