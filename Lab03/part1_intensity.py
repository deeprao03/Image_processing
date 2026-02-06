import numpy as np
import cv2

def log_transform(img):

    r = img.astype(np.float32)
    s = np.log(1 + r)
    s = 255 * s / np.max(s)

    return s.astype(np.uint8)


def gamma_correction(img, gamma):

    r = img.astype(np.float32) / 255.0
    s = np.power(r, gamma) * 255.0

    return np.clip(s, 0, 255).astype(np.uint8)


def bit_planes(img):

    planes = []
    for k in range(8):
        p = ((img >> k) & 1) * 255
        planes.append(p.astype(np.uint8))
    return planes
