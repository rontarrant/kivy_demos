## NOTE: DOESN'T WORK
def ryb_to_rgb(ryb_color):
    r, y, b = ryb_color

    # Red
    r = r * 1.0 + y * -0.166 + b * 0.5

    # Green
    g = r * -0.5 + y * 0.5 + b * -0.166

    # Blue
    b = r * -0.166 + y * 0.5 + b * 1.0

    # Ensure values are clamped to the range [0, 1]
    r = min(1.0, max(0.0, r))
    g = min(1.0, max(0.0, g))
    b = min(1.0, max(0.0, b))

    return r, g, b

# Testing with pure green (RYB values)
ryb_green = (0.0, 1.0, 1.0)  # Pure Green in RYB

rgb_color = ryb_to_rgb(ryb_green)
print("RGB color:", rgb_color)

# Example usage:
ryb_color = (1.0, 0.0, 0.0)  # Pure Red (RYB values)
rgb_color = ryb_to_rgb(ryb_color)
print("RGB color:", rgb_color)

ryb_color = (0.0, 1.0, 1.0)  # Pure Green (RYB values)
rgb_color = ryb_to_rgb(ryb_color)
print("RGB color:", rgb_color)