# importing multiple kivy files to build a UI
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget

Builder.load_file("k02_main.kv")
Builder.load_file("k02_dohdoh_label.kv")
Builder.load_file("k02_papa_label.kv")
Builder.load_file("k02_mama_label.kv")


class MainGridLayout(Widget):
	pass
	

class MainApp(App):
	def build(self):
		return MainGridLayout()


if __name__ == "__main__":
	MainApp().run()
