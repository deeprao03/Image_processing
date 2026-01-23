# translate.py
#
# Manual translation

def translate_image(pixels, width, height, Tx, Ty):
    # Output size stays same
    new_width = width
    new_height = height

    new_pixels = [[(0,0,0) for _ in range(new_width)] for _ in range(new_height)]

    for y in range(height):
        for x in range(width):
            new_x = x + Tx
            new_y = y + Ty

            if 0 <= new_x < new_width and 0 <= new_y < new_height:
                new_pixels[new_y][new_x] = pixels[y][x]

    return new_width, new_height, new_pixels
