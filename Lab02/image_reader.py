# image_reader.py
#
# Manual 24-bit BMP reader (no external libraries)
# Returns width, height, and pixel matrix pixels[y][x] = (r, g, b)

def read_bmp(filename):
    with open(filename, "rb") as f:
        data = f.read()

    # === BMP HEADER PARSING ===
    # Signature
    if data[0:2] != b'BM':
        raise ValueError("Not a BMP file or unsupported format")

    pixel_offset = int.from_bytes(data[10:14], byteorder='little')
    width = int.from_bytes(data[18:22], byteorder='little', signed=True)
    height = int.from_bytes(data[22:26], byteorder='little', signed=True)
    bpp = int.from_bytes(data[28:30], byteorder='little')

    if bpp != 24:
        raise ValueError("Only 24-bit BMP supported")

    # Determine orientation
    top_down = height < 0
    height = abs(height)

    # Calculate row padding (BMP rows padded to 4 bytes)
    row_bytes = width * 3
    padding = (4 - (row_bytes % 4)) % 4

    pixels = [[(0,0,0) for _ in range(width)] for _ in range(height)]

    # === PIXEL ARRAY ===
    index = pixel_offset

    for row in range(height):
        bmp_row = row if top_down else (height - 1 - row)
        for col in range(width):
            b = data[index]
            g = data[index+1]
            r = data[index+2]
            index += 3
            pixels[bmp_row][col] = (r, g, b)
        index += padding

    return width, height, pixels
