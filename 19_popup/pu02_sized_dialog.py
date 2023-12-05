import kivy
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.widget import Widget

Builder.load_file('pu02_sized_dialog.kv')

class MyLayout(Widget):
	pass

class MyApp(App):
	def build(self):
		return MyLayout()

if __name__ == "__main__":
	MyApp().run()
