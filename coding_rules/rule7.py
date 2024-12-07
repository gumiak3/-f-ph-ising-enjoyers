import re

class CCodeComplianceChecker:
    def __init__(self, code):
        self.code = code
        self.functions = {}
        self.errors = []

    def extract_functions(self):
        """
        Extract function definitions and store metadata about them.
        """
        function_regex = re.compile(r"(\w+\s+\**\w+)\s*\(([^)]*)\)\s*{")
        matches = function_regex.finditer(self.code)

        for match in matches:
            return_type, params = match.group(1), match.group(2)
            function_name = return_type.split()[-1]
            return_type = return_type.rsplit(" ", 1)[0]
            self.functions[function_name] = {
                "return_type": return_type.strip(),
                "params": [p.strip().split()[-1] for p in params.split(",") if p.strip()],
                "body": self._get_function_body(function_name),
            }

    def _get_function_body(self, function_name):
        """
        Extract the function body using regex.
        """
        body_regex = re.compile(rf"{function_name}\s*\([^)]*\)\s*{{(.*?)}}", re.S)
        match = body_regex.search(self.code)
        return match.group(1) if match else ""

    def analyze_calls(self):
        """
        Analyze all function calls and verify if their return values are checked.
        """
        for function_name, details in self.functions.items():
            if details["return_type"] != "void":
                calls_regex = re.compile(rf"\b{function_name}\s*\([^)]*\)\s*;")
                calls = calls_regex.finditer(self.code)
                for call in calls:
                    before_call = self.code[:call.start()]
                    if not re.search(r"if\s*\(|while\s*\(|&&|\|\|", before_call[-50:]):
                        self.errors.append(
                            f"Return value of function '{function_name}' is not checked."
                        )

    def validate_parameters(self):
        """
        Ensure all parameters of each function are validated in its body.
        """
        for function_name, details in self.functions.items():
            for param in details["params"]:
                if param:  # Non-empty parameter
                    param_validation_pattern = re.compile(
                        rf"\bif\s*\(\s*{param}\s*(==|!=|>|<|>=|<=)\s*.*?\)"
                    )
                    if not param_validation_pattern.search(details["body"]):
                        self.errors.append(
                            f"Parameter '{param}' in function '{function_name}' is not validated."
                        )

    def check_compliance(self):
        """
        Check the compliance for all functions in the code.
        """
        self.extract_functions()
        self.analyze_calls()
        self.validate_parameters()

        if self.errors:
            print("Compliance errors found:")
            for error in self.errors:
                print(f"- {error}")
        else:
            print("All functions are compliant with the rule.")

if __name__ == "__main__":
    c_code = """
    int func1(int* param) {
        if (param != NULL) {
            return *param;
        }
        return 0;
    }

    int func2(int param) {
        return param * 2;
    }

    int main() {
        int value = func1(NULL);
        func2(value);
        if (value > 0) {
            // Do something
        }
        return 0;
    }
    """

    checker = CCodeComplianceChecker(c_code)
    checker.check_compliance()