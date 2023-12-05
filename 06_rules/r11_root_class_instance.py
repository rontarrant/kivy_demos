## r11_root_class_instance.py
## Here, we've moved all class definitions back into the .kv
## file, even the custom classes.

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

kv_file = Builder.load_file("r11_root_class_instance.kv")

class MainApp(App):
	def build(self):
		# Either of the following will work:
		#return kv_file
		Window.add_widget(kv_file)

if __name__ == "__main__":
	MainApp().run()
