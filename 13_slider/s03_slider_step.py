## s03_slider_step.py
## Incremental steps along a slider.

from kivy.app import App
from kivy.uix.slider import Slider
from kivy.lang import Builder

Builder.load_file('s03_slider_step.kv')

class TestApp(App):
	def build(self):
		return Slider()

if __name__ == "__main__":
	TestApp().run()
