from kivy.uix.widget import Widget
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

from web_safe_colours_rgb import WebColours

	
class MyApp(App):
	def build(self):
		## set a background colour for the Window
		Window.clearcolor = WebColours["Coral"]
		Window.clear()
		

if __name__ == "__main__":
	MyApp().run()
