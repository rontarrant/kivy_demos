if __name__ == '__main__':
	from textwrap import dedent
	from kivy.app import App
	from kivy.uix.boxlayout import BoxLayout
	from kivy.lang import Builder
	from kivy.properties import NumericProperty

	KV = dedent(r'''
	#:set font_size '20dp'

	BoxLayout:
		orientation: 'vertical'
		padding: '20dp'
		spacing: '10dp'
		TextInput:
			font_size: font_size
			size_hint_y: None
			height: self.minimum_height
			multiline: False
			text: 'monoline'

		TextInput:
			size_hint_y: None
			font_size: font_size
			height: self.minimum_height
			multiline: False
			password: True
			password_mask: '•'
			text: 'password'

		TextInput:
			font_size: font_size
			size_hint_y: None
			height: self.minimum_height
			multiline: False
			readonly: True
			text: 'readonly'

		TextInput:
			font_size: font_size
			size_hint_y: None
			height: self.minimum_height
			multiline: False
			disabled: True
			text: 'disabled'

		TextInput:
			font_size: font_size
			hint_text: 'normal with hint text'

		TextInput:
			font_size: font_size
			text: 'default'

		TextInput:
			font_size: font_size
			text: 'bubble & handles'
			use_bubble: True
			use_handles: True

		TextInput:
			font_size: font_size
			text: 'no wrap'
			do_wrap: False

		TextInput:
			font_size: font_size
			text: 'multiline\nreadonly'
			disabled: app.time % 5 < 2.5
	''')

class TextInputApp(App):
	time = NumericProperty()

	def build(self):
		Clock.schedule_interval(self.update_time, 0)
		return Builder.load_string(KV)

	def update_time(self, dt):
		self.time += dt

TextInputApp().run()
