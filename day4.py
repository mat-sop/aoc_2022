with open("input.txt") as f:
    lines = f.read().split("\n")[:-1]

def sectors(elf):
    start, end = elf.split("-")
    return set(range(int(start), int(end)+1))

counter1 = 0
counter2 = 0
for line in lines:
    elf1, elf2 = line.split(",")
    s1 = sectors(elf1)
    s2 = sectors(elf2)
    if s1.issubset(s2) or s2.issubset(s1):
        counter1 += 1
    if s1.intersection(s2):
        counter2 += 1
        
print(counter1)
print(counter2)
