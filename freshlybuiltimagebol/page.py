from cv2 import (
    ADAPTIVE_THRESH_GAUSSIAN_C,
    BORDER_CONSTANT,
    CHAIN_APPROX_SIMPLE,
    COLOR_BGR2GRAY,
    MORPH_CLOSE,
    RETR_TREE,
    THRESH_BINARY,
    Canny,
    adaptiveThreshold,
    approxPolyDP,
    arcLength,
    bilateralFilter,
    contourArea,
    copyMakeBorder,
    cvtColor,
    findContours,
    getPerspectiveTransform,
    isContourConvex,
    medianBlur,
    morphologyEx,
    resize,
    warpPerspective,
)
from numpy import argmax, argmin, array, diff, float32, linalg, ones


class Page:
    def detect(image):
        """Finding Page."""
        image_edges = Page.edges_detection(image, 200, 250)

        closed_edges = morphologyEx(image_edges, MORPH_CLOSE, ones((5, 11)))
        page_contour = Page.find_page_contours(closed_edges, Page.resize(image))
        page_contour = page_contour.dot(Page.ratio(image))
        new_image = Page.persp_transform(image, page_contour)
        return new_image

    def resize(img, height=800, allways=False):
        """Resize image to given height."""
        if img.shape[0] > height or allways:
            rat = height / img.shape[0]
            return resize(img, (int(rat * img.shape[1]), height))

        return img

    def ratio(img, height=800):
        """Getting scale ratio."""
        return img.shape[0] / height

    def edges_detection(img, minVal, maxVal):
        """Preprocessing (gray, thresh, filter, border) + Canny edge detection."""
        img = cvtColor(Page.resize(img), COLOR_BGR2GRAY)

        img = bilateralFilter(img, 9, 75, 75)
        img = adaptiveThreshold(
            img, 255, ADAPTIVE_THRESH_GAUSSIAN_C, THRESH_BINARY, 115, 4
        )

        img = medianBlur(img, 11)

        img = copyMakeBorder(img, 5, 5, 5, 5, BORDER_CONSTANT, value=[0, 0, 0])
        return Canny(img, minVal, maxVal)

    def four_corners_sort(pts):
        """Sort corners in order: top-left, bot-left, bot-right, top-right."""
        dif = diff(pts, axis=1)
        summ = pts.sum(axis=1)
        return array(
            [pts[argmin(summ)], pts[argmax(dif)], pts[argmax(summ)], pts[argmin(dif)]]
        )

    def contour_offset(cnt, offset):
        """Offset contour because of 5px border."""
        cnt += offset
        cnt[cnt < 0] = 0
        return cnt

    def find_page_contours(edges, img):
        """Finding corner points of page contour."""
        contours, hierarchy = findContours(edges, RETR_TREE, CHAIN_APPROX_SIMPLE)

        height = edges.shape[0]
        width = edges.shape[1]
        MIN_COUNTOUR_AREA = height * width * 0.5
        MAX_COUNTOUR_AREA = (width - 10) * (height - 10)

        max_area = MIN_COUNTOUR_AREA
        page_contour = array(
            [[0, 0], [0, height - 5], [width - 5, height - 5], [width - 5, 0]]
        )

        for cnt in contours:
            perimeter = arcLength(cnt, True)
            approx = approxPolyDP(cnt, 0.03 * perimeter, True)

            if (
                len(approx) == 4
                and isContourConvex(approx)
                and max_area < contourArea(approx) < MAX_COUNTOUR_AREA
            ):

                max_area = contourArea(approx)
                page_contour = approx[:, 0]

        page_contour = Page.four_corners_sort(page_contour)
        return Page.contour_offset(page_contour, (-5, -5))

    def persp_transform(img, s_points):
        """Transform perspective from start points to target points."""
        height = max(
            linalg.norm(s_points[0] - s_points[1]),
            linalg.norm(s_points[2] - s_points[3]),
        )
        width = max(
            linalg.norm(s_points[1] - s_points[2]),
            linalg.norm(s_points[3] - s_points[0]),
        )

        t_points = array([[0, 0], [0, height], [width, height], [width, 0]], float32)

        if s_points.dtype != float32:
            s_points = s_points.astype(float32)

        M = getPerspectiveTransform(s_points, t_points)
        return warpPerspective(img, M, (int(width), int(height)))
