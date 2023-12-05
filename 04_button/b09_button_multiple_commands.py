# Connecting multiple commands to a single event.

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.button import Button

kivy_button_def = Builder.load_file("b09_button_multiple_commands.kv")

class MyApp(App):
	def build(self):
		return kivy_button_def

if __name__ == "__main__":
	MyApp().run()
