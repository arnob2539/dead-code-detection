import re


def detect_dead_code(file_path):
    with open(file_path, 'r') as file:
        source_code = file.read()

    function_declaration_pattern = re.compile(r'\b(?:int|void|char|float)\s+([a-zA-Z_]\w*)\s*\([^)]*\)\s*{')

    function_declarations = function_declaration_pattern.findall(source_code)

    function_call_pattern = re.compile(r'\b([a-zA-Z_]\w*)\s*\([^)]*\)\s*;')

    function_calls = function_call_pattern.findall(source_code)

    dead_code = set(function_declarations) - set(function_calls)

    for dead_function in dead_code:
        if dead_function == 'main':
            continue
        print(f"Potential dead code: {dead_function}")


if __name__ == '__main__':
    detect_dead_code('dead_codes/1.c')
