# -------------------------------
# Two Pass Assembler (Simplified)
# -------------------------------

OPTAB = {
    "START": ("AD", 1),
    "END": ("AD", 2),
    "LTORG": ("AD", 3),
    "DS": ("DL", 1),
    "DC": ("DL", 2),
    "MOVER": ("IS", 1),
    "MOVEM": ("IS", 2),
    "ADD": ("IS", 3),
    "SUB": ("IS", 4),
    "MULT": ("IS", 5),
    "STOP": ("IS", 0)
}

REG = {
    "AREG": 1,
    "BREG": 2,
    "CREG": 3,
    "DREG": 4
}

def is_literal(x):
    return x.startswith('=')

# -------------------------------
# PASS 1
# -------------------------------
def pass1(program):
    LC = 0
    symtab = {}
    littab = []
    pooltab = [0]
    intermediate = []

    for line in program:
        parts = line.split()

        if parts[0] == "START":
            LC = int(parts[1])
            intermediate.append(f"(AD,01) (C,{LC})")

        elif parts[0] in OPTAB:
            op, code = OPTAB[parts[0]]

            if parts[0] == "LTORG" or parts[0] == "END":
                # Assign addresses to literals
                for i in range(pooltab[-1], len(littab)):
                    littab[i]["address"] = LC
                    LC += 1
                pooltab.append(len(littab))
                intermediate.append(f"(AD,{code:02})")

            else:
                intermediate.append(f"(IS,{code:02})")
                LC += 1

        else:
            # Label present
            symtab[parts[0]] = LC
            op = parts[1]

            if op == "DS":
                size = int(parts[2])
                intermediate.append(f"(DL,01) (C,{size})")
                LC += size

            elif op == "DC":
                intermediate.append(f"(DL,02) (C,{parts[2]})")
                LC += 1

            else:
                LC += 1

        # Handle literals
        for p in parts:
            if is_literal(p):
                if p not in [l["lit"] for l in littab]:
                    littab.append({"lit": p, "address": None})

    return symtab, littab, pooltab, intermediate


# -------------------------------
# DRIVER CODE
# -------------------------------
program = [
    "START 100",
    "MOVER AREG =5",
    "ADD BREG =1",
    "LTORG",
    "A DS 1",
    "END"
]

symtab, littab, pooltab, ic = pass1(program)

# -------------------------------
# OUTPUT
# -------------------------------
print("\n--- SYMBOL TABLE ---")
for k, v in symtab.items():
    print(k, "->", v)

print("\n--- LITERAL TABLE ---")
for i, l in enumerate(littab):
    print(i, l)

print("\n--- POOL TABLE ---")
for i, p in enumerate(pooltab):
    print(i, "->", p)

print("\n--- INTERMEDIATE CODE ---")
for line in ic:
    print(line)


-----------------


cd ~/Desktop
nano assembler.py
# paste code

python3 assembler.py


