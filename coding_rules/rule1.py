import re

def check_goto(c_code):
    """
    Check for the presence of 'goto' in the C code.
    """
    # Regular expression to find any 'goto' statement in the code
    goto_pattern = re.compile(r'\bgoto\s+[A-Za-z_][A-Za-z0-9_]*;')
    return bool(goto_pattern.search(c_code))

def check_recursion(c_code):
    """
    Check for potential recursion in C code by looking for function calls
    where the function calls itself.
    """
    # Regular expression to find function definitions and calls
    function_pattern = re.compile(r'\b[A-Za-z_][A-Za-z0-9_]*\s+[A-Za-z_][A-Za-z0-9_]*\s*\(.*\)\s*\{')
    function_calls_pattern = re.compile(r'\b[A-Za-z_][A-Za-z0-9_]*\s*\(.*\)\s*;')

    # Extract all function names defined in the C code
    function_names = re.findall(r'\b[A-Za-z_][A-Za-z0-9_]*\s+[A-Za-z_][A-Za-z0-9_]*\s*\(.*\)\s*\{', c_code)
    function_names = [fn.split()[1].split('(')[0] for fn in function_names]

    # Check if any of the function names calls itself
    for fn in function_names:
        recursion_pattern = re.compile(r'\b' + re.escape(fn) + r'\b\s*\(.*\)\s*;')
        if recursion_pattern.search(c_code):
            return True
    return False

def analyze_code(c_code):
    """
    Analyzes C code to check for 'goto' and recursion.
    """
    issues = []
    
    # Check for goto
    if check_goto(c_code):
        issues.append("Goto statement found. Avoid complex flow constructs.")
    
    # Check for recursion
    if check_recursion(c_code):
        issues.append("Recursion detected. Avoid complex flow constructs.")
    
    if not issues:
        issues.append("No complex flow constructs detected.")
    
    return issues

if __name__ == "__main__":
    # Sample C code
    c_code = """
    #include <stdio.h>
    void recursive_function(int var) {
        int a = 5;
        int b = 3;
        int c = a + b
        recursive_function(c);  // Recursion here
    }
    
    void example_function() {
        int x = 0;
        if (x > 0) {
            goto end;  // Goto statement here
        }
    end:
        printf("End of function\\n");
    }
    """
    
    # Analyze the provided C code
    issues = analyze_code(c_code)
    
    # Output the issues found
    for issue in issues:
        print(issue)
