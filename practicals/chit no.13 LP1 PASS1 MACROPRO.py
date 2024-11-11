import re

# Step 1: Define a function to identify and store macros
def store_macros(source_code):
    macros = {}  # Dictionary to store macros

    # Regular expression to identify macro definitions
    macro_pattern = re.compile(r"^(\w+)\s+MACRO(.*?)(?=\s+ENDMACRO|$)", re.DOTALL)

    # Iterate through the source code and identify macro definitions
    lines = source_code.split("\n")
    for line in lines:
        match = macro_pattern.match(line.strip())
        if match:
            macro_name = match.group(1)
            macro_body = match.group(2).strip()
            macros[macro_name] = macro_body

    return macros

# Step 2: Replace macro invocations with the corresponding definitions
def replace_macros_with_definitions(source_code, macros):
    # Regular expression to identify macro invocations
    invocation_pattern = re.compile(r"\b(\w+)\b")

    # Replace invocations with macro definitions
    lines = source_code.split("\n")
    processed_lines = []

    for line in lines:
        line = line.strip()
        if invocation_pattern.match(line):
            # Check if the line is a macro invocation
            words = line.split()
            for i, word in enumerate(words):
                if word in macros:
                    # Replace macro invocation with macro body
                    words[i] = macros[word]
            processed_lines.append(" ".join(words))
        else:
            processed_lines.append(line)

    return "\n".join(processed_lines)

# Main function to simulate the two-pass macro processor
def pass_one_of_macro_processor(source_code):
    macros = store_macros(source_code)  # Store macros from the source code
    print("Stored Macros:")
    for macro_name, macro_body in macros.items():
        print(f"{macro_name}: {macro_body}")

    processed_code = replace_macros_with_definitions(source_code, macros)  # Replace invocations
    return processed_code

# Example Source Code with Macro Definitions and Invocations
source_code = """
MACRO    ADD
    MOV AX, BX
    ADD AX, CX
ENDMACRO

MACRO    SUB
    MOV AX, BX
    SUB AX, CX
ENDMACRO

    ADD
    SUB
"""

# Call Pass-I
processed_code = pass_one_of_macro_processor(source_code)

# Print the processed code
print("\nProcessed Code (After Pass-I):")
print(processed_code)
