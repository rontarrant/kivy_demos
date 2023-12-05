# Kivy class rule - basic

from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder

Builder.load_file("r01_class_rule_basic.kv")
	

class LaLaLabel(Label):
	pass
	
class KvLangApp(App):
	def build(self):
		return LaLaLabel()


if __name__ == "__main__":
	KvLangApp().run()
