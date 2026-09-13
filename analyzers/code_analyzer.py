import ast


def analyze_code(code):
    try:
        tree = ast.parse(code)

        issues = []
        # Check for dangerous eval() usage
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                if isinstance(node.func, ast.Name) and node.func.id == "eval":
                    issues.append({
                        "type": "Security",
                        "message": "Avoid eval() because it can execute arbitrary code.",
                        "line": node.lineno
                    })
        # Check for print statements
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                if isinstance(node.func, ast.Name) and node.func.id == "print":
                    issues.append({
                        "type": "Code Quality",
                        "message": "Consider using logging instead of print() in production code.",
                        "line": node.lineno
                    })
        # Check for functions without a docstring
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                if ast.get_docstring(node) is None:
                    issues.append({
                        "type": "Code Quality",
                        "message": f"Function '{node.name}' has no docstring.",
                        "line": node.lineno
                    })
                 # Check for nested loops
                    for node in ast.walk(tree):
                        if isinstance(node, (ast.For, ast.While)):
                            for child in ast.walk(node):
                                if child is not node and isinstance(child, (ast.For, ast.While)):
                                    issues.append({
                                        "type": "Performance",
                                        "message": "Nested loop detected. Check whether this can be optimized.",
                                        "line": node.lineno
                                    })
                                    break

        return {
            "status": "success",
            "functions": len([
                node for node in ast.walk(tree)
                if isinstance(node, ast.FunctionDef)
            ]),
            "issues": issues
        }

    except SyntaxError as error:
        return {
            "status": "error",
            "message": "Syntax error found.",
            "line": error.lineno,
            "details": error.msg
        }
