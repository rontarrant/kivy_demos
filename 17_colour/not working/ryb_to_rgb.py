## NOTE: DOESN'T WORK
def RybToRgb(ryb_color):
	r, y, b = ryb_color

	# Convert RYB to RGB approximately
	r = r * 1.0 + y * 0.0 + b * 0.0
	g = r * 0.0 + y * 1.0 + b * 0.0
	b = r * 0.0 + y * 0.0 + b * 1.0

	# Ensure values are clamped to the range [0, 1]
	r = min(1.0, r)
	g = min(1.0, g)
	b = min(1.0, b)

	return r, g, b

if __name__ == "__main__":
	# Example usage:
	ryb_color = (1.0, 0.0, 0.0)  # Pure Red (RYB values)

	rgb_color = RybToRgb(ryb_color)
	print("RGB color:", rgb_color)

	ryb2 = (0.0, 1.0, 1.0)
	rgb2 = RybToRgb(ryb2)
	print("RGB2: ", rgb2)