# shear.py
#
# Manual shearing with bounding box adjustment

def shear_image(pixels, width, height, Kx, Ky):
    # Compute new bounds
    corners = [
        (0,0),
        (width-1, 0),
        (0, height-1),
        (width-1, height-1)
    ]

    new_coords = [(x + Kx*y, y + Ky*x) for (x,y) in corners]
    
    min_x = min(c[0] for c in new_coords)
    max_x = max(c[0] for c in new_coords)
    min_y = min(c[1] for c in new_coords)
    max_y = max(c[1] for c in new_coords)

    new_width = int(max_x - min_x + 1)
    new_height = int(max_y - min_y + 1)

    new_pixels = [[(0,0,0) for _ in range(new_width)] for _ in range(new_height)]

    for y in range(height):
        for x in range(width):
            new_x = int(x + Kx*y - min_x)
            new_y = int(y + Ky*x - min_y)

            if 0 <= new_x < new_width and 0 <= new_y < new_height:
                new_pixels[new_y][new_x] = pixels[y][x]

    return new_width, new_height, new_pixels
