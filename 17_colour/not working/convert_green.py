## NOTE: DOESN'T WORK
def ryb_green_to_rgb(ryb_green):
	r, y, b = ryb_green

	# Convert RYB green to RGB approximately
	r_rgb = r * 1.0
	g_rgb = (y + r) / 2.0
	b_rgb = b * 1.0

	# Ensure values are clamped to the range [0, 1]
	r_rgb = min(1.0, max(0.0, r_rgb))
	g_rgb = min(1.0, max(0.0, g_rgb))
	b_rgb = min(1.0, max(0.0, b_rgb))

	return r_rgb, g_rgb, b_rgb

# Example usage:
ryb_green = (0.0, 1.0, 1.0)  # Pure Green in RYB

rgb_green = ryb_green_to_rgb(ryb_green)
print("RGB green:", rgb_green)