## Conditional command connected to an event.

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.button import Button

kivy_button_def = Builder.load_file("b12_button_conditional_command.kv")

class MyApp(App):
	def build(self):
		return kivy_button_def

if __name__ == "__main__":
	MyApp().run()
