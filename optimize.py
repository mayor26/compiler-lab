import re

def optimize_tac(code):
    const = {}
    used = set()
    optimized = []

    # ---------------------------
    # 1. Constant Folding
    # ---------------------------
    for line in code:
        m = re.match(r'(\w+)\s*=\s*(\d+)\s*([\+\-\*/])\s*(\d+)', line)
        if m:
            var, a, op, b = m.groups()
            val = str(eval(a + op + b))
            const[var] = val
            optimized.append(f"{var} = {val}")
        else:
            optimized.append(line)

    # ---------------------------
    # 2. Constant Propagation
    # ---------------------------
    new_code = []
    for line in optimized:
        for k, v in const.items():
            line = re.sub(rf'\b{k}\b', v, line)
        new_code.append(line)

    # ---------------------------
    # 3. Algebraic Simplification
    # ---------------------------
    simplified = []
    for line in new_code:
        line = re.sub(r'(\w+)\s*=\s*(\w+)\s*\+\s*0', r'\1 = \2', line)
        line = re.sub(r'(\w+)\s*=\s*0\s*\+\s*(\w+)', r'\1 = \2', line)
        line = re.sub(r'(\w+)\s*=\s*(\w+)\s*\*\s*1', r'\1 = \2', line)
        line = re.sub(r'(\w+)\s*=\s*1\s*\*\s*(\w+)', r'\1 = \2', line)
        line = re.sub(r'(\w+)\s*=\s*(\w+)\s*\*\s*0', r'\1 = 0', line)
        line = re.sub(r'(\w+)\s*=\s*0\s*\*\s*(\w+)', r'\1 = 0', line)
        simplified.append(line)

    # ---------------------------
    # 4. Dead Code Elimination
    # ---------------------------
    for line in simplified:
        parts = re.findall(r'\b[a-zA-Z]\w*\b', line)
        if len(parts) > 1:
            used.update(parts[1:])

    final = []
    for line in simplified:
        lhs = line.split('=')[0].strip()
        if lhs in used or '=' not in line:
            final.append(line)

    return final


# 🔹 Example TAC
code = [
    "t1 = 2 + 3",
    "t2 = t1 * 1",
    "t3 = t2 + 0",
    "t4 = t3 * 0",
    "t5 = t4 + 5"
]

result = optimize_tac(code)

print("Optimized Code:")
for line in result:
    print(line)
