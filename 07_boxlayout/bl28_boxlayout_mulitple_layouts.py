from kivy.uix.widget import Widget
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout

from webcolours import WebColours

kv1 = Builder.load_file("bl02_boxlayout_sized_lower_left.kv")
kv2 = Builder.load_file("bl03_boxlayout_sized_center_left.kv")
kv3 = Builder.load_file("bl04_boxlayout_sized_upper_left.kv")
kv4 = Builder.load_file("bl05_boxlayout_sized_upper_middle.kv")
kv5 = Builder.load_file("bl06_boxlayout_sized_upper_right.kv")
kv6 = Builder.load_file("bl07_boxlayout_sized_center_right.kv")
kv7 = Builder.load_file("bl08_boxlayout_sized_lower_right.kv")
kv8 = Builder.load_file("bl09_boxlayout_sized_lower_middle.kv")
kv9 = Builder.load_file("bl10_boxlayout_sized_center_middle.kv")


class MyBoxLayout(BoxLayout):
	def release(self):
		label = self.ids.my_label
		button = self.ids.my_button
		
		if label.text == "Here's a label":
			label.text = "Another Label"
		else:
			label.text = "Here's a label"

class LLBoxLayout(MyBoxLayout):
	pass
	
class CLBoxLayout(MyBoxLayout):
	pass
	
class ULBoxLayout(MyBoxLayout):
	pass
	
class UMBoxLayout(MyBoxLayout):
	pass
	
class URBoxLayout(MyBoxLayout):
	pass
	
class CRBoxLayout(MyBoxLayout):
	pass
	
class LRBoxLayout(MyBoxLayout):
	pass
	
class LMBoxLayout(MyBoxLayout):
	pass
	
class CMBoxLayout(MyBoxLayout):
	pass
	

	
class MyApp(App):
	def build(self):
		## set a background colour for the Window
		Window.clearcolor = WebColours["Coral"]
		Window.clear()
		
		## populate the window with BoxLayouts
		llboxlayout = LLBoxLayout()
		Window.add_widget(llboxlayout)
		clboxlayout = CLBoxLayout()
		Window.add_widget(clboxlayout)
		ulboxlayout = ULBoxLayout()
		Window.add_widget(ulboxlayout)
		umboxlayout = UMBoxLayout()
		Window.add_widget(umboxlayout)
		urboxlayout = URBoxLayout()
		Window.add_widget(urboxlayout)
		crboxlayout = CRBoxLayout()
		Window.add_widget(crboxlayout)
		lrboxlayout = LRBoxLayout()
		Window.add_widget(lrboxlayout)
		lmboxlayout = LMBoxLayout()
		Window.add_widget(lmboxlayout)
		cmboxlayout = CMBoxLayout()
		Window.add_widget(cmboxlayout)

if __name__ == "__main__":
	MyApp().run()
