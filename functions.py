FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    """
    Read todos from a text file
    :param filepath: path to the text file
    :return: list of todos
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """
    Write list of todos to a text file
    :param filepath: path to the text file
    :param todos_arg: list of todos
    :return: none
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    #todos = ["Get grocery\n", "Play soccer\n", "Run a marathon\n"]
    #write_todos(todos)
    todos = get_todos()
    print(todos)