dict_ = {}
for i in range(1, 4):
    up_name = f'{i}.txt'
    with open(up_name, 'r', encoding='utf-8') as file:
        dict_[up_name] = file.readlines()
with open('finall.txt', 'a', encoding='utf-8') as fi:
    for l in sorted(dict_.items(), key=lambda x: len(x[1])):
        fi.write(l[0] + '\n')
        fi.write(str(len(l[1])) + '\n')
        fi.write(''.join(l[1]) + '\n')