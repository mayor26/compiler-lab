def pass1(lines):
    mnt = {}   # Macro Name Table
    mdt = []   # Macro Definition Table

    i = 0
    while i < len(lines):
        if lines[i] == "MACRO":
            i += 1
            macro_name = lines[i]
            mnt[macro_name] = len(mdt)

            i += 1
            while lines[i] != "MEND":
                mdt.append(lines[i])
                i += 1
        i += 1

    return mnt, mdt


def pass2(lines, mnt, mdt):
    output = []
    i = 0

    while i < len(lines):
        if lines[i] == "MACRO":
            # Skip macro definitions
            while lines[i] != "MEND":
                i += 1
        elif lines[i] in mnt:
            # Expand macro
            index = mnt[lines[i]]
            while index < len(mdt):
                output.append(mdt[index])
                index += 1
        else:
            output.append(lines[i])
        i += 1

    return output


# --------------------------
# Sample Input Program
# --------------------------
program = [
    "MACRO",
    "INCR",
    "A = A + 1",
    "MEND",
    "START",
    "INCR",
    "END"
]

# Pass 1
mnt, mdt = pass1(program)

print("MNT (Macro Name Table):")
print(mnt)

print("\nMDT (Macro Definition Table):")
for line in mdt:
    print(line)

# Pass 2
output = pass2(program, mnt, mdt)

print("\nExpanded Code:")
for line in output:
    print(line)


-----------------

cd ~/Desktop
nano macro_processor.py
# paste code, save

python3 macro_processor.py


sudo apt update
sudo apt install python3 -y
python3 --version
