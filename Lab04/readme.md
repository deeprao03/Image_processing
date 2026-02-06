2-D DFT and Centered DFT (Manual Implementation)
------------------------------------------------

Objective
---------
1. Generate the basis of an 8×8 2-D DFT and display it as a 64×64 image.
2. Create a binary 64×64 image containing a rectangle.
   - Take input for the top-left corner of the rectangle.
   - Take input for width and height in pixels.
3. Compute and plot the 2-D DFT of the image without using any FFT/DFT function.
4. Compute and plot the 2-D DFT of the centered image obtained by multiplying
   the image with (-1)^(x+y).

Folder structure
```
----------------
project/
│
├── main.py
├── dft2d.py
├── basis.py
└── result/
```
How to run
```
----------
python main.py

User input
----------
The program asks:
Row (x)
Column (y)
Width
Height
```

Implementation details
----------------------
- The 2-D DFT is implemented manually using nested loops.
- No built-in FFT or DFT functions are used.
- Centering is done using:

    f_c(x,y) = f(x,y) * (-1)^(x+y)

Output
------
All output images are saved in the folder:

result/

Files generated:
- dft_basis.png
- original_image.png
- DFT_of_original_image.png
- centered_image.png
- DFT_of_centered_image.png

Note
----
The implementation is intentionally slow because it uses a direct
DFT formula and not FFT.
