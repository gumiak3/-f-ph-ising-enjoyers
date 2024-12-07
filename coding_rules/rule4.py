import re

def check_function_length(c_code, max_lines=50):
    """
    Check that functions do not exceed a specified number of lines.
    """
    issues = []
    
    # Regular expression to match function definitions
    # Matches return_type function_name(...) {
    function_pattern = re.compile(r'\b[A-Za-z_][A-Za-z0-9_]*\s+[A-Za-z_][A-Za-z0-9_]*\s*\(.*?\)\s*\{')
    
    # Find all functions in the code
    functions = list(function_pattern.finditer(c_code))
    
    for func in functions:
        # Extract the function body (everything between '{' and '}')
        func_start = func.end() - 1  # Include the opening brace '{'
        func_end = find_matching_brace(c_code, func_start)
        
        if func_end == -1:
            issues.append("Malformed function: unmatched braces.")
            continue  # Skip malformed functions
        
        # Extract the function body
        function_body = c_code[func_start + 1:func_end].strip()  # Exclude the enclosing braces
        function_lines = function_body.split('\n')
        
        # Check the number of lines in the function body
        if len(function_lines) > max_lines:
            func_signature = c_code[func.start():func.start() + 100].split('\n')[0]  # Get the first line of the function signature
            issues.append(f"Function exceeds {max_lines} lines: {func_signature.strip()}")

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

def analyze_code(c_code, max_lines=50):
    """
    Analyze C code to check if any function exceeds the specified line limit.
    """
    issues = check_function_length(c_code, max_lines)
    
    if not issues:
        issues.append(f"All functions are within the {max_lines}-line limit.")
    
    return issues

if __name__ == "__main__":
    # Sample C code with various function lengths
    c_code = """
    #include <stdio.h>

    // A small function
    void small_function() {
        printf("Hello, World!\\n");
    }

    // A large function
    void large_function() {
        int i;
        for (i = 0; i < 100; i++) {
            printf("i = %d\\n", i);
        }
        printf("End of function.\\n");
        int i;
        for (i = 0; i < 100; i++) {
            printf("i = %d\\n", i);
        }
        printf("End of function.\\n");
        int i;
        for (i = 0; i < 100; i++) {
            printf("i = %d\\n", i);
        }
        printf("End of function.\\n");
        int i;
        for (i = 0; i < 100; i++) {
            printf("i = %d\\n", i);
        }
        printf("End of function.\\n");
        int i;
        for (i = 0; i < 100; i++) {
            printf("i = %d\\n", i);
        }
        printf("End of function.\\n");
        int i;
        for (i = 0; i < 100; i++) {
            printf("i = %d\\n", i);
        }
        printf("End of function.\\n");
        int i;
        for (i = 0; i < 100; i++) {
            printf("i = %d\\n", i);
        }
        printf("End of function.\\n");
        int i;
        for (i = 0; i < 100; i++) {
            printf("i = %d\\n", i);
        }
        printf("End of function.\\n");
        int i;
        for (i = 0; i < 100; i++) {
            printf("i = %d\\n", i);
        }
        printf("End of function.\\n");
        int i;
        for (i = 0; i < 100; i++) {
            printf("i = %d\\n", i);
        }
        printf("End of function.\\n");
        int i;
        for (i = 0; i < 100; i++) {
            printf("i = %d\\n", i);
        }
        printf("End of function.\\n");
        int i;
        for (i = 0; i < 100; i++) {
            printf("i = %d\\n", i);
        }
        printf("End of function.\\n");

        int i;
        for (i = 0; i < 100; i++) {
            printf("i = %d\\n", i);
        }
        printf("End of function.\\n");
        int i;
        for (i = 0; i < 100; i++) {
            printf("i = %d\\n", i);
        }
        printf("End of function.\\n");
        int i;
        for (i = 0; i < 100; i++) {
            printf("i = %d\\n", i);
        }
        printf("End of function.\\n");
        int i;
        for (i = 0; i < 100; i++) {
            printf("i = %d\\n", i);
        }
        printf("End of function.\\n");
    }

    void another_small_function() {
        printf("This is a short function.\\n");
    }
    """
    
    # Analyze the provided C code
    issues = analyze_code(c_code, max_lines=20)
    
    # Output the issues found
    for issue in issues:
        print(issue)
