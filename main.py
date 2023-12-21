import ast

def detect_dead_code(filepath):
    with open(filepath) as f:
        source_code = f.read()

    # Find all function definitions and variable names.
    functions = {node.name for node in ast.walk(ast.parse(source_code)) if isinstance(node, ast.FunctionDef)}
    # print(functions)
    # Find all function calls and variable names in expressions.
    calls = set()
    for node in ast.walk(ast.parse(source_code)):
        if isinstance(node, ast.Name):
            calls.add(node.id)
        elif isinstance(node, ast.Attribute):
            # Handle Attribute nodes separately
            calls.add(node.attr)

    # Exclude built-in functions and other unwanted entries.
    # print(calls)
    calls.discard("print")
    calls.discard("__name__")
    # print(calls)
    # Find all unused functions.
    unused_functions = functions - calls

    # Print the unused functions.
    if unused_functions:
        print("Unused functions:")
        for f in unused_functions:
            print(f)

if __name__ == "__main__":
    detect_dead_code("dead_codes/1.py")
