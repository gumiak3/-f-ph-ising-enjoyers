import re

class PointerUsageComplianceChecker:
    def __init__(self, code):
        self.code = code
        self.errors = []

    def check_pointer_dereferences(self):
        """
        Check for multiple pointer dereferences in the code.
        """
        # Regex to find multiple pointer dereferences (e.g., **ptr, *(*ptr))
        multiple_dereference_pattern = re.compile(r"\*{2,}|\*\s*\(")
        matches = multiple_dereference_pattern.finditer(self.code)

        for match in matches:
            self.errors.append(
                f"Multiple pointer dereference found: {match.group().strip()} at position {match.start()}."
            )

    def check_function_pointers(self):
        """
        Check for the use of function pointers in the code.
        """
        # Regex to detect function pointer declarations (e.g., int (*func_ptr)())
        function_pointer_pattern = re.compile(r"\w+\s*\(\s*\*\s*\w+\s*\)\s*\(")
        matches = function_pointer_pattern.finditer(self.code)

        for match in matches:
            self.errors.append(
                f"Function pointer usage found: {match.group().strip()} at position {match.start()}."
            )

    def check_compliance(self):
        """
        Perform compliance checks for pointer usage.
        """
        self.check_pointer_dereferences()
        self.check_function_pointers()

        if self.errors:
            print("Compliance errors found:")
            for error in self.errors:
                print(f"- {error}")
        else:
            print("All pointer usages are compliant with the rule.")

if __name__ == "__main__":
    c_code = """
    int main() {
        int value = 10;
        int *ptr = &value;
        int **double_ptr = &ptr; // Multiple dereference
        *(*double_ptr) = 20;

        void (*func_ptr)() = NULL; // Function pointer declaration
        func_ptr = &main;          // Function pointer assignment
        return 0;
    }
    """

    checker = PointerUsageComplianceChecker(c_code)
    checker.check_compliance()