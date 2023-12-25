import re

def detect_dead_code(file_path):
    with open(file_path, 'r') as file:
        source_code = file.read()

    # Define a regular expression for function declarations
    function_declaration_pattern = re.compile(r'\b(?:int|void|char|float)\s+([a-zA-Z_]\w*)\s*\([^)]*\)\s*{')

    # Find all function declarations in the source code
    function_declarations = function_declaration_pattern.findall(source_code)

    # Define a regular expression for function calls
    function_call_pattern = re.compile(r'\b([a-zA-Z_]\w*)\s*\([^)]*\)\s*;')

    # Find all function calls in the source code
    function_calls = function_call_pattern.findall(source_code)

    # Identify potential dead code by comparing function declarations and function calls
    dead_code = set(function_declarations) - set(function_calls)

    # Print potential dead code
    for dead_function in dead_code:
        print(f"Potential dead code: {dead_function}")

if __name__ == '__main__':
    # Example usage:
    detect_dead_code('dead_codes/1.c')
