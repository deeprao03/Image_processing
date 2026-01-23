# scale.py
#
# Manual scaling using nearest neighbor

def scale_image(pixels, width, height, Sx, Sy):
    new_width = int(width * Sx)
    new_height = int(height * Sy)

    # Create new blank image
    new_pixels = [[(0,0,0) for _ in range(new_width)] for _ in range(new_height)]

    for y in range(new_height):
        for x in range(new_width):
            # inverse mapping
            orig_x = int(x / Sx)
            orig_y = int(y / Sy)

            if 0 <= orig_x < width and 0 <= orig_y < height:
                new_pixels[y][x] = pixels[orig_y][orig_x]

    return new_width, new_height, new_pixels
