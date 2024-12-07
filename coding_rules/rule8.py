import re

class PreprocessorComplianceChecker:
    def __init__(self, code):
        self.code = code
        self.errors = []

    def check_preprocessor_directives(self):
        """
        Analyze preprocessor directives for compliance.
        """
        # Regex to match preprocessor directives
        preprocessor_pattern = re.compile(r"^\s*#\s*(\w+)(.*)", re.MULTILINE)
        matches = preprocessor_pattern.findall(self.code)

        for directive, content in matches:
            directive = directive.strip()
            content = content.strip()

            if directive == "include":
                # Check for valid #include syntax
                if not re.match(r"<.*?>|\".*?\"", content):
                    self.errors.append(f"Invalid #include syntax: {content}")
            elif directive == "define":
                # Check for simple macro definitions (no parameters, no multiline)
                if re.search(r"\(.*?\)", content) or "\\" in content:
                    self.errors.append(f"Complex macro definition found: {content}")
            else:
                # Any other preprocessor directive is non-compliant
                self.errors.append(f"Non-compliant preprocessor directive: #{directive} {content}")

    def check_compliance(self):
        """
        Perform compliance check for preprocessor directives.
        """
        self.check_preprocessor_directives()

        if self.errors:
            print("Compliance errors found:")
            for error in self.errors:
                print(f"- {error}")
        else:
            print("All preprocessor directives are compliant with the rule.")

if __name__ == "__main__":
    c_code = """
    #include <stdio.h>
    #define MAX 100
    #define SQUARE(x) ((x) * (x)) // Complex macro
    #ifdef DEBUG
    #define DEBUG_PRINT(x) printf(x)
    #endif
    #include "custom_header.h"
    #undef MAX
    """

    checker = PreprocessorComplianceChecker(c_code)
    checker.check_compliance()