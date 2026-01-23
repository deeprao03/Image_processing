# rotate.py
#
# Manual rotation about center

import math

def rotate_image(pixels, width, height, angle_deg):
    angle = math.radians(angle_deg)
    cosA = math.cos(angle)
    sinA = math.sin(angle)

    cx = width / 2
    cy = height / 2

    corners = [
        (-cx, -cy),
        (width-cx-1, -cy),
        (-cx, height-cy-1),
        (width-cx-1, height-cy-1)
    ]

    new_coords = [(x*cosA - y*sinA, x*sinA + y*cosA) for (x,y) in corners]

    min_x = min(c[0] for c in new_coords)
    max_x = max(c[0] for c in new_coords)
    min_y = min(c[1] for c in new_coords)
    max_y = max(c[1] for c in new_coords)

    new_width = int(max_x - min_x + 1)
    new_height = int(max_y - min_y + 1)

    new_pixels = [[(0,0,0) for _ in range(new_width)] for _ in range(new_height)]

    for y in range(height):
        for x in range(width):
            dx = x - cx
            dy = y - cy

            rx = dx*cosA - dy*sinA - min_x
            ry = dx*sinA + dy*cosA - min_y

            rx = int(rx)
            ry = int(ry)

            if 0 <= rx < new_width and 0 <= ry < new_height:
                new_pixels[ry][rx] = pixels[y][x]

    return new_width, new_height, new_pixels
