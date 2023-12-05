# Doing something with on_flip...
# Grabbing the window and moving it triggers window redraw,
# and when it's redrawn, the window's background colour changes.

from kivy.app import App
from kivy.core.window import Window
from kivy.properties import NumericProperty

class WindowApp(App):
	color = NumericProperty(0.0)
	
	def build(self):
		Window.bind(on_flip = self.increment_color)

	
	def increment_color(self, window):
		self.color += .05
		print("color: ", self.color)
		Window.clearcolor = (self.color, self.color, self.color)
		Window.clear()
		
		return

if __name__ == "__main__":
	WindowApp().run()
