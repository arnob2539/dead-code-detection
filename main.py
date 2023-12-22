import re


def main(filepath):
    code_mapping = {}
    source_code_lines = []

    with open(filepath) as f:
        for line_number, line in enumerate(f, start=1):
            code_mapping[line.strip()] = line_number
            source_code_lines.append(line.strip())

    source_code = '\n'.join(source_code_lines)

    looks_for_dead_function(source_code, code_mapping)
    looks_for_dead_variable(source_code, code_mapping)


def looks_for_dead_variable(source_code, code_mapping):
    variable_define_search = re.findall(r'^\s*([a-zA-Z_]\w*)\s*=\s*(.*?)(?=\n|\Z)', source_code, re.MULTILINE)

    print(variable_define_search)


def looks_for_dead_function(source_code, code_mapping):
    function_define_search = re.findall(r'^def\s+([a-zA-Z_]\w*)\s*\(([^)]*)\)\s*:', source_code, re.MULTILINE)

    print('Unused function found:')
    for function_name, function_args in function_define_search:
        function_calls = re.findall(rf'^\b(?!def\s+){function_name}\((.*?)\)?\s*$', source_code, re.MULTILINE)

        if not function_calls:
            function_full_define = f'def {function_name}({function_args}):'
            print(f'{function_full_define} at line {code_mapping[function_full_define]}.')


if __name__ == "__main__":
    main("dead_codes/1.py")
