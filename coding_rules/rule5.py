import re

def check_assertion_density(c_code, min_avg_assertions=2):
    """
    Check that the code's assertion density averages at least two assertions per function.
    """
    total_assertions = 0
    total_functions = 0
    issues = []
    
    # Regular expression to match function definitions
    function_pattern = re.compile(r'\b[A-Za-z_][A-Za-z0-9_]*\s+[A-Za-z_][A-Za-z0-9_]*\s*\(.*?\)\s*\{')
    
    # Regular expression to match assert statements
    assert_pattern = re.compile(r'\bassert\s*\(')
    
    # Find all functions in the code
    functions = list(function_pattern.finditer(c_code))
    
    for func in functions:
        total_functions += 1  # Increment function count
        # Extract the function body (everything between '{' and '}')
        func_start = func.end() - 1  # Include the opening brace '{'
        func_end = find_matching_brace(c_code, func_start)
        
        if func_end == -1:
            issues.append("Malformed function: unmatched braces.")
            continue  # Skip malformed functions
        
        # Extract the function body
        function_body = c_code[func_start + 1:func_end].strip()  # Exclude the enclosing braces
        
        # Count the number of assertions
        assertions = assert_pattern.findall(function_body)
        total_assertions += len(assertions)
    
    # Calculate assertion density
    if total_functions > 0:
        avg_assertions = total_assertions / total_functions
    else:
        avg_assertions = 0

    # Check if the average meets the required minimum
    if avg_assertions < min_avg_assertions:
        issues.append(
            f"Assertion density too low: average is {avg_assertions:.2f} assertions per function, "
            f"but minimum required is {min_avg_assertions}."
        )
    else:
        issues.append(
            f"Assertion density is sufficient: average is {avg_assertions:.2f} assertions per function."
        )

    return issues

def find_matching_brace(c_code, start_index):
    """
    Finds the index of the matching closing brace for a function body.
    Returns -1 if no matching brace is found.
    """
    stack = 0
    for i in range(start_index, len(c_code)):
        if c_code[i] == '{':
            stack += 1
        elif c_code[i] == '}':
            stack -= 1
            if stack == 0:
                return i
    return -1

if __name__ == "__main__":
    # Sample C code with various function lengths and assertions
    c_code = """
    #include <stdio.h>
    #include <assert.h>

    void function_with_assertions() {
        int x = 5;
        assert(x > 0);
        assert(x < 10);
        printf("Function executed successfully.\\n");
    }

    void function_without_assertions() {
        int y = 10;
        printf("This function has no assertions.\\n");
    }

    void function_with_one_assertion() {
        int z = -1;
        assert(z >= 0);
    }
    """
    
    # Analyze the provided C code
    issues = check_assertion_density(c_code, min_avg_assertions=2)
    
    # Output the issues found
    for issue in issues:
        print(issue)
