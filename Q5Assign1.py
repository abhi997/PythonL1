chars = words = lines = 0

outfile = open('output.txt', 'w')


with open('a.txt', 'r') as in_file:
    for line in in_file:
        lines += 1
        words += len(line.split())
        chars += len(line)

print(chars,words,lines)

with open('output.txt','w') as f:

    f.write(str(lines))
    f.write("\n")
    f.write(str(words))
    f.write("\n")
    f.write(str(chars))