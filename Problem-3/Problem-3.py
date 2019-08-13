with open('outputlog.txt', 'w') as fout:
    with open('inputlog.txt', 'r') as fin:
        for line in fin.readlines():
            if 'error'.lower() in line or 'warning'.lower() in line:
                    fout.write(line)

