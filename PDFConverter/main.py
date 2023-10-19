from pdf2docx import Converter

pdf_path = "aCvENG.pdf"
docx_path = "aCvENG2.docx"

cv = Converter(pdf_path)
cv.convert(docx_path)
cv.close()