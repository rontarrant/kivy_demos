# Bind the mouse down event to a callback
# method which prints mouse information
# at the time the mouse button was clicked.
# When that's done, the window closes.
# NOTE: binding a callback to on_close() produces an error.
# NOTE 2: Adding a call to self.stop() just changes the error to a warning
# of a different kind.

from kivy.app import App
from kivy.core.window import Window


class WindowApp(App):
	def build(self):
		Window.bind(on_mouse_down = self.mouse_down)
		Window.bind(on_close = self.close_window)
		
	def mouse_down(self, window, x, y, button, modifiers):
		print("window: ", window)
		print("x: ", x, " y: ", y)
		print("button: ", button)
		print("modifiers: ", modifiers)

		Window.close()
		
		return
		
	def close_window(self, *args):
		self.stop()
		print("Good-bye")


if __name__ == "__main__":
	WindowApp().run()
