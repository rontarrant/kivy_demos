from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout

class MyBoxLayout(BoxLayout):
	pass


kv = Builder.load_file("gl01_gridlayout_size.kv")

class MyApp(App):

	def build(self):
		Window.size = 800, 800
		return MyBoxLayout()

if __name__ == "__main__":
	MyApp().run()
