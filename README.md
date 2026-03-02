# READ

1️⃣ Define the file path
file = pathlib.Path("sample.txt")

This creates a relative path pointing to sample.txt in the current directory.

2️⃣ Open and read the file
with file.open("rt") as fh:

"r" = read mode

"t" = text mode

The with statement ensures the file is properly closed after reading.

3️⃣ Iterate through lines
for line in fh:
    print(line.strip())

Reads the file line by line

.strip() removes newline characters (\n)

4️⃣ Error Handling
except FileNotFoundError:

If sample.txt does not exist, the script prints:

Error: The file sample.txt was not found


# Append

1️⃣ Write to File (Overwrite Mode)
with open(file, "w") as f:

"w" mode creates the file if it doesn't exist.

If the file already exists, it overwrites its contents.

The user is prompted to enter text, which is written to the file.

2️⃣ Append to File
with open(file, "a") as f:

"a" mode adds new content to the end of the file.

Existing content remains unchanged.

The user enters additional text, which is appended.

3️⃣ Read Final Content
with open(file, "r") as f:

"r" mode reads the file.

Each line is printed using .strip() to remove newline characters.