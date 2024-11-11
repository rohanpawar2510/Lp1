class SymbolTable:
    def __init__(self):  # Fixed constructor name
        self.symbols = {}

    def add_symbol(self, label, address):
        if label not in self.symbols:
            self.symbols[label] = address

    def get_address(self, label):
        return self.symbols.get(label, None)

    def __str__(self):  # Fixed string representation method name
        return str(self.symbols)


class LiteralTable:
    def __init__(self):  # Fixed constructor name
        self.literals = []
        self.current_pool = 0
        self.pool_table = []

    def add_literal(self, literal):
        if literal not in (lit for lit, _ in self.literals):
            self.literals.append((literal, None))

    def allocate_literals(self, start_address):
        address = start_address
        for i, (literal, addr) in enumerate(self.literals):
            if addr is None:
                self.literals[i] = (literal, address)
                address += 1
        self.pool_table.append(len(self.literals))

    def get_address(self, literal):
        for lit, addr in self.literals:
            if lit == literal:
                return addr
        return None

    def __str__(self):  # Fixed string representation method name
        literals_str = "\n".join(f"{literal}: {addr}" for literal, addr in self.literals)
        pool_str = "\n".join(f"Pool {i+1}: {start}" for i, start in enumerate(self.pool_table))
        return f"Literals:\n{literals_str}\n\nPools:\n{pool_str}"


class IntermediateCode:
    def __init__(self):  # Fixed constructor name
        self.instructions = []

    def add_instruction(self, address, instruction, operand):
        self.instructions.append((address, instruction, operand))

    def __str__(self):  # Fixed string representation method name
        return '\n'.join(f"{addr}: {instr} {oprnd}" for addr, instr, oprnd in self.instructions)


class AssemblerPass1:
    def __init__(self):  # Fixed constructor name
        self.symbol_table = SymbolTable()
        self.literal_table = LiteralTable()
        self.intermediate_code = IntermediateCode()
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
            self.intermediate_code.add_instruction(self.location_counter, instruction, operand)
            self.location_counter += 1

    def assemble(self, source_code):
        for line in source_code:
            self.process_line(line)
        return self.symbol_table, self.literal_table, self.intermediate_code


# Sample source code for a pseudo-machine
source_code = [
    "START 100",
    "LOOP LOAD =3",
    "ADD =6",
    "STORE A",
    "LTORG",
    "B STORE =10",
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
