# import ast
#
#
# def detect_dead_code(filepath):
#     with open(filepath) as f:
#         source_code = f.read()
#
#     # Find all function definitions and variable assignments.
#     functions = {node.name for node in ast.walk(ast.parse(source_code)) if isinstance(node, ast.FunctionDef)}
#     variables = {node.targets[0].id for node in ast.walk(ast.parse(source_code)) if isinstance(node, ast.Assign)}
#     # print(variables)
#     # Find all function calls and variable names in expressions.
#     calls = set()
#     for node in ast.walk(ast.parse(source_code)):
#         if isinstance(node, ast.Name):
#             calls.add(node.id)
#         elif isinstance(node, ast.Attribute):
#             calls.add(node.attr)
#         elif isinstance(node, ast.BinOp):
#             if isinstance(node.left, ast.Name):
#                 calls.add(node.left.id)
#             if isinstance(node.right, ast.Name):
#                 calls.add(node.right.id)
#         elif isinstance(node, ast.Call):
#             if isinstance(node.func, ast.Name):
#                 calls.add(node.func.id)
#
#     # Exclude built-in functions and other unwanted entries.
#     calls.discard("print")
#     calls.discard("__name__")
#
#     # Find unused functions and variables.
#     unused_functions = functions - calls
#     # print(calls)
#     unused_variables = variables - calls
#
#     # Print the results.
#     if unused_functions:
#         print("Unused functions:")
#         for f in unused_functions:
#             print(f)
#
#     if unused_variables:
#         print("Unused variables:")
#         for v in unused_variables:
#             print(v)
#
#
# if __name__ == "__main__":
#     detect_dead_code("dead_codes/1.py")

# import ast
#
#
# def detect_dead_code(filepath):
#     with open(filepath) as f:
#         source_code = f.read()
#
#     # Find all function definitions and variable assignments.
#     functions = {node.name for node in ast.walk(ast.parse(source_code)) if isinstance(node, ast.FunctionDef)}
#     variables = {node.targets[0].id for node in ast.walk(ast.parse(source_code)) if isinstance(node, ast.Assign)}
#
#     # Initialize a dictionary to track variable and function usage.
#     usage_tracker = {name: 0 for name in functions.union(variables)}
#
#     def track_usage(node):
#         if isinstance(node, ast.Name) and node.id in usage_tracker:
#             usage_tracker[node.id] += 1
#         elif isinstance(node, ast.Attribute) and node.attr in usage_tracker:
#             usage_tracker[node.attr] += 1
#         elif isinstance(node, ast.FunctionDef):
#             usage_tracker[node.name] += 1
#
#     # Execute the code and track variable and function usage.
#     exec(compile(ast.parse(source_code), filename=filepath, mode='exec'), {}, {'track_usage': track_usage})
#
#     # Find unused functions and variables.
#     unused_functions = [name for name in functions if usage_tracker[name] == 0]
#     unused_variables = [name for name in variables if usage_tracker[name] == 0]
#
#     # Print the results.
#     if unused_functions:
#         print("Unused functions:")
#         for f in unused_functions:
#             print(f)
#
#     if unused_variables:
#         print("Unused variables:")
#         for v in unused_variables:
#             print(v)
#
#
# if __name__ == "__main__":
#     detect_dead_code("dead_codes/1.py")
#
# import ast
#
# def find_dead_functions(file_path):
#     with open(file_path, 'r') as file:
#         tree = ast.parse(file.read(), filename=file_path)
#
#     function_definitions = [node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
#     function_names = set(node.name for node in function_definitions)
#
#     # Find function calls within the code
#     function_calls = [node.func.id for node in ast.walk(tree) if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)]
#
#     # Identify dead functions
#     dead_functions = function_names - set(function_calls)
#
#     return dead_functions
#
# if __name__ == "__main__":
#     file_path = "dead_codes/1.py"
#     dead_functions = find_dead_functions(file_path)
#
#     if dead_functions:
#         print("Dead functions found:")
#         for function_name in dead_functions:
#             print(f"  {function_name}")
#     else:
#         print("No dead functions found.")
#
# import ast
#
# def find_dead_variables(code):
#     tree = ast.parse(code)
#     used_variables = set()
#
#     def visit_Name(node):
#         used_variables.add(node.id)
#
#     def visit_Assign(node):
#         for target in node.targets:
#             if isinstance(target, ast.Name):
#                 used_variables.discard(target.id)
#
#     def visit_FunctionDef(node):
#         # Exclude function arguments from dead variable analysis
#         for arg in node.args.args:
#             used_variables.add(arg.arg)
#
#     def visit(node):
#         method = 'visit_' + node.__class__.__name__
#         visitor = globals().get(method)
#         if visitor:
#             visitor(node)
#         for child in ast.iter_child_nodes(node):
#             visit(child)
#
#     visit(tree)
#
#     dead_variables = set(v for v in used_variables if v not in globals() and v not in locals())
#     return dead_variables
#
# if __name__ == "__main__":
#     python_code = """
# x = 5
# y = 10
# print(x)
# """
#
#     dead_variables = find_dead_variables(python_code)
#     print("Dead Variables:", dead_variables)
