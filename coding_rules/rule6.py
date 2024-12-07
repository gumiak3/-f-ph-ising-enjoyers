import re

def check_scope_compliance(c_code):
    """
    Check that all data objects are declared at the smallest possible level of scope.
    """
    issues = []

    # Regular expressions to identify variable declarations and block scopes
    declaration_pattern = re.compile(r'\b(?:int|float|double|char|long|short|unsigned|bool)\s+\b([A-Za-z_][A-Za-z0-9_]*)')
    block_pattern = re.compile(r'\{|\}')

    # Track variable declarations and usage
    variables = {}  # Key: variable name, Value: {'declared': scope, 'used': [scopes]}
    scope_stack = []  # Stack to track current scope level
    current_scope = 0

    # Iterate through the code line by line
    lines = c_code.splitlines()
    for line_num, line in enumerate(lines):
        # Update scope based on '{' and '}'
        for match in block_pattern.finditer(line):
            if match.group() == '{':
                current_scope += 1
                scope_stack.append(current_scope)
            elif match.group() == '}':
                if scope_stack:
                    scope_stack.pop()
                current_scope -= 1

        # Find all variable declarations in the current line
        for match in declaration_pattern.finditer(line):
            var_name = match.group(1)
            if var_name not in variables:
                variables[var_name] = {'declared': current_scope, 'used': []}

        # Track usage of declared variables
        for var_name in variables.keys():
            if var_name in line and not re.search(rf'\b(?:int|float|double|char|long|short|unsigned|bool)\s+{var_name}\b', line):
                variables[var_name]['used'].append(current_scope)

    # Check scope compliance for each variable
    for var_name, info in variables.items():
        declared_scope = info['declared']
        used_scopes = set(info['used'])
        if not used_scopes:
            issues.append(f"Variable '{var_name}' declared in scope {declared_scope} but never used.")
        elif used_scopes and min(used_scopes) > declared_scope:
            issues.append(
                f"Variable '{var_name}' declared in scope {declared_scope} but only used in narrower scope(s): {sorted(used_scopes)}."
            )

    if not issues:
        issues.append("All variables are declared at the smallest possible level of scope.")

    return issues


if __name__ == "__main__":
    # Sample C code for testing
    c_code = """
    #include <stdio.h>

    void test_function() {
        int x = 10;  // Declared at function level but only used in a narrower block
        {
            printf("Value of x: %d\\n", x);
        }

        int y = 20;  // Declared at function level and used in multiple blocks
        {
            printf("Value of y in first block: %d\\n", y);
        }
        {
            printf("Value of y in second block: %d\\n", y);
        }
    }

    void another_test() {
        int z;  // Declared at function level but never used
    }

    int global_var = 100;  // Global variable
    """
    
    # Analyze the provided C code
    issues = check_scope_compliance(c_code)
    
    # Output the issues found
    for issue in issues:
        print(issue)
