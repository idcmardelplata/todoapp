from todoapp.task  import Task

def test_dado_un_label_y_un_estado_deberia_crear_una_tarea():
    label = "ir a comprar puchos"
    status = "Done"
    task = Task(label = label, status = status)
    assert task.title() == label
