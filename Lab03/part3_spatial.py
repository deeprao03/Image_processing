import cv2
import numpy as np

def box_filter(img, k):

    kernel = np.ones((k, k), np.float32) / (k * k)
    return cv2.filter2D(img, -1, kernel)


def gaussian_filter(img, k, sigma):

    return cv2.GaussianBlur(img, (k, k), sigma)


def laplacian_sharpen(img, c=1.0):

    lap = cv2.Laplacian(img, cv2.CV_32F)
    res = img.astype(np.float32) + c * lap

    return np.clip(res, 0, 255).astype(np.uint8)


def unsharp_mask(img, k=1.5):

    blur = cv2.GaussianBlur(img, (5, 5), 1.0)
    mask = img.astype(np.float32) - blur.astype(np.float32)

    res = img.astype(np.float32) + k * mask

    return np.clip(res, 0, 255).astype(np.uint8)
