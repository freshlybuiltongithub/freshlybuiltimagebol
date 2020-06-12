import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pytesseract
from PIL import Image

class image_to_text:
    def remove_noise(image):
        image = cv2.fastNlMeansDenoisingColored(image,None,20,10,7,21)
        return image
    def remove_skew(image):
        in_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        in_gray = cv2.bitwise_not(in_gray)
        thresh_pic = cv2.threshold(in_gray, 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        coords_x_y = np.column_stack(np.where(thresh_pic > 0))
        angle = cv2.minAreaRect(coords_x_y)[-1]
        if angle < -45:
            angle = -(90 + angle)
        else:
            angle = -angle
        (h, w) = image.shape[:2]
        center_of_pic = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center_of_pic, angle, 1.0)
        image = cv2.warpAffine(image, M, (w, h),flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
        return image
    def shapness_blur(image):
        sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
        image = cv2.filter2D(image, -1, sharpen_kernel)
        return image
    def to_text(image):
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        string_from_image = pytesseract.image_to_string(image,lang='eng')
    ##plot image in output
    def plot_image(image):
        plt.imshow(image)
        plt.xticks([])
        plt.yticks([])







