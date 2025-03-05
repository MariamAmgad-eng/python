# fileoperation.py

def read(filepath, option="all"):
    """Reads a file based on the specified option."""
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return {
                "all": file.read,
                "5": lambda: file.read(5),
                "line": file.readline,
                "lines": file.readlines
            }.get(option, lambda: "Invalid read option")()
    except FileNotFoundError:
        return "File not found"

def write(filepath, content, option="write"):
    """Writes or overwrites content in a file."""
    return _file_operation(filepath, content, option, mode="w")

def append(filepath, newcontent, option="write"):
    """Appends content to a file."""
    return _file_operation(filepath, newcontent, option, mode="a")

def _file_operation(filepath, content, option, mode):
    """Helper function to handle file writing and appending."""
    try:
        with open(filepath, mode, encoding="utf-8") as file:
            if option == "write":
                file.write(content)
            elif option == "lines" and isinstance(content, list):
                file.writelines(content)
            else:
                return "Invalid option or content format"
        return "Operation successful"
    except Exception as e:
        return f"Error: {e}"
