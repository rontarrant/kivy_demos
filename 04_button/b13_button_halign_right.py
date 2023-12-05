# Setting the background colour...
# The background_normal property must be set to an empty string
# or else the colour we set with background_color won't be accurate.

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.button import Button

kivy_button_def = Builder.load_file("b13_button_halign_right.kv")

class MyApp(App):
	def build(self):
		return kivy_button_def

if __name__ == "__main__":
	MyApp().run()
