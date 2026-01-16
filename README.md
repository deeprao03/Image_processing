# Image Encoder–Decoder (Sampling + Quantization)

This project demonstrates the concepts of **spatial resolution (sampling)** and **intensity resolution (quantization)** in digital image processing by designing a simple **image encoder–decoder** system with a custom binary file format.

The encoder takes an input image, crops it to a square, applies spatial sampling and intensity quantization, and stores the result in a compact `.bin` file.  
The decoder reads the binary file, extracts the header parameters, reconstructs the image, and displays it.

---

## 🎯 Objectives

- Understand spatial resolution reduction (sampling)
- Understand intensity resolution reduction (quantization)
- Implement custom file encoding with metadata
- Implement decoding and reconstruction pipeline
- Demonstrate trade-offs in image compression and quality

---

## 🧩 Features

✔ Converts any image to grayscale and crops to square  
✔ Adjustable spatial resolutions: `100, 200, 400, 800`  
✔ Adjustable bit depths: `1, 2, 4, 8 bits`  
✔ Custom 4-bit header format  
✔ Binary file output (`encoded_image.bin`)  
✔ Image decoding and reconstruction  
✔ User-interactive `demo.py` script  
✔ Compatible with OpenCV + NumPy  

---

## 📦 Directory Structure

project/
├── README.md
├── encoder.py
├── decoder.py
├── demo.py
├── image.png
├── encoded_image.bin
├── reconstructed.png
└── requirements.txt



---

## 🗜 Header Format (4-bit)

Each encoded file begins with a **4-bit header**:


### Spatial resolution index (`2 bits`)
| Index | Resolution |
|---|---|
| 00 | 100×100 |
| 01 | 200×200 |
| 10 | 400×400 |
| 11 | 800×800 |

### Bit-depth index (`2 bits`)
| Index | Bits | Levels |
|---|---|---|
| 00 | 1-bit | 2 levels |
| 01 | 2-bit | 4 levels |
| 10 | 4-bit | 16 levels |
| 11 | 8-bit | 256 levels |

#### Example:


---

## 🚀 Running the Project

### **1. Install Dependencies**

### **2. Run Demo**

The program will prompt for:

✔ input image  
✔ resolution selection  
✔ bit-depth selection  

---

## 📁 Encoder Output

After encoding:

encoded_image.bin

After decoding:

reconstructed.png


---

## 🧠 Concepts Explained

### **Spatial Resolution (Sampling)**
Reduces number of pixels → affects image detail

Example:
800×800 → 100×100


### **Intensity Resolution (Quantization)**
Reduces number of gray levels → introduces banding

Example:
8-bit (256 levels) → 2-bit (4 levels)


---

## 📊 Quality vs Compression Trade-offs

Higher sampling & bit-depth → better quality, larger size  
Lower sampling & bit-depth → lower quality, smaller size

---

## 👨‍💻 Technologies Used

- Python 3.x
- OpenCV (cv2)
- NumPy

---

## 📑 Report Use

This repository can be used to generate lab reports for:

✔ Digital Image Processing  
✔ Multimedia Systems  
✔ Signals & Systems  

---

## 🏁 Conclusion

This project successfully demonstrates how spatial and intensity resolution affect digital image quality and how custom encoding schemes can compactly represent image data for transmission and storage.

---
