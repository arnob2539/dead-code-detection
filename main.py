from pycparser import parse_file, c_ast


def detect_dead_code(file_path):
    ast = parse_file(file_path, use_cpp=True)

    # Define a visitor to traverse the AST
    class DeadCodeVisitor(c_ast.NodeVisitor):
        def visit_FuncDef(self, node):
            # Add your dead code detection logic here
            # Example: check if function is never called
            if node.decl.name not in called_functions:
                print(f"Potential dead code: {node.decl.name}")

    # You need a list of called functions to determine dead code accurately
    called_functions = set()

    class FunctionCallVisitor(c_ast.NodeVisitor):
        def visit_FuncCall(self, node):
            if isinstance(node.name, c_ast.ID):
                called_functions.add(node.name.name)

    # Traverse the AST to collect called functions
    FunctionCallVisitor().visit(ast)
    # Traverse the AST again to detect dead code
    DeadCodeVisitor().visit(ast)


# Example usage:
detect_dead_code('your_c_file.c')
