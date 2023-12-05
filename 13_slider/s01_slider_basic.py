## s01_slider_basic.py
from kivy.app import App
from kivy.uix.slider import Slider
from kivy.lang import Builder

Builder.load_file('s01_slider_basic.kv')

class TestApp(App):
	def build(self):
		return Slider()

if __name__ == "__main__":
	TestApp().run()
