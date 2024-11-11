import re

# Pass-I: Store macros
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

# Pass-I: Replace macros with definitions
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


# Pass-II: Generate the final code (machine or intermediate code)
def generate_final_code(expanded_code):
    # For simplicity, assume we convert the expanded code to an intermediate code
    # For now, we are just returning the expanded code as is.
    final_code = []
    lines = expanded_code.split("\n")
    
    for line in lines:
        line = line.strip()
        if line:  # Only process non-empty lines
            # For each line, generate intermediate code (just for demonstration)
            final_code.append(f"Generated: {line}")
    
    return "\n".join(final_code)

# Main function to simulate the entire macro processor
def macro_processor(source_code):
    macros = store_macros(source_code)  # Pass-I: Store macros
    print("Stored Macros:")
    for macro_name, macro_body in macros.items():
        print(f"{macro_name}: {macro_body}")
    
    expanded_code = replace_macros_with_definitions(source_code, macros)  # Pass-I: Replace invocations
    print("\nExpanded Code After Pass-I:")
    print(expanded_code)
    
    final_code = generate_final_code(expanded_code)  # Pass-II: Generate final code
    print("\nFinal Code After Pass-II:")
    print(final_code)


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

# Run the Macro Processor (Pass-I + Pass-II)
macro_processor(source_code)
