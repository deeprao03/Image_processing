# image_writer.py
#
# Manual 24-bit BMP writer (no external libraries)
# Expects pixels[y][x] = (r, g, b)

def write_bmp(filename, width, height, pixels):
    # Calculate row padding
    row_bytes = width * 3
    padding = (4 - (row_bytes % 4)) % 4
    pixel_array_size = (row_bytes + padding) * height
    file_size = 54 + pixel_array_size

    with open(filename, "wb") as f:

        # === BMP FILE HEADER (14 bytes) ===
        f.write(b'BM')
        f.write(file_size.to_bytes(4, byteorder='little'))
        f.write((0).to_bytes(2, byteorder='little'))
        f.write((0).to_bytes(2, byteorder='little'))
        f.write((54).to_bytes(4, byteorder='little'))

        # === DIB HEADER (40 bytes) ===
        f.write((40).to_bytes(4, byteorder='little'))     # DIB header size
        f.write(width.to_bytes(4, byteorder='little', signed=True))
        f.write(height.to_bytes(4, byteorder='little', signed=True))  # bottom-up
        f.write((1).to_bytes(2, byteorder='little'))       # planes
        f.write((24).to_bytes(2, byteorder='little'))      # bits per pixel
        f.write((0).to_bytes(4, byteorder='little'))       # no compression
        f.write(pixel_array_size.to_bytes(4, byteorder='little'))
        f.write((2835).to_bytes(4, byteorder='little'))    # horizontal resolution
        f.write((2835).to_bytes(4, byteorder='little'))    # vertical resolution
        f.write((0).to_bytes(4, byteorder='little'))       # colors in palette
        f.write((0).to_bytes(4, byteorder='little'))       # important colors

        # === PIXEL ARRAY ===
        for row in reversed(pixels):   # bottom-up
            for (r, g, b) in row:
                f.write(bytes([b, g, r]))
            f.write(b'\x00' * padding)
