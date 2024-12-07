import re

def check_for_fixed_bounds(c_code):
    """
    Check that all loops (for, while, do-while) have fixed bounds.
    """
    issues = []

    # Regex patterns for different loop types
    for_pattern = re.compile(r'for\s*\(([^;]+);\s*([^;]+);\s*([^;]+)\)\s*\{')
    while_pattern = re.compile(r'while\s*\(([^)]+)\)\s*\{')
    do_while_pattern = re.compile(r'do\s*\{([^}]+)\}[\s]*while\s*\(([^)]+)\)\s*;')

    # Check all `for` loops
    for match in for_pattern.finditer(c_code):
        init_expr = match.group(1).strip()
        condition_expr = match.group(2).strip()
        increment_expr = match.group(3).strip()
        
        # Check if any of the expressions in the `for` loop contains variable-based conditions
        if not (is_fixed_bound(init_expr) and is_fixed_bound(condition_expr) and is_fixed_bound(increment_expr)):
            issues.append(f"Fixed bounds required for 'for' loop: {match.group(0)}")
    
    # Check all `while` loops
    for match in while_pattern.finditer(c_code):
        condition_expr = match.group(1).strip()
        
        # Check if the condition involves any variables
        if not is_fixed_bound(condition_expr):
            issues.append(f"Fixed bounds required for 'while' loop: {match.group(0)}")
    
    # Check all `do-while` loops
    for match in do_while_pattern.finditer(c_code):
        condition_expr = match.group(2).strip()
        
        # Check if the condition involves any variables
        if not is_fixed_bound(condition_expr):
            issues.append(f"Fixed bounds required for 'do-while' loop: {match.group(0)}")
    
    return issues

def is_fixed_bound(expression):
    """
    Checks if an expression involves only fixed bounds (e.g., constants, literals).
    """
    # A fixed bound expression should be a constant, a literal, or a simple integer comparison
    # It should not include variables or runtime-dependent expressions
    # Examples of fixed bounds: 10, 100, 0
    # Non-fixed bounds: n, x, some_function()

    # Regex to match expressions that involve only literals or constants
    constant_pattern = re.compile(r'^[0-9]+$')  # Matches only numeric constants

    # Check if the expression is a constant (a number or literal)
    if constant_pattern.match(expression):
        return True
    
    # Further checks can be added here for more complex constant expressions (e.g., mathematical constants)
    return False

def analyze_code(c_code):
    """
    Analyze C code for loops with non-fixed bounds.
    """
    issues = check_for_fixed_bounds(c_code)
    
    if not issues:
        issues.append("All loops have fixed bounds.")
    
    return issues

if __name__ == "__main__":
    # Sample C code with different loops
    c_code = """
    #include <stdio.h>
    void example_function() {
        int n = 10;

        // Fixed bound for loop
        for (int i = 0; i < 10; i++) {
            printf("%d\\n", i);
        }

        // Non-fixed bound for loop
        for (int i = 0; i < n; i++) {  // Issue: n is variable
            printf("%d\\n", i);
        }

        // Fixed bound while loop
        while (x < 5) {
            x++;
        }

        // Non-fixed bound while loop
        while (x < n) {  // Issue: n is variable
            x++;
        }

        // Fixed bound do-while loop
        do {
            x++;
        } while (x < 5);

        // Non-fixed bound do-while loop
        do {
            x++;
        } while (x < n);  // Issue: n is variable
    }
    """
    
    # Analyze the provided C code
    issues = analyze_code(c_code)
    
    # Output the issues found
    for issue in issues:
        print(issue)
