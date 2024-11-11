class SymbolTable:
    def __init__(self):  # Fixed constructor name
        self.symbols = {}

    def add_symbol(self, label, address):
        self.symbols[label] = address

    def get_address(self, label):
        return self.symbols.get(label)

    def __str__(self):  # Fixed string representation method name
        result = "Label       Address\n"
        result += "-" * 20 + "\n"
        for label, address in self.symbols.items():
            result += f"{label:<10} {address:<10}\n"
        return result


class LiteralTable:
    def __init__(self):  # Fixed constructor name
        self.literals = []
        self.pool_table = []

    def add_literal(self, literal):
        if literal not in [lit for lit, _ in self.literals]:
            self.literals.append((literal, None))  # Add literals with None as address initially

    def allocate_literals(self, start_address):
        address = start_address
        for i, (literal, addr) in enumerate(self.literals):
            if addr is None:  # Only allocate address if not already allocated
                self.literals[i] = (literal, address)
                address += 1
        self.pool_table.append(len(self.literals))

    def get_address(self, literal):
        for lit, addr in self.literals:
            if lit == literal:
                return addr
        return None

    def __str__(self):  # Fixed string representation method name
        literals_str = "Literal      Address\n"
        literals_str += "-" * 20 + "\n"
        for literal, addr in self.literals:
            literals_str += f"{literal:<10} {addr:<10}\n"

        pool_str = "Pool Table\n"
        pool_str += "-" * 20 + "\n"
        for i, start in enumerate(self.pool_table):
            pool_str += f"Pool {i+1}:   {start}\n"

        return f"{literals_str}\n{pool_str}"


class IntermediateCode:
    def __init__(self, instructions):  # Fixed constructor name
        self.instructions = instructions

    def __str__(self):  # Fixed string representation method name
        result = "Address   Instruction   Operand\n"
        result += "-" * 30 + "\n"
        for addr, instr, operand in self.instructions:
            result += f"{addr:<9} {instr:<12} {operand if operand else '':<9}\n"
        return result


class AssemblerPass1:
    def __init__(self):
        self.symbol_table = SymbolTable()
        self.literal_table = LiteralTable()
        self.intermediate_code = IntermediateCode([])
        self.location_counter = 0
        self.directives = {
            'START': self.start_directive,
            'END': self.end_directive,
            'LTORG': self.ltor_directive
        }

    def start_directive(self, operand):
        self.location_counter = int(operand)

    def end_directive(self, operand):
        self.literal_table.allocate_literals(self.location_counter)

    def ltor_directive(self, operand):
        self.literal_table.allocate_literals(self.location_counter)

    def process_line(self, line):
        label, instruction, operand = None, None, None
        parts = line.split()

        if len(parts) == 3:
            label, instruction, operand = parts
        elif len(parts) == 2:
            instruction, operand = parts
        elif len(parts) == 1:
            instruction = parts[0]

        if label:
            self.symbol_table.add_symbol(label, self.location_counter)

        if instruction in self.directives:
            self.directives[instruction](operand)
        else:
            if operand and operand.startswith('='):
                self.literal_table.add_literal(operand)
            self.intermediate_code.instructions.append((self.location_counter, instruction, operand))
            self.location_counter += 1

    def assemble(self, source_code):
        for line in source_code:
            self.process_line(line)
        return self.symbol_table, self.literal_table, self.intermediate_code


# Sample source code for a pseudo-machine
source_code = [
    "START 100",
    "LOOP LOAD =5",
    "ADD =10",
    "STORE A",
    "LTORG",
    "B STORE =15",
    "END"
]

assembler = AssemblerPass1()
symbol_table, literal_table, intermediate_code = assembler.assemble(source_code)

print("Symbol Table:")
print(symbol_table)
print("\nLiteral Table and Pools:")
print(literal_table)
print("\nIntermediate Code:")
print(intermediate_code)


class Pass2Assembler:
    def __init__(self, symbol_table, literal_table, intermediate_code):
        self.symbol_table = symbol_table
        self.literal_table = literal_table
        self.intermediate_code = intermediate_code
        self.opcode_mapping = {
            "LOAD": "01",
            "ADD": "02",
            "STORE": "03",
            # Add more opcodes here as needed
        }

    def generate_machine_code(self):
        machine_code = []

        print(f"{'Address':<10} {'Instruction':<15} {'Operand':<15} {'Machine Code':<15}")
        print("=" * 60)

        for addr, instr, operand in self.intermediate_code.instructions:
            code = self.opcode_mapping.get(instr, "??")  # Fallback if opcode is not recognized
            if operand:
                if operand.startswith('='):
                    # Handling literals
                    literal_address = self.literal_table.get_address(operand)
                    if literal_address is not None:
                        code += f"{literal_address:02d}"
                    else:
                        code += "??"  # Fallback if literal address is not recognized
                elif operand in self.symbol_table.symbols:
                    code += f"{self.symbol_table.get_address(operand):02d}"
                else:
                    code += "??"  # Fallback if operand address is not recognized
            else:
                code += "00"  # Default operand if none provided

            machine_code.append((addr, instr, operand, code))

        for addr, instr, operand, code in machine_code:
            print(f"{addr:<10} {instr:<15} {operand:<15} {code:<15}")


# Sample symbol table generated from Pass 1
symbol_table = SymbolTable()
symbol_table.add_symbol("LOOP", 100)
symbol_table.add_symbol("A", 103)
symbol_table.add_symbol("B", 105)

# Sample literal table generated from Pass 1
literal_table = LiteralTable()
literal_table.add_literal("=5")
literal_table.add_literal("=10")
literal_table.add_literal("=15")
literal_table.allocate_literals(104)

# Sample intermediate code generated from Pass 1
instructions = [
    (100, "LOAD", "=5"),
    (101, "ADD", "=10"),
    (102, "STORE", "A"),
    (103, "STORE", "=15")
]
intermediate_code = IntermediateCode(instructions)

# Perform Pass 2
pass2 = Pass2Assembler(symbol_table, literal_table, intermediate_code)
pass2.generate_machine_code()
