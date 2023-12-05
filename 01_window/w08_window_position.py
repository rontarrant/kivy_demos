# Bind the mouse down event to a callback
# method which prints mouse information
# at the time the mouse button was clicked.
# When that's done, the window closes.

from kivy.app import App
from kivy.core.window import Window


class WindowApp(App):
	def build(self):
		print("window position - left: ", Window.left, " top: ", Window.top)
		
		return

if __name__ == "__main__":
	WindowApp().run()
