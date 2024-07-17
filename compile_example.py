def main():
    # Source code as a string
    source_code = """
def greet(name):
    print(f"Hello, {name}!")

for i in range(5):
    greet("Person " + str(i))
"""

    # Compile source code as a module
    compiled_module = compile(source_code, filename="<string>", mode="exec")
    exec(compiled_module)

    # Compile source code as an expression
    expression_code = "2 + 9"
    compiled_expression = compile(expression_code, filename="<string>", mode="eval")
    result = eval(compiled_expression)
    print("Result of the expression:", result)

    # Compile source code as a single interactive statement
    single_statement_code = "print('Hello, world!')"
    compiled_single_statement = compile(
        single_statement_code, filename="", mode="single"
    )
    exec(compiled_single_statement)


if __name__ == "__main__":
    main()
