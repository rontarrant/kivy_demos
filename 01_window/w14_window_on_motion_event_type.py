# Doing something else with on_flip...
# Events are reported as the mouse pointer is moved across the window
# or when any mouse button is clicked.
# For some reason I don't yet understand, clicking either the middle
# or right mouse button leaves a red dot on the window.
# Event types:
#	begin (mouse click)
#	end (mouse click)
#	update (mouse motion)

from kivy.app import App
from kivy.core.window import Window


class WindowApp(App):
	def build(self):
		Window.bind(on_motion = self.increment_color)

	
	def increment_color(self, window, event_type, motion_event):
		print("event_type: ", event_type, ", motion_event: ", motion_event)
		
		if event_type == "end":
				print("mouse button released")
		elif event_type == "begin":
				print("mouse button pressed")
		elif event_type == "update":
				print("mouse pointer moved")
		
		return

if __name__ == "__main__":
	WindowApp().run()
