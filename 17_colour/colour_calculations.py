## Colour Calculations

class ColourCalculations():
	def half_and_half(self, colour_01, colour_02):
		## break the colours out into RGB values
		c1_r, c1_g, c1_b, c1_a = self.separate_rgb(colour_01)
		c2_r, c2_g, c2_b, c2_a = self.separate_rgb(colour_02)
		alpha = 1 ## assume full strength
		
		## mix components
		red = (c1_r + c2_r) / 2
		green = (c1_g + c2_g) / 2
		blue = (c1_b + c2_b) / 2
		alpha = (c1_a * .33) + (c2_a * .66)
		
		return (red, green, blue, alpha)

	def split_33_66(self, colour_01, colour_02):
		## break the colours out into RGB values
		c1_r, c1_g, c1_b, c1_a = self.separate_rgb(colour_01)
		c2_r, c2_g, c2_b, c2_a = self.separate_rgb(colour_02)
		
		## mix
		red = (c1_r * .33) + (c2_r * .66)
		green = (c1_g * .33) + (c2_g * .66)
		blue = (c1_b * .33) + (c2_b * .66)
		alpha = (c1_a * .33) + (c2_a * .66)
		
		return (red, green, blue, alpha)
		
	
	def colour_blend(self, colour_01, colour_02):
		## break the colours out into RGB values
		c1_r, c1_g, c1_b, c1_a = self.separate_rgb(colour_01)
		c2_r, c2_g, c2_b, c2_a = self.separate_rgb(colour_02)
		
		alpha = 1 - (1 - c1_a) * (1 - c2_a)
		red = c1_r * c1_a / alpha + c2_r * c2_a * (1 - c1_a) / alpha
		green = c1_g * c1_a / alpha + c2_g * c2_a * (1 - c1_a) / alpha
		blue = c1_b * c1_a / alpha + c2_b * c2_a * (1 - c1_a) / alpha
		
		return (red, green, blue, alpha)


	def separate_rgb(self, colour):
		## break the colours out into RGB values
		red = colour[0]
		green = colour[1]
		blue = colour[2]
		alpha = colour[3]
		
		return red, green, blue, alpha
		
## tests
colour_01 = (1, 0, 0, .5)
colour_02 = (0, 1, 0, .5)

## test 50/50
colcalc = ColourCalculations()
result = colcalc.half_and_half(colour_01, colour_02)
print("50/50: ", result)

## test 33/66
result = colcalc.split_33_66(colour_01, colour_02)
print("33/66: ", result)

result = colcalc.colour_blend(colour_01, colour_02)
print("colour blend: ", result)
