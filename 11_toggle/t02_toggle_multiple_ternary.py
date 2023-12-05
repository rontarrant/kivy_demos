## t01_toggle_basic.py

from kivy.app import App
from kivy.uix.togglebutton import ToggleButton
from kivy.lang import Builder

Builder.load_file("t02_toggle_multiple_ternary.kv")

class TestApp(App):
	def build(self):
		return ToggleButton()

if __name__ == "__main__":
	TestApp().run()
