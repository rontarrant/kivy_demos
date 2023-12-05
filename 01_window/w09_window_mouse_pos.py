# Report the position of the mouse within the window.
# Something to note here: the window's x & y coordinates
# originate in the top-left corner, but the mouse's
# position originates from the lower-left corner.
# I'm guessing that means under some circumstances,
# a little translation from one coordinate system to
# the other may be in order.

from kivy.app import App
from kivy.core.window import Window


class WindowApp(App):
	def build(self):
		Window.bind(on_mouse_down = self.report_mouse_pos)
		
	
	def report_mouse_pos(self, window, x, y, button, modifiers):
		print("x: ", x, " y: ", y)
		print("button: ", button)
		print("modifiers: ", modifiers)
		print("mouse position: ", Window.mouse_pos)
		
		return

if __name__ == "__main__":
	WindowApp().run()
