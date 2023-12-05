# Set up both Root and Class rules in the .kv file.

# Shows another technique for adding a widget tree to an App class.
# 		Return the imported .kv file from the build() method, or


# NOTE: When custom classes are defined in the .py file,
# such statements must appear before the .kv file is loaded.

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class RootObj(GridLayout):
	pass

class MyButton(Button):
	pass

class MyLabel(Label):
	pass

kv_file = Builder.load_file("r07_root_and_class_combo02.kv")


class MainApp(App):
	def build(self):
		return kv_file

if __name__ == "__main__":
	MainApp().run()
