from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout

class AddLocationForm(BoxLayout):
	pass

kv = Builder.load_file("bl21_control_child_height.kv")

## Note:
## If you don't want to bother setting a window title,
## Kivy subs in the name of the app, everything up
## to—but not including—the "App" part.
 
class WeatherApp(App):
	def build(self):
		return AddLocationForm()

if __name__ == "__main__":
	WeatherApp().run()
