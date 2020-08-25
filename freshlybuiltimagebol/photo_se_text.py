from PIL import Image
from pytesseract import image_to_pdf_or_hocr, image_to_string

"""
Type of:
photo_ka_naam: string
pdf_ka_naam: string

"""


class PhotoShabd:
    def photo_ka_text(photo_ka_naam):
        return image_to_string(Image.open(photo_ka_naam))

    def photo_ki_pdf(photo_ka_naam, pdf_ka_naam):
        pdf = image_to_pdf_or_hocr(photo_ka_naam, extension='pdf')
        with open(pdf_ka_naam, 'w+b') as f:
            f.write(pdf)
