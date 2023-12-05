from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

Builder.load_file("sc01_ref_in_kivy.kv")

Window.clearcolor = (0, 0.6, 0.1, 1.0)
Window.size = (400, 600)


class HomeScreen(Screen):
	pass


class OtherScreen(Screen):
	pass


class RootWidget(ScreenManager):
	pass


class MainApp(App):

	def build(self):
		self.title = "My Gardens App"

		return RootWidget()

if __name__ == "__main__":
	MainApp().run()


