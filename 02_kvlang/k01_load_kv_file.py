# load the .kv file using the Builder module
# and let the build() method drop it into the App.

from kivy.app import App
from kivy.lang import Builder

kv_file = Builder.load_file("k01_load_kv_file.kv")
	

class WindowApp(App):
	def build(self):
		return kv_file


if __name__ == "__main__":
	WindowApp().run()
