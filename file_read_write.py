# file_read_write.py

try:
    with open("original.txt", "r") as infile:
        lines = infile.readlines()

    modified_lines = []
    for i, line in enumerate(lines, start=1):
        modified_line = f"{i}: {line.strip().upper()}\n"
        modified_lines.append(modified_line)

    with open("modified.txt", "w") as outfile:
        outfile.writelines(modified_lines)

    print("✅ File successfully read, modified, and saved as 'modified.txt'.")

except FileNotFoundError:
    print("❌ 'original.txt' not found. Please make sure the file exists.")
except Exception as e:
    print(f"⚠️ Unexpected error: {e}")
