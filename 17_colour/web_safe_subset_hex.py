WebColours = {	"Indigo": ('4B0082FF'),
					"Dark Magenta": ('8B008BFF'),
					"Medium Violet Red": ('C71585FF'),
					"Deep Pink": ('FF1493FF'),
					"Magenta": ('FF00FFFF'),
					"Maroon": ('800000FF'),
					"Saddle Brown": ('8B4513FF'),
					"Crimson": ('DC143CFF'),
					"Tomato": ('FF6347FF'),
					"Red": ('FF0000FF'),
					"Dark Red": ('8B0000FF'),
					"Fire Brick": ('B22222FF'),
					"Orange Red": ('FF4500FF'),
					"Dark Orange": ('FF8C00FF'),
					"Orange": ('FFA500FF'),
					"Dark Goldenrod": ('B8860BFF'),
					"Goldenrod": ('DAA520FF'),
					"Gold": ('FFD700FF'),
					"Yellow": ('FFFF00FF'),
					"Chartreuse": ('7FFF00FF'),
					"Lime": ('00FF00FF'),
					"Lime Green": ('32CD32FF'),
					"Green": ('008000FF'),
					"Dark Green": ('006400FF'),
					"Dark Olive Green": ('556B2FFF'),
					"Light Sea Green": ('20B2AAFF'),
					"Dark Slate Gray": ('2F4F4FFF'),
					"Teal": ('008080FF'),
					"Cyan": ('00FFFFFF'),
					"Turquoise": ('40E0D0FF'),
					"Dark Turquoise": ('00CED1FF'),
					"Steel Blue": ('4682B4FF'),
					"Deep Sky Blue": ('00BFFFFF'),
					"Blue": ('0000FFFF'),
					"Navy": ('000080FF'),
					"White": ('FFFFFFFF'),
					"Snow": ('FFFAFAFF'),
					"Beige": ('F5F5DCFF'),
					"Antique White": ('FAEBD7FF'),
					"White Smoke": ('F5F5F5FF'),
					"Ivory": ('FFFFF0FF'),
					"Azure": ('F0FFFFFF'),
					"Black": ('000000FF')
					}

def get_colour(colour):
	print("colour: ", colour)
	print("result: ", WebColours[colour])
	return WebColours[colour]

def nailed_colour():
	return '#CD5C5C'