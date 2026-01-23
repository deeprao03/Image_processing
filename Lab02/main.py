# main.py

import os
from image_reader import read_bmp
from image_writer import write_bmp
from scale import scale_image
from rotate import rotate_image
from translate import translate_image
from shear import shear_image
from affine_matrix import build_affine, apply_affine


def ensure_result_folder():
    if not os.path.exists("result"):
        os.makedirs("result")


def open_image(path):
    try:
        full_path = os.path.abspath(path)
        if os.name == "nt":  # Windows
            os.startfile(full_path)
        elif hasattr(os, "uname") and os.uname().sysname == "Darwin":
            os.system(f"open '{full_path}'")  # macOS
        else:
            os.system(f"xdg-open '{full_path}'")  # Linux
    except Exception as e:
        print("Could not open image automatically:", e)


def main():
    input_file = "input.bmp"
    width, height, pixels = read_bmp(input_file)
    print(f"Loaded {input_file} ({width} x {height})")

    ensure_result_folder()

    print("\nSelect operation:")
    print("1) Scale")
    print("2) Rotate")
    print("3) Translate")
    print("4) Shear")
    print("5) Apply All (Combined Affine)")
    choice = input("Enter choice: ")

    # === SCALE ===
    if choice == "1":
        Sx = float(input("Enter Sx: "))
        Sy = float(input("Enter Sy: "))
        w2, h2, p2 = scale_image(pixels, width, height, Sx, Sy)
        path = "result/scaled.bmp"
        write_bmp(path, w2, h2, p2)
        print("Saved:", path)
        open_image(path)

    # === ROTATE ===
    elif choice == "2":
        angle = float(input("Enter angle (deg): "))
        w2, h2, p2 = rotate_image(pixels, width, height, angle)
        path = "result/rotated.bmp"
        write_bmp(path, w2, h2, p2)
        print("Saved:", path)
        open_image(path)

    # === TRANSLATE ===
    elif choice == "3":
        Tx = int(input("Enter Tx: "))
        Ty = int(input("Enter Ty: "))
        w2, h2, p2 = translate_image(pixels, width, height, Tx, Ty)
        path = "result/translated.bmp"
        write_bmp(path, w2, h2, p2)
        print("Saved:", path)
        open_image(path)

    # === SHEAR ===
    elif choice == "4":
        Kx = float(input("Enter Kx: "))
        Ky = float(input("Enter Ky: "))
        w2, h2, p2 = shear_image(pixels, width, height, Kx, Ky)
        path = "result/sheared.bmp"
        write_bmp(path, w2, h2, p2)
        print("Saved:", path)
        open_image(path)

    # === COMBINED ===
    elif choice == "5":
        Sx = float(input("Enter Sx: "))
        Sy = float(input("Enter Sy: "))
        angle = float(input("Enter angle (deg): "))
        Tx = int(input("Enter Tx: "))
        Ty = int(input("Enter Ty: "))
        Kx = float(input("Enter Kx: "))
        Ky = float(input("Enter Ky: "))
        A = build_affine(Sx, Sy, angle, Tx, Ty, Kx, Ky)
        w2, h2, p2 = apply_affine(pixels, width, height, A)
        path = "result/combined.bmp"
        write_bmp(path, w2, h2, p2)
        print("Saved:", path)
        open_image(path)

    else:
        print("Invalid choice. Exiting...")
        return

    print("\nOperation completed. Program exiting...")


if __name__ == "__main__":
    main()
