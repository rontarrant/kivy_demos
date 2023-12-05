# Window size.
# Access the Window's size (an AliasProperty) and report.
# Then change the size and report again.

from kivy.app import App
from kivy.core.window import Window

class WindowApp(App):
	def build(self):
		window_size = Window.size # get size
		
		print("window size: ", window_size)
		
		Window.size = (600, 1024) # set size
		
		print("Window.size: ", Window.size)
		
		return

if __name__ == "__main__":
	WindowApp().run()
	print("window size: ", window_size)
