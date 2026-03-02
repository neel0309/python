import pathlib

file = pathlib.Path("output.txt")

try:
    with open(file, "w") as f:
        f.write(input("Enter text to write to the file:") + "\n")
    with open(file, "a") as f:
        print(f"Data successfully written to {file}")
        f.write(input("Enter additional text to append:")+ "\n")
        print(f"Data successfully appended")
    with open(file, "r") as f:
        print(f"Final content of {file}:")
        for line in f.readlines():
            print(line.strip())
except:
    print("File does not exist")


