import os
import cv2

from part1_intensity import log_transform, gamma_correction, bit_planes
from part2_histogram import global_hist_eq, local_hist_eq
from part3_spatial import box_filter, gaussian_filter, laplacian_sharpen, unsharp_mask
from part4_mixed import mixed_enhancement


INPUT_FOLDER = "Lab03/Original_images"
OUTPUT_FOLDER = "Lab03/result"


for fname in os.listdir(INPUT_FOLDER):

    if not fname.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".tif")):
        continue

    path = os.path.join(INPUT_FOLDER, fname)

    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

    if img is None:
        continue

    name, _ = os.path.splitext(fname)

    # ---------- Part 1 ----------
    cv2.imwrite(os.path.join(OUTPUT_FOLDER, name + "_log.png"),
                log_transform(img))

    for g in [0.6, 0.4, 0.3, 3.0, 4.0, 5.0]:
        cv2.imwrite(os.path.join(OUTPUT_FOLDER, f"{name}_gamma_{g}.png"),
                    gamma_correction(img, g))

    planes = bit_planes(img)
    for i, p in enumerate(planes):
        cv2.imwrite(os.path.join(OUTPUT_FOLDER,
                                 f"{name}_bit_{i}.png"), p)

    # ---------- Part 2 ----------
    cv2.imwrite(os.path.join(OUTPUT_FOLDER, name + "_hist_eq.png"),
                global_hist_eq(img))

    cv2.imwrite(os.path.join(OUTPUT_FOLDER, name + "_local_hist_eq.png"),
                local_hist_eq(img))

    # ---------- Part 3 ----------
    cv2.imwrite(os.path.join(OUTPUT_FOLDER, name + "_box3.png"),
                box_filter(img, 3))

    cv2.imwrite(os.path.join(OUTPUT_FOLDER, name + "_box5.png"),
                box_filter(img, 5))

    cv2.imwrite(os.path.join(OUTPUT_FOLDER, name + "_gauss5.png"),
                gaussian_filter(img, 5, 1.0))

    cv2.imwrite(os.path.join(OUTPUT_FOLDER, name + "_laplacian.png"),
                laplacian_sharpen(img))

    cv2.imwrite(os.path.join(OUTPUT_FOLDER, name + "_unsharp.png"),
                unsharp_mask(img))

    # ---------- Part 4 ----------
    cv2.imwrite(os.path.join(OUTPUT_FOLDER, name + "_mixed.png"),
                mixed_enhancement(img))


print("All images processed for all 4 parts.")
