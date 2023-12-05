# A window's children
# Show that the window has no children,
# then add a Label to the window and show that
# it now has children.
# Then access the text property of the label via
# the Window's list of children and change the text.

from kivy.app import App
from kivy.core.window import Window


class WindowApp(App):
	def build(self):
		Window.bind(on_resize = self.on_window_resize)
		
	def on_window_resize(self, window, width, height):
		print("width: ", width)
		print("height: ", height)
		
		return

if __name__ == "__main__":
	WindowApp().run()
