from cv2 import FONT_HERSHEY_SIMPLEX, imread, imshow, putText, rectangle, resize
from cv2.dnn import blobFromImage, readNet
from imutils.object_detection import non_max_suppression
from numpy import array, cos, sin
from pytesseract import image_to_string

# from playsound import playsound
# from .text_bol_uthega import ShabdDhwani

'''
USE CASE
=====================
from freshlybuiltimagebol import NaturalPhotoShabd
img=cv2.imread(path_to_image)
out=NaturalPhotoShabd.text_pehchano(img)
cv2.imshow('output',out)
'''


class NaturalPhotoShabd:
    def result_vyakhya_kro(scores, geometry, min_confidence):
        (numRows, numCols) = scores.shape[2:4]
        rects = []
        confidences = []
        for y in range(0, numRows):
            scoresData = scores[0, 0, y]
            xData0 = geometry[0, 0, y]
            xData1 = geometry[0, 1, y]
            xData2 = geometry[0, 2, y]
            xData3 = geometry[0, 3, y]
            anglesData = geometry[0, 4, y]
            for x in range(0, numCols):
                if scoresData[x] < min_confidence:
                    continue
                (offsetX, offsetY) = (x * 4.0, y * 4.0)
                angle = anglesData[x]
                c = cos(angle)
                s = sin(angle)
                h = xData0[x] + xData2[x]
                w = xData1[x] + xData3[x]
                endX = int(offsetX + (c * xData1[x]) + (s * xData2[x]))
                endY = int(offsetY - (s * xData1[x]) + (c * xData2[x]))
                startX = int(endX - w)
                startY = int(endY - h)
                rects.append((startX, startY, endX, endY))
                confidences.append(scoresData[x])
        return (rects, confidences)

    def text_pehchano(image, min_confidence=0.85, width=320, height=320, padding=0.00):
        '''
        image=input image (type=numpy.ndarray)
        min_confidence= minimum confidence threshold to detect text from image (default=0.85)
        width=resizing width of image (default=320)
        height=resizing height of image (default=320)
        padding =
        '''
        east = 'freshlybuiltimagebol/models/frozen_east_text_detection.pb'
        orig = image.copy()
        (origH, origW) = image.shape[:2]
        (newW, newH) = (width, height)
        rW = origW / float(newW)
        rH = origH / float(newH)
        image = resize(image, (newW, newH))
        (H, W) = image.shape[:2]
        layerNames = ["feature_fusion/Conv_7/Sigmoid", "feature_fusion/concat_3"]
        net = readNet(east)
        blob = blobFromImage(
            image, 1.0, (W, H), (123.68, 116.78, 103.94), swapRB=True, crop=False
        )
        net.setInput(blob)
        (scores, geometry) = net.forward(layerNames)
        (rects, confidences) = NaturalPhotoShabd.result_vyakhya_kro(
            scores, geometry, min_confidence
        )
        boxes = non_max_suppression(array(rects), probs=confidences)
        results = []
        for (startX, startY, endX, endY) in boxes:
            startX = int(startX * rW)
            startY = int(startY * rH)
            endX = int(endX * rW)
            endY = int(endY * rH)
            dX = int((endX - startX) * padding)
            dY = int((endY - startY) * padding)
            startX = max(0, startX - dX)
            startY = max(0, startY - dY)
            endX = min(origW, endX + (dX * 2))
            endY = min(origH, endY + (dY * 2))
            roi = orig[startY:endY, startX:endX]
            config = "-l eng --psm 7"
            text = image_to_string(roi, config=config)
            results.append(((startX, startY, endX, endY), text))
        results = sorted(results, key=lambda r: r[0][1])
        output = orig.copy()
        for ((startX, startY, endX, endY), text) in results:
            # print("OCR TEXT : ",text)
            text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
            # ShabdDhwani.shabd_se_dhwani(text,'english',"out.mp3")
            # playsound('out.mp3')
            rectangle(output, (startX, startY), (endX, endY), (0, 0, 255), 1)
            putText(
                output,
                text,
                (startX, startY - 20),
                FONT_HERSHEY_SIMPLEX,
                0.5,
                (255, 0, 0),
                2,
            )
        return output
