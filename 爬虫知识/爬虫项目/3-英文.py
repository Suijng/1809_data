file_name = 'ying.txt'
character_count = 0
with open(file_name, 'r', encoding='utf-8') as f:
    for line in f:
        word = line.split()
        character_count += len(line)
print('字母数：', character_count)
