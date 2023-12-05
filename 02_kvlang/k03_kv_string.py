from kivy.app import App
from kivy.lang import Builder

kv_file = Builder.load_string("""Label:
	text: "Hello Again, Kivy World!" """)
	
	
class WindowApp(App):
	def build(self):
		return kv_file


if __name__ == "__main__":
	WindowApp().run()
