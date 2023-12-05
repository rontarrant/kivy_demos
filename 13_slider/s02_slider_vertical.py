## s02_slider_vertical.py
## Make the slider vertical instead of the default (horizontal).

from kivy.app import App
from kivy.uix.slider import Slider
from kivy.lang import Builder

Builder.load_file('s02_slider_vertical.kv')

class TestApp(App):
	def build(self):
		return Slider()

if __name__ == "__main__":
	TestApp().run()
