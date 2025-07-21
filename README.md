# File Renaming Automation with Python

This Python script automatically renames all PDF files inside a selected folder, using a sequential format like `file_001.pdf`, `file_002.pdf`, etc. It's perfect for organizing invoices, receipts, or any document series with clean, consistent naming.

## Features

- Sequential renaming with padded numbering (`001`, `002`, `003`, ...)
- Works only on `.pdf` files to avoid renaming incorrect items, but can be customized to other extensions
- Prevents accidental renaming of folders or unsupported files
- Simple and efficient — no GUI required

## How to Use

1. Download or copy the script to your computer.
2. Open it in any Python editor (e.g., VS Code, Thonny).
3. Update the folder path in the script:
   ```python
   folder = 'C:/Path/To/Your/PDFs'
4. Run the script

**Note:** This script renames files permanently. Always make a beckup before use.

## Example Output

If your folder contains:

```plaintext
invoice_March.pdf
scan001.pdf
client_A_receipt.pdf
```

The rename files will be:

```plaintext
file_001.pdf
file_002.pdf
file-003.pdf
```

## Requirements
- Python 3.6+
- Basic understanding of how to edit Python Scripts

## Support & Customization
Need this with a graphical interface or support for other file types? I offer custom solutions through my Fiverr gig - from interactive bots to advanced automation.
