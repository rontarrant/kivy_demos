# on_flip seems to be about redrawing the window.
# So if something should be done each time the window
# is redrawn, connecting to the on_flip event seems
# to do the trick.

from kivy.app import App
from kivy.core.window import Window


class WindowApp(App):
	def build(self):
		Window.bind(on_flip = self.flip_stuff)
		
	
	def flip_stuff(self, window):
		print("This method fires when the window opens, when it receives focus, and when it's moved.")
		print("window: ", window)
		
		return

if __name__ == "__main__":
	WindowApp().run()
