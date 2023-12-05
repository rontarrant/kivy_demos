# root rule using a custom rule name

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label

class MyLabel(Label):
	pass

class R04_Root_Rule_CustomApp(App):
	def build(self):
		label = MyLabel()
		Window.add_widget(label)
		

if __name__ == "__main__":
	R04_Root_Rule_CustomApp().run()
