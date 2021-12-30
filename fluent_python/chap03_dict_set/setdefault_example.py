"""단어가 나타나는 위치를 가리키는 인덱스를 만든다"""
import sys
import re
import collections

WORD_RE = re.compile(r"\w+")

index = {}
index2 = collections.defaultdict(list)

with open(sys.argv[1], encoding="utf-8") as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)

            # not using default dict
            # occurrences = index.get(word, [])
            # occurrences.append(location)
            # index[word] = occurrences

            # using setdefault
            index.setdefault(word, []).append(location)

            # using defaultdict
            index2[word].append(location)

# print alphabet order
for word in sorted(index, key=str.upper):
    print(word, index[word])
