import re


def detect_dead_code(filepath):
    with open(filepath) as f:
        source_code = f.read()

    looks_for_dead_functions(source_code=source_code)


def looks_for_dead_functions(source_code):
    function_define = re.findall(r'^def\s+([a-zA-Z_]\w*)\s*\(([^)]*)\)\s*:\s*$', source_code, re.MULTILINE)
    
    if function_define:
        for match in function_define:
            function_name = match[0]

            function_calls = re.findall(rf'^\b(?!def\s+)({function_name})(\((.*?)\))?$', source_code, re.MULTILINE)

            if not function_calls:
                print(f'Unused function found def {match[0]}({match[1]}).')


if __name__ == "__main__":
    detect_dead_code("dead_codes/1.py")
