def error_messages(path, mode):

    file1 = open(path, mode)

    while True:
        line = file1.readline()
        if not line:
            break
        if "ERROR" in line:
            yield line.strip()

    file1.close


for message in error_messages('log.txt', 'r'):
    print(message)
