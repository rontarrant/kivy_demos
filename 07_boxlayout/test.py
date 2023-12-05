from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.lang import Builder

class ShowActionBar(BoxLayout):
	pass

Builder.load_file('test.kv')

class MyTestApp(App):
	def build(self):
		Window.size = (600, 1024)
		return ShowActionBar()

if __name__ == "__main__":
	MyTestApp().run()