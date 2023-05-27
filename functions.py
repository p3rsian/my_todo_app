FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """"
    Read the file in the specified path and extract
    the todos in that file.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """"
        write todos in the file in the specified path
        """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello from functions")
    print(get_todos())