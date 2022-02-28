from contextlib import contextmanager


@contextmanager
def open_file(path, mode):
    data = open(path, mode)
    print(len(data.readlines()))
    data.close()
    data = open(path, mode)
    yield data
    data.close()


with open_file('file.txt', 'r') as fw:
    print(fw.read())
