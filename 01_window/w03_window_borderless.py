# borderless window
# Because there's no border (and therefore no close gadget
# use Ctrl-C to quit.

from kivy.app import App
from kivy.core.window import Window


class WindowApp(App):
	def build(self):
		borderless = Window.borderless # get state
		
		print("borderless: ", borderless)
		
		Window.borderless = True # set state
		
		print("Window.borderless: ", Window.borderless)
		
		return

if __name__ == "__main__":
	WindowApp().run()
	print("window size: ", window_size)
