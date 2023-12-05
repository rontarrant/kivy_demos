class Selector(Button, MouseOver):
	""" Base class for Prev and Next Image Buttons"""

	def on_hover(self):
		self.opacity = .8

	def on_exit(self):
		self.opacity = 0
