import PyPDF2
import os

def merge_pdfs(input_pdfs, output_pdf):
    pdf_writer = PyPDF2.PdfWriter()

    for pdf_path in input_pdfs:
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                pdf_writer.add_page(page)

    with open(output_pdf, 'wb') as output_file:
        pdf_writer.write(output_file)

if __name__ == "__main__":
    # List of full paths to input PDF files
    input_pdfs = [
        "D:/PROGRAMACION/PDF Merge/1.pdf",
        "D:/PROGRAMACION/PDF Merge/2.pdf",
        "D:/PROGRAMACION/PDF Merge/3.pdf",
        "D:/PROGRAMACION/PDF Merge/4.pdf",
        "D:/PROGRAMACION/PDF Merge/5.pdf",
        "D:/PROGRAMACION/PDF Merge/6.pdf",
        "D:/PROGRAMACION/PDF Merge/7.pdf"
    ]

    # Full path to the merged output PDF file
    output_pdf = "D:/PROGRAMACION/PDF Merge/merge.pdf"

    merge_pdfs(input_pdfs, output_pdf)

    print(f"The merging process is complete. The file {output_pdf} has been created.")
