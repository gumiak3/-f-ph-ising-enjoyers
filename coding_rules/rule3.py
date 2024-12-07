import re

def check_heap_allocation(c_code):
    """
    Check for the usage of heap memory allocation functions.
    """
    issues = []
    
    # Regex patterns for heap allocation functions
    malloc_pattern = re.compile(r'\bmalloc\s*\(')
    calloc_pattern = re.compile(r'\bcalloc\s*\(')
    realloc_pattern = re.compile(r'\brealloc\s*\(')
    free_pattern = re.compile(r'\bfree\s*\(')

    # Check for malloc, calloc, realloc, and free
    if malloc_pattern.search(c_code):
        issues.append("Heap memory allocation detected: malloc()")
    if calloc_pattern.search(c_code):
        issues.append("Heap memory allocation detected: calloc()")
    if realloc_pattern.search(c_code):
        issues.append("Heap memory allocation detected: realloc()")
    if free_pattern.search(c_code):
        issues.append("Heap memory deallocation detected: free()")
    
    return issues

def analyze_code(c_code):
    """
    Analyze C code for heap memory allocation and deallocation.
    """
    issues = check_heap_allocation(c_code)
    
    if not issues:
        issues.append("No heap memory allocation detected.")
    
    return issues

if __name__ == "__main__":
    # Sample C code with heap memory allocation and deallocation
    c_code = """
    #include <stdio.h>
    #include <stdlib.h>

    void example_function() {
        int *arr = (int *)malloc(10 * sizeof(int));  // malloc is used here
        if (arr == NULL) {
            printf("Memory allocation failed\\n");
            return;
        }

        // realloc usage
        arr = (int *)realloc(arr, 20 * sizeof(int));  // realloc is used here

        free(arr);  // free is used here
    }
    """
    
    # Analyze the provided C code
    issues = analyze_code(c_code)
    
    # Output the issues found
    for issue in issues:
        print(issue)
