# This is how you work with PDFs with Python
import PyPDF2

with open('dummy.pdf', 'rb') as file:         # 'rb' stands for 'Read-Binary'
    reader = PyPDF2.PdfFileReader(file)       # Read from PDF file
    page = reader.getPage(0)                  # Get page info
    print(page)                               # Print page info
    page.rotateCounterClockwise(90)           # Rotate page
    writer = PyPDF2.PdfFileWriter()           # Write to PDF file
    writer.addPage(page)                      # Add page to PDF file
    with open('tilt.pdf', 'wb') as new_file:  # 'wb' stands for 'Write-Binary
        writer.write(new_file)                # Write to file to save changes