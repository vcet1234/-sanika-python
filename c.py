from contextlib import contextmanager
from fileinput import filename

@contextmanager
def genericFileFunction (filename, method):
    file = open (filename, method)
    yield file
    file.close ()

if __name__ == '__main__':
    with genericFileFunction("file.txt", "w") as file:
        print ('Middle')
        file.write('Hello from the function')

    with genericFileFunction("file.txt", "r") as file:
        print ('Middle')
        content = file.read()
    print("File after reading:")
    print(content)

    with genericFileFunction("file.txt", "a") as file:
        print('Appending to the file')
        file.write("This is some appended content.\n")

    with genericFileFunction("file.txt", "r") as file:
        updated_content = file.read()
    print("\nFile after appending:")
    print(updated_content)

   
