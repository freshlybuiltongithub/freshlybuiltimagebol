from cv2 import fastNlMeansDenoisingColored
from cv2 import cvtColor
from cv2 import bitwise_not,threshold,getRotationMatrix2D
from cv2 import warpAffine,filter2D,imread
from cv2 import THRESH_BINARY,COLOR_BGR2GRAY,THRESH_OTSU
from cv2 import INTER_CUBIC,BORDER_REPLICATE,minAreaRect
from numpy import column_stack,array,where
from matplotlib.pyplot import imshow,xticks,yticks
from pytesseract import image_to_string,pytesseract 
from PIL import Image

class ImageProcess:
    '''this function is removing noise from the image'''
    def remove_noise(image):
        image = fastNlMeansDenoisingColored(image,None,20,10,7,21)
        return image

    '''this function is removing skewness.
    first, it calculate the angle and accordingly rotate image'''
    def remove_skew(image):
        in_gray = cvtColor(image, COLOR_BGR2GRAY)
        in_gray = bitwise_not(in_gray)
        thresh_pic = threshold(in_gray, 0, 255,THRESH_BINARY | THRESH_OTSU)[1]
        coords_x_y = column_stack(where(thresh_pic > 0))
        angle = minAreaRect(coords_x_y)[-1]
        if angle < -45:
            angle = -(90 + angle)
        else:
            angle = -angle
        (h, w) = image.shape[:2]
        center_of_pic = (w // 2, h // 2)
        M = getRotationMatrix2D(center_of_pic, angle, 1.0)
        image = warpAffine(image, M, (w, h),flags=INTER_CUBIC, borderMode=BORDER_REPLICATE)
        return image

    '''for removing blurness from the image,
    this function increase sharpness of the image.'''
    def sharpness_blur(image):
        sharpen_kernel = array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
        image = filter2D(image, -1, sharpen_kernel)
        return image

    '''using pytesseract, this function extracting text from the image.'''
    def to_text(image):
        try:
            pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
            string_from_image = image_to_string(image,lang='eng')
        except Exception:
            pytesseract.tesseract_cmd = r"C:\Program Files(x86)\Tesseract-OCR\tesseract.exe"
            string_from_image = image_to_string(image,lang='eng')
        return string_from_image

    ##plot image in output
    def plot_image(image):
        imshow(image)
        xticks([])
        yticks([])

