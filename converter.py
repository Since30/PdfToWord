from PIL import Image
from io import BytesIO
from pdf2docx import Converter
from docx2pdf import convert

def convert_pdf_to_docx(uploaded_file):
    images = []
    with Converter(BytesIO(uploaded_file.read())) as converter:
        for page in converter.pages:
            images.append(page.as_image())

    doc = convert(images)

    return doc

def convert_docx_to_pdf(uploaded_file):
    with open('uploaded.docx', 'wb') as f:
        uploaded_file.save(f)
    convert("uploaded.docx")
    return 'uploaded.pdf'
