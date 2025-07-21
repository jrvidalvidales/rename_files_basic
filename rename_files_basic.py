import os

# Path which contains the files
folder = "C:/Path/To/Your/PDFs" # Update the path

# Get list of file on folder
files = sorted(os.listdir(folder))

#Prefix and initial counter
prefix = "file_"
counter = 1

for file in files:
    old_path = os.path.join(folder, file)

    # Filter only PDF files (you may change the extension if needed)
    if file.lower().endswith(".pdf") and os.path.isfile(old_path):
        new_name = f"{prefix}{counter:03}.pdf" # Format: file_001.pdf

        new_path = os.path.join(folder, new_name)

        os.rename(old_path, new_path)
        print(f"Renamed: {file} ➜ {new_name}")
        counter += 1
