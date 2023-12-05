# Set up both Root and Class rules in the .kv file.

# Shows another technique for adding a widget tree to an App class.
# 		add the widget tree to the Window object.

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

kv_file = Builder.load_file("r08_root_and_class_combo03.kv")


class MainApp(App):
	def build(self):
		Window.add_widget(kv_file)

if __name__ == "__main__":
	MainApp().run()
