from contextlib import contextmanager


@contextmanager
def genericFileFunction(filename, method):
    file = open(filename, method)
    yield file
    file.close()

if __name__ == '__main__':
    with genericFileFunction('./file.txt', "w") as f:
        print("midddle")
        f.write("This is the initial content.\n")

    with genericFileFunction('./file.txt', "r") as f:
        print("Initial content")
        content=f.read()
        print("read file content",content)

    
    with genericFileFunction('./file.txt', "a") as f:
        print("appending file")
        f.write("This is the appended content.\n")

    
    with genericFileFunction('./file.txt', "r") as f:
        print("\nUpdated file content:")
        print(f.read())
