import re

class Interpreter:
    def __init__(self):
        self.variables = {}

    def interpret(self, program):
        statements = program.split(';')
        for statement in statements:
            statement = statement.strip()
            if statement:
                if self.is_assignment(statement):
                    self.handle_assignment(statement)
                else:
                    print(f"Syntax error: Invalid statement - {statement}")
                    return

        uninitialized_variables = [var for var, val in self.variables.items() if val is None]
        if uninitialized_variables:
            print("Uninitialized variables:", uninitialized_variables)
            return

        print("Variable values:")
        for var, val in self.variables.items():
            print(f"{var} = {val}")

    def is_assignment(self, statement):
        return '=' in statement

    def handle_assignment(self, assignment):
        identifier, expression = assignment.split('=')
        identifier = identifier.strip()
        expression = expression.strip()
        if not self.is_valid_identifier(identifier):
            print(f"Syntax error: Invalid identifier - {identifier}")
            return
        if not self.is_valid_expression(expression):
            print(f"Syntax error: Invalid expression - {expression}")
            return
        value = self.evaluate_expression(expression)
        self.variables[identifier] = value

    def is_valid_identifier(self, identifier):
        return re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', identifier) is not None

    def is_valid_expression(self, expression):
        # Check for balanced parentheses
        if expression.count('(') != expression.count(')'):
            return False

        # Check for invalid characters
        return re.match(r'^[()+\-*/a-zA-Z0-9_ ]*$', expression) is not None

    def evaluate_expression(self, expression):
        try:
            return eval(expression, self.variables)
        except:
            print(f"Syntax error: Invalid expression - {expression}")
            return None
        
interpreter = Interpreter()
program = '''
    x = 1;
    y = 2;
    z = ---(x+y)*(x+-y);
'''
interpreter.interpret(program)