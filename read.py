import pathlib

file = pathlib.Path("sample.txt")

print("Reading file content:")

try:
    with file.open ("rt") as fh:
        for line in fh:
           print(line.strip())
except FileNotFoundError:
    print(f"Error: The file {file} was not found")

