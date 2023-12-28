import re


def detect_dead_code(filepath):
    with open(filepath, 'r') as f:
        source_code = f.read()

    look_for_dead_methods(source_code=source_code)


def look_for_dead_methods(source_code):
    method_define_pattern = r'\b(public|protected|private|static)?\s*[a-zA-Z_][\w<>[\]]*\s+([a-zA-Z_]\w*)\s*\([^)]*\)\s*{'
    method_define = re.findall(method_define_pattern, source_code)

    defined_methods = set(match[1] for match in method_define)  # Extract method names
    used_methods = set()

    for method in defined_methods:
        if re.search(rf'\b{method}\s*\(', source_code):
            used_methods.add(method)

    unused_methods = defined_methods - used_methods

    for method in unused_methods:
        print(f'Unused method found: {method}')
    print(f"Total unused methods found: {len(unused_methods)}")


if __name__ == "__main__":
    detect_dead_code("dead_codes/Main.java")