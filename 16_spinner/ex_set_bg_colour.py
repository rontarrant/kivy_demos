class Colour01Spinner(Spinner):
	def do_something(self, colour_name, label):
		print(f"Colour 01 is {self.text}")
		## look up new colour in dictionary
		new_colour = WebColours[colour_name]
		## The following two lines set the background color
		## of the Spinner itself.
		##self.background_normal = ""
		##self.background_color = WebColours[colour_name]
		## assign it to the chip
		label.dynamic_colour = new_colour
		print(f"Label colour_01 is set to: {label.dynamic_colour}")
