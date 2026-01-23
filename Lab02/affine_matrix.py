# affine_matrix.py
#
# Manual construction + application of affine transformation matrix
# Uses 7 parameters: Sx, Sy, θ, Tx, Ty, Kx, Ky

import math

# === Build individual matrices ===

def scale_matrix(Sx, Sy):
    return [
        [Sx, 0, 0],
        [0, Sy, 0],
        [0, 0, 1]
    ]

def shear_matrix(Kx, Ky):
    return [
        [1, Kx, 0],
        [Ky, 1, 0],
        [0, 0, 1]
    ]

def rotation_matrix(angle_deg):
    angle = math.radians(angle_deg)
    c = math.cos(angle)
    s = math.sin(angle)
    return [
        [c, -s, 0],
        [s,  c, 0],
        [0,  0, 1]
    ]

def translation_matrix(Tx, Ty):
    return [
        [1, 0, Tx],
        [0, 1, Ty],
        [0, 0, 1]
    ]


# === Manual 3x3 Matrix Multiplication ===

def matmul(A, B):
    result = [[0]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                result[i][j] += A[i][k] * B[k][j]
    return result


# === Build Final Affine Matrix ===

def build_affine(Sx, Sy, angle, Tx, Ty, Kx, Ky):
    S = scale_matrix(Sx, Sy)
    H = shear_matrix(Kx, Ky)
    R = rotation_matrix(angle)
    T = translation_matrix(Tx, Ty)

    # A = T * R * H * S
    A = matmul(T, matmul(R, matmul(H, S)))
    return A


# === Apply Matrix to Image ===

def apply_affine(pixels, width, height, A):
    # Transform corners to compute bounding box
    corners = [(0,0), (width-1,0), (0,height-1), (width-1,height-1)]

    transformed = []
    for (x,y) in corners:
        nx = A[0][0]*x + A[0][1]*y + A[0][2]
        ny = A[1][0]*x + A[1][1]*y + A[1][2]
        transformed.append((nx, ny))

    min_x = min(p[0] for p in transformed)
    max_x = max(p[0] for p in transformed)
    min_y = min(p[1] for p in transformed)
    max_y = max(p[1] for p in transformed)

    new_width = int(max_x - min_x + 1)
    new_height = int(max_y - min_y + 1)

    # Create empty output (black background)
    new_pixels = [[(0,0,0) for _ in range(new_width)] for _ in range(new_height)]

    # Forward mapping
    for y in range(height):
        for x in range(width):
            nx = A[0][0]*x + A[0][1]*y + A[0][2] - min_x
            ny = A[1][0]*x + A[1][1]*y + A[1][2] - min_y

            nx = int(nx)
            ny = int(ny)

            if 0 <= nx < new_width and 0 <= ny < new_height:
                new_pixels[ny][nx] = pixels[y][x]

    return new_width, new_height, new_pixels
