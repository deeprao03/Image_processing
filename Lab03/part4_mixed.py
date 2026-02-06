import cv2
import numpy as np
from part1_intensity import gamma_correction

def mixed_enhancement(img):

    lap = cv2.Laplacian(img, cv2.CV_32F)

    sx = cv2.Sobel(img, cv2.CV_32F, 1, 0, ksize=3)
    sy = cv2.Sobel(img, cv2.CV_32F, 0, 1, ksize=3)

    grad = np.abs(sx) + np.abs(sy)

    temp = img.astype(np.float32) + lap + grad
    temp = np.clip(temp, 0, 255).astype(np.uint8)

    return gamma_correction(temp, 0.8)
