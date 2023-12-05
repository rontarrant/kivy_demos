# ch01_basic_checkbox.py

from kivy.app import App
from kivy.uix.checkbox import CheckBox
from kivy.lang import Builder

kv = Builder.load_file("ch01_basic_checkbox.kv")


class TestApp(App):
	def build(self):
		return CheckBox()

if __name__ == "__main__":
	TestApp().run()
