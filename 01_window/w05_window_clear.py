# set a background color, then clear the window with it.
# Unlike what I first thought, it doesn't cover up child
# widgets. It just changes the background colour for the
# window. Any child widgets with a transparent background
# will allow the window's background colour to show through.

from kivy.app import App
from kivy.core.window import Window


class WindowApp(App):
	def build(self):
		
		# clear colour (including transparency level)
		Window.clearcolor = (.5, .5, 0, 1)
		
		Window.clear()
		
		return

if __name__ == "__main__":
	WindowApp().run()
