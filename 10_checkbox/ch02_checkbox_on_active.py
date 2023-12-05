# hook something up to the on

from kivy.app import App
from kivy.uix.checkbox import CheckBox
from kivy.lang import Builder

kv = Builder.load_file("ch02_checkbox_on_active.kv")


class TestApp(App):
	def build(self):
		return CheckBox()

if __name__ == "__main__":
	TestApp().run()
