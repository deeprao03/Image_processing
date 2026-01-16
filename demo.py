import cv2
import os
from encoder import encode
from decoder import decode

print("\n===================================")
print("       IMAGE ENCODER / DECODER     ")
print("===================================\n")

# ---- Image Input ----
img_path = input("Enter input image filename (e.g., image.png): ").strip()

if not os.path.exists(img_path):
    print(f"\n[ERROR] File not found: {img_path}")
    exit()

# ---- Spatial Resolution Selection ----
print("\nSelect Spatial Resolution:")
print("  0 → 100 x 100")
print("  1 → 200 x 200")
print("  2 → 400 x 400")
print("  3 → 800 x 800")

while True:
    try:
        sidx = int(input("Enter choice (0-3): "))
        if sidx in [0, 1, 2, 3]:
            break
        else:
            print("Invalid choice! Please enter 0, 1, 2, or 3.")
    except ValueError:
        print("Invalid input! Please enter a number.")

# ---- Bit Depth Selection ----
print("\nSelect Intensity Bit-Depth:")
print("  0 → 1-bit  (2 gray levels)")
print("  1 → 2-bit  (4 gray levels)")
print("  2 → 4-bit  (16 gray levels)")
print("  3 → 8-bit  (256 gray levels)")

while True:
    try:
        bidx = int(input("Enter choice (0-3): "))
        if bidx in [0, 1, 2, 3]:
            break
        else:
            print("Invalid choice! Please enter 0, 1, 2, or 3.")
    except ValueError:
        print("Invalid input! Please enter a number.")

# ---- Encoding ----
outfile = "encoded_image.bin"
encode(img_path, sidx, bidx, outfile)

# ---- Decoding ----
img = decode(outfile)
# ensure folder exists
if not os.path.exists("results"):
    os.makedirs("results")

output_recon = "results/reconstructed.png"
cv2.imwrite(output_recon, img)

cv2.imshow("Reconstructed Image", img)
print(f"\n[INFO] Reconstructed image saved as: {output_recon}")
print("[INFO] Encoded file saved as: encoded_image.bin\n")

cv2.waitKey(0)
cv2.destroyAllWindows()
