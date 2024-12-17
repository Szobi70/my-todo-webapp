FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """Read a text file and return a list of to-do items."""
    try:
        with open(filepath, "r") as file_open:
            # Minden sorvégi karakter eltávolítása
            todos_local = [line.strip() for line in file_open.readlines()]
        return todos_local
    except FileNotFoundError:
        # Ha a fájl nem létezik, visszaadunk egy üres listát
        return []

def write_todos(todos_arg, filepath=FILEPATH):
    """Write the list of to-dos to the text file."""
    with open(filepath, "w") as file_write:
        # Hozzáadjuk a sortörést minden elemhez
        todos_with_newlines = [todo + "\n" for todo in todos_arg]
        file_write.writelines(todos_with_newlines)


if __name__ == '__main__':
	print("Hello!")
	print(get_todos())