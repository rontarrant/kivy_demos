## NOTE: DOESN'T WORK
def rgb_to_cmy(r, g, b):
	c = 1 - (r / 255.0)
	m = 1 - (g / 255.0)
	y = 1 - (b / 255.0)
	return c, m, y

def cmy_to_rgb(c, m, y):
	r = int((1 - c) * 255)
	g = int((1 - m) * 255)
	b = int((1 - y) * 255)
	return r, g, b


## Testing
if __name__ == "__main__":
	## convert red rgb to cmy and back
	red = (1.0, 0.0, 0.0)
	print("red: ", red)
	cmy_red = rgb_to_cmy(red[0], red[1], red[2])
	print("cmy_red: ", cmy_red)
	rgb_red = cmy_to_rgb(cmy_red[0], cmy_red[1], cmy_red[2])
	print("rgb_red: ", rgb_red)
	
	## convert blue rgb to cmy and back
	