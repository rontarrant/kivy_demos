# Drag-n-drop a file onto the window.
# NOTE: binding to on_drop_file triggers an erroneous deprication warning
# which has been reported to the developers. We'll likely have to wait
# until the next Kivy release before this warning disappears.

from kivy.app import App
from kivy.core.window import Window


class WindowApp(App):
	def build(self):
		Window.bind(on_drop_end = self.drop_end)
		
	
	def drop_end(self, window, x, y, *args):
		print("This method fires after a file is dropped onto the window.")
		print("window: ", window)
		print("x: ", x, " y:", y)
		print(f"args: %s" % (args,))
		
		return

if __name__ == "__main__":
	WindowApp().run()
