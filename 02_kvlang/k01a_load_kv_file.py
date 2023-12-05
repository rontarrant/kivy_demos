# Import the .kv file with Builder.load_file() and
# put it in the App Window using add_widget().

from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder

kv_file = Builder.load_file("k01_load_kv_file.kv")
	
	
class WindowApp(App):
	def build(self):
		Window.add_widget(kv_file)


if __name__ == "__main__":
	WindowApp().run()
