import pathlib

file = pathlib.Path("/Users/neil/PyCharmMiscProject/python/sample.txt")

print("Reading file content:")

try:
    with file.open ("rt") as fh:
        for line in fh:
           content = fh.read()
           print(f"Line 1:{line}")
           print(f"Line 2:{line}")
except FileNotFoundError:
    print(f"Error: The file {file} was not found")

