import re
pattern1 = r'.*ion$'
pattern2 = r'.*at[^irt].*$'
regex = re.compile(pattern2)
matching_words = []
with open("TP1/dico.txt", "r") as dic_fr:
    for line in dic_fr:
        if regex.match(line):
            matching_words.append(line.strip())

print(matching_words)
print(len(matching_words))