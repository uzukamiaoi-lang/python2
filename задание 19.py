#1
K = int(input("Введите K: "))
with open("input.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
with open("output.txt", "w", encoding="utf-8") as f:
    f.writelines(lines[-K:])
#2
K = int(input("Введите K: "))
with open("input.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
with open("input.txt", "w", encoding="utf-8") as f:
    f.writelines(lines[:-K])
   
#3
K = int(input("Введите K: "))
with open("input.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
with open("input.txt", "w", encoding="utf-8") as f:
    for line in lines:
        f.write(line[K:] if len(line) > K else "")
#4
with open("file1.txt", "r") as f1:
    lines1 = f1.readlines()
with open("file2.txt", "r") as f2:
    lines2 = f2.readlines()
if len(lines1) > len(lines2):
    lines2 += [""] * (len(lines1) - len(lines2))
combined_lines = [l1.rstrip('\n') + l2 for l1, l2 in zip(lines1, lines2)]
with open("result.txt", "w") as result:
    result.writelines(combined_lines)
#5
K = int(input("Введите K: "))
with open("input.txt", "r") as file:
    lines = file.readlines()
if 0 < K <= len(lines):
    del lines[K-1]  
with open("output.txt", "w") as file:
    file.writelines(lines)
#6
with open("input.txt", "r") as file:
    text = file.read()
punctuation = ".,;:!?-()[]{}'"
result = ""
for char in text:
    if char in punctuation:
        result += char
with open("punctuation.txt", "w") as file:
    file.write(result)
#7
total = 0
count = 0
with open("numbers.txt", "r") as file:
    for line in file:
        number = int(line.strip())  
        total += number
        count += 1
print(f"Количество чисел: {count}")
print(f"Сумма чисел: {total}")
#8
S = input("Введите строку S: ")
with open("input.txt", "r") as file:
    lines = file.readlines()
new_lines = []
for line in lines:
    if line.strip() == "":
        new_lines.append(S + "\n")
    else:
        new_lines.append(line)
with open("output.txt", "w") as file:
    file.writelines(new_lines)
#9

with open("input.txt", "r") as file:
    lines = file.readlines()
new_lines = []
for line in lines:
    line = line.strip()
    if len(line) % 2 == 1:
        line = " " + line
    centered_line = line.center(50) + "\n"
    new_lines.append(centered_line)
with open("output.txt", "w") as file:
    file.writelines(new_lines)
#10

with open("input.txt", "r") as file:
    lines = file.readlines()
count = 0
in_paragraph = False
for line in lines:
    if line.strip() != "":
        if not in_paragraph:
            count += 1
            in_paragraph = True
    else:
        in_paragraph = False
print("Количество абзацев:", count)
#11
with open("input.txt", "r") as file:
    lines = file.readlines()
new_lines = []
for line in lines:
    line = line.strip()
    right_aligned = line.rjust(50) + "\n"
    new_lines.append(right_aligned)
with open("output.txt", "w") as file:
    file.writelines(new_lines)
#12
with open("file2.txt", "r") as file2:
    content2 = file2.read()
with open("file1.txt", "r") as file1:
    content1 = file1.read()
combined_content = content2 + content1
with open("file1.txt", "w") as file1:
    file1.write(combined_content)
#13
K = int(input("Введите номер строки K: "))
with open("input.txt", "r") as file:
    lines = file.readlines()
if 0 < K <= len(lines):
    lines.insert(K - 1, "\n")
with open("output.txt", "w") as file:
    file.writelines(lines)
#14

with open("input.txt", "r") as file:
    lines = file.readlines()
new_lines = []
for line in lines:
    new_lines.append(line)
    if line.strip() == "":
        new_lines.append("\n")
with open("output.txt", "w") as file:
    file.writelines(new_lines)
#15
with open("input.txt", "r") as file:
    lines = file.readlines()
del lines[0]
del lines[-1]
with open("output.txt", "w") as file:
    file.writelines(lines)
