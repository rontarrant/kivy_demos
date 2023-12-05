## s04_slider_get_value.py
## Grab the Slider's value and print to CLI.

from kivy.app import App
from kivy.uix.slider import Slider
from kivy.lang import Builder

Builder.load_file('s04_slider_get_value.kv')

class TestApp(App):
	def build(self):
		return Slider()

if __name__ == "__main__":
	TestApp().run()
