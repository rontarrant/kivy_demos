import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.graphics import Color, RoundedRectangle

kivy.require('2.0.0')


class RoundedButton(Button):

    def __init__(self, **kwargs):
        super(RoundedButton, self).__init__(**kwargs)
        self.background_color = (0, 0, 0, 0)  # Invisible background color to regular button
        self.background_normal = ''

        with self.canvas.before:
            self.shape_color = Color(rgba=(0.5, .5, .5, .5))
            self.shape = RoundedRectangle(pos=self.pos, size=self.size, radius=[15])
            self.bind(pos=self.update_shape, size=self.update_shape)

        self.text = 'test'
        self.size_hint = (0.05, 0.05)
        self.pos_hint = {"center_x": 0.5, "center_y": 0.5}

    def update_shape(self, *args):
        self.shape.pos = self.pos
        self.shape.size = self.size

    def on_press(self, *args):
        self.shape_color.rgba = (0, 0, 1, 1)
        print('pressed')

    def on_release(self, *arg):
        self.shape_color.rgba = (0.5, .5, .5, .5)


class MainApp(App):
    def build(self):
        return RoundedButton()


if __name__ == "__main__":
    MainApp().run()
