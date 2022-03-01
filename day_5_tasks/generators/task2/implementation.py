def error_messages(path, mode):

    data = open(path, mode)

    while True:
        line = data.readline().lower()
        if not line:
            break
        if "error" in line:
            yield line.strip()

    data.close


for message in error_messages('log.txt', 'r'):
    print(message)
