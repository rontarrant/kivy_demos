## NOTE: DOESN'T WORK
def RgbToRyb(rgb_color):
	r, g, b = rgb_color

	# Convert RGB to RYB approximately
	w = min(r, g, b)
	
	r -= w
	g -= w
	b -= w

	y = min(r, g)
	r -= y
	g -= y

	if g > 0 and b > 0:
		g /= 2.0
		b /= 2.0

	y += g
	b += g

	# Ensure values are clamped to the range [0, 1]
	r = min(1.0, r)
	y = min(1.0, y)
	b = min(1.0, b)

	return r, y, b

# Example usage:
if __name__ == "__main__":
	rgb_color = (1.0, 0.0, 0.0)  # Pure Red (RGB values)
	ryb_color = RgbToRyb(rgb_color)
	print("RYB color:", ryb_color)

	rgb_color = (1.0, 1.0, 0.0)  # Pure Yellow (RGB values)
	ryb_color = RgbToRyb(rgb_color)
	print("RYB color:", ryb_color)

	rgb_color = (0.0, 1.0, 0.0)  # Pure Green (RGB values)
	ryb_color = RgbToRyb(rgb_color)
	print("RYB color:", ryb_color)
