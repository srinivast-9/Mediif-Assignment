with open('errorwarning.txt', 'w') as few:
    with open('log.txt', 'r') as fl:
        for line in fl.readlines():
            if 'error'.lower() in line or 'warning'.lower() in line:
                    few.writelines(line)
                    print(line)

