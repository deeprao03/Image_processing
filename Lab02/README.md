# Affine Image Transformation (Without In-Built Libraries)

## 1. Objective
To understand and manually implement affine transformations on a digital image by applying:
- Horizontal & Vertical Scaling
- Rotation
- Horizontal & Vertical Translation
- Horizontal & Vertical Shearing

The project demonstrates affine transformation mathematics without using any image processing libraries.

---

## 2. Problem Statement
Design and implement a program to perform an affine transformation on a given image. The user should be able to enter transformation parameters and generate a transformed output image.

---

## 3. Key Requirement
No in-built or external image processing libraries such as:
- OpenCV
- PIL/Pillow
- NumPy
- SciPy
- scikit-image

All operations are done using pure Python and manual pixel manipulation.

---

## 4. User Inputs

The following parameters are entered by the user:

| Parameter | Meaning |
|-----------|---------------------------|
| Sx | Horizontal scaling factor |
| Sy | Vertical scaling factor |
| θ | Rotation angle (degrees) |
| Tx | Horizontal translation |
| Ty | Vertical translation |
| Kx | Horizontal shear factor |
| Ky | Vertical shear factor |

---

## 5. Supported Operations

| Option | Operation | Output File |
|--------|-------------------|----------------------|
| 1 | Scale | `result/scaled.bmp` |
| 2 | Rotate | `result/rotated.bmp` |
| 3 | Translate | `result/translated.bmp` |
| 4 | Shear | `result/sheared.bmp` |
| 5 | Combined Affine | `result/combined.bmp` |

Each result opens automatically after generation.

---

## 6. Project Structure

```
Lab02/
├── main.py
├── image_reader.py
├── image_writer.py
├── scale.py
├── rotate.py
├── translate.py
├── shear.py
├── affine_matrix.py
├── input.bmp
├── README.md
└── result/
```


---

## 7. Image Format Constraint
The program works with:
- **24-bit BMP (uncompressed)**

Reason: BMP stores raw pixel data and does not require decoding libraries.

JPG/PNG are not used because they require decoder libraries, violating the project's rule.

---

## 8. How to Run

1. Place your input image in the project directory and rename it to `input.bmp`

2. Run the program:
   ```
   python main.py
   ```

3. Choose an operation and enter parameters when prompted.

4. Output image will be:
   - Saved in `result/`
   - Opened automatically

---

## 9. Mathematical Background

The affine transformation combines the following operations:

Affine Matrix:
A = T × R × H × S

Where:

### Scaling matrix (S):
````
[ Sx   0    0 ]
[ 0    Sy   0 ]
[ 0    0    1 ]
````
### Shearing matrix (H):
[ 1   Kx   0 ]
[ Ky  1    0 ]
[ 0   0    1 ]

### Rotation matrix (R):
[ cosθ  -sinθ   0 ]
[ sinθ   cosθ   0 ]
[ 0      0      1 ]

### Translation matrix (T):
[ 1   0   Tx ]
[ 0   1   Ty ]
[ 0   0   1  ]

### Final Mapping:
[ x' ]   [ a11  a12  a13 ]   [ x ]
[ y' ] = [ a21  a22  a23 ] × [ y ]
[ 1  ]   [ 0    0    1   ]   [ 1 ]

Nearest neighbor sampling is used for pixel assignment.

---

## 10. Features
✔ Manual BMP parsing  
✔ Manual affine matrix construction  
✔ No dependencies  
✔ Real pixel-level operations  
✔ Automatic output visualization  
✔ Works on Windows/Linux/Mac  

---

## 11. Limitations
- No anti-aliasing/interpolation
- Only 24-bit BMP supported
- Nearest-neighbor mapping only
- No compression handling

---

## 12. Conclusion
This project demonstrates affine transformations at a low level without relying on external libraries, making it suitable for academic use and understanding the underlying mathematics of image manipulation.

