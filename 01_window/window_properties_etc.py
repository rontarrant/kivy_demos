Window Properties
	keycodes = {
        # specials keys
        'backspace': 8, 'tab': 9, 'enter': 13, 'rshift': 303, 'shift': 304,
        'alt': 308, 'rctrl': 306, 'lctrl': 305,
        'super': 309, 'alt-gr': 307, 'compose': 311, 'pipe': 310,
        'capslock': 301, 'escape': 27, 'spacebar': 32, 'pageup': 280,
        'pagedown': 281, 'end': 279, 'home': 278, 'left': 276, 'up':
        273, 'right': 275, 'down': 274, 'insert': 277, 'delete': 127,
        'numlock': 300, 'print': 144, 'screenlock': 145, 'pause': 19,

        # a-z keys
        'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103,
        'h': 104, 'i': 105, 'j': 106, 'k': 107, 'l': 108, 'm': 109, 'n': 110,
        'o': 111, 'p': 112, 'q': 113, 'r': 114, 's': 115, 't': 116, 'u': 117,
        'v': 118, 'w': 119, 'x': 120, 'y': 121, 'z': 122,

        # 0-9 keys
        '0': 48, '1': 49, '2': 50, '3': 51, '4': 52,
        '5': 53, '6': 54, '7': 55, '8': 56, '9': 57,

        # numpad
        'numpad0': 256, 'numpad1': 257, 'numpad2': 258, 'numpad3': 259,
        'numpad4': 260, 'numpad5': 261, 'numpad6': 262, 'numpad7': 263,
        'numpad8': 264, 'numpad9': 265, 'numpaddecimal': 266,
        'numpaddivide': 267, 'numpadmul': 268, 'numpadsubstract': 269,
        'numpadadd': 270, 'numpadenter': 271,

        # F1-15
        'f1': 282, 'f2': 283, 'f3': 284, 'f4': 285, 'f5': 286, 'f6': 287,
        'f7': 288, 'f8': 289, 'f9': 290, 'f10': 291, 'f11': 292, 'f12': 293,
        'f13': 294, 'f14': 295, 'f15': 296,

        # other keys
        '(': 40, ')': 41,
        '[': 91, ']': 93,
        '{': 123, '}': 125,
        ':': 58, ';': 59,
        '=': 61, '+': 43,
        '-': 45, '_': 95,
        '/': 47, '*': 42,
        '?': 47,
        '`': 96, '~': 126,
        '´': 180, '¦': 166,
        '\\': 92, '|': 124,
        '"': 34, "'": 39,
        ',': 44, '.': 46,
        '<': 60, '>': 62,
        '@': 64, '!': 33,
        '#': 35, '$': 36,
        '%': 37, '^': 94,
        '&': 38, '¬': 172,
        '¨': 168, '…': 8230,
        'ù': 249, 'à': 224,
        'é': 233, 'è': 232,
    }

	allow_screensaver = BooleanProperty(True)
	borderless = BooleanProperty(False)
	borderless: str, one of ('0', '1')
	canvas = ObjectProperty(None)
	center = AliasProperty(_get_center, bind = ('width', 'height'))
	children = ListProperty([])
	clearcolor = ColorProperty((0, 0, 0, 1))
	custom_titlebar = BooleanProperty(False)
	custom_titlebar: str, one of ('0', '1')
	dpi = NumericProperty(96.)
	event_managers = None
	event_managers_dict = None
	fullscreen = OptionProperty(False/True/'auto'/'fake')
	gl_backends_allowed = []
	gl_backends_ignored = []
	height = AliasProperty(_get_height, bind = ('_rotation', '_size', '_density'))
	height = NumericProperty(800)
	icon = StringProperty()
	keyboard_anim_args = {'t': 'in_out_quart', 'd': .5}
	keyboard_padding = NumericProperty(0)
	left = AliasProperty(_get_left, _set_left)
	managed_textinput = False
	minimum_height = NumericProperty(0)
	minimum_width = NumericProperty(0)
	mouse_pos = ObjectProperty((0, 0))
	parent = ObjectProperty(None, allownone = True)
	position = OptionProperty('auto', options=['auto', 'custom'])
	render_context = ObjectProperty(None)
	rotation = AliasProperty(_get_rotation, _set_rotation, bind = ('_rotation', ))
	shape_color_key = ColorProperty([1, 1, 1, 1])
	shape_cutoff = BooleanProperty(True)
	shape_image = StringProperty('')
	shape_mode = AliasProperty(_get_shape_mode, _set_shape_mode)
	shaped = AliasProperty(_get_shaped, None)
	show_cursor = BooleanProperty(True)
	size = AliasProperty(_get_size, _set_size, bind=('_size', '_rotation'))
	softinput_mode = OptionProperty('below_target'/'pan'/'scale'/'resize')
	title = StringProperty('Kivy')
	top = AliasProperty(_get_top, _set_top)
	trigger_create_window = None
	width = AliasProperty(_get_width, bind = ('_rotation', '_size', '_density'))
	width: int

	
Window Events
	on_close
	on_cursor_enter
	on_cursor_leave
	on_draw
	on_drop_begin`: x, y, *args
	on_drop_end`: x, y, *args
	on_drop_file`: filename (bytes), x, y, *args
	on_drop_text`: text (bytes), x, y, *args
	on_dropfile
	on_flip
	on_hide
	on_joy_axis
	on_joy_ball
	on_joy_button_down
	on_joy_button_up
	on_joy_hat
	on_key_down`: key, scancode, codepoint, modifier
	on_key_up`: key, scancode, codepoint
	on_keyboard`: key, scancode, codepoint, modifier
	on_maximize
	on_memorywarning
	on_minimize:
	on_motion: etype, motionevent
	on_mouse_down
	on_mouse_move
	on_mouse_up
	on_move
	on_pre_resize
	on_request_close
	on_resize
	on_restore
	on_rotate: rotation
	on_show
	on_textedit(self, text)`:
	on_textinput
	on_touch_down:
	on_touch_move:
	on_touch_up:

	
Window Methods
	set_system_cursor(self, cursor_name):

        +------------+-----------+------------+-----------+---------------+
        |            | Windows   | MacOS      | Linux X11 | Linux Wayland |
        +============+===========+============+===========+===============+
        | arrow      | arrow     | arrow      | arrow     | arrow         |
        +------------+-----------+------------+-----------+---------------+
        | ibeam      | ibeam     | ibeam      | ibeam     | ibeam         |
        +------------+-----------+------------+-----------+---------------+
        | wait       | wait      | arrow      | wait      | wait          |
        +------------+-----------+------------+-----------+---------------+
        | crosshair  | crosshair | crosshair  | crosshair | hand          |
        +------------+-----------+------------+-----------+---------------+
        | wait_arrow | arrow     | arrow      | wait      | wait          |
        +------------+-----------+------------+-----------+---------------+
        | size_nwse  | size_nwse | size_all   | size_all  | hand          |
        +------------+-----------+------------+-----------+---------------+
        | size_nesw  | size_nesw | size_all   | size_all  | hand          |
        +------------+-----------+------------+-----------+---------------+
        | size_we    | size_we   | size_we    | size_we   | hand          |
        +------------+-----------+------------+-----------+---------------+
        | size_ns    | size_ns   | size_ns    | size_ns   | hand          |
        +------------+-----------+------------+-----------+---------------+
        | size_all   | size_all  | size_all   | size_all  | hand          |
        +------------+-----------+------------+-----------+---------------+
        | no         | no        | no         | no        | ibeam         |
        +------------+-----------+------------+-----------+---------------+
        | hand       | hand      | hand       | hand      | hand          |
        +------------+-----------+------------+-----------+---------------+
	
	clear(self):
	configure_keyboards(self):
	get_parent_layout(self):
	get_parent_window(self):
	get_root_window(self):
	get_window_matrix(self, x = 0, y = 0):
	grab_mouse(self):
	on_close(self, *largs):
	on_cursor_enter(self, *largs):
	on_cursor_leave(self, *largs):
	on_draw(self):
	on_drop_begin(self, x, y, *args):
	on_hide(self, *largs):
	on_joy_axis(self, stickid, axisid, value):
	on_joy_ball(self, stickid, ballid, xvalue, yvalue):
	on_joy_button_down(self, stickid, buttonid):
	on_joy_button_up(self, stickid, buttonid):
	on_joy_hat(self, stickid, hatid, value):
	on_key_down(self, key, scancode = None, codepoint = None,
	on_key_up(self, key, scancode = None, codepoint = None,
	on_keyboard(self, key, scancode = None, codepoint = None,
	on_maximize(self, *largs):
	on_minimize(self, *largs):
	on_motion(self, etype, me):
	on_mouse_down(self, x, y, button, modifiers):
	on_mouse_move(self, x, y, modifiers):
	on_mouse_up(self, x, y, button, modifiers):
	on_move(self):
	on_pre_resize(self, width, height):
	on_request_close(self, *largs, **kwargs):
	on_resize(self, width, height):
	on_restore(self, *largs):
	on_rotate(self, rotation):
	on_show(self, *largs):
	on_textinput(self, text):
	on_touch_down(self, touch):
	on_touch_move(self, touch):
	on_touch_up(self, touch):
	release_all_keyboards(self):
	release_keyboard(self, target = None):
	remove_widget(self, widget):
	request_keyboard(self, callback, target, input_type = 'text', keyboard_suggestions = True):
	screenshot(self, name = 'screenshot{:04d}.png'):
	set_icon(self, filename):
	set_title(self, title):
	set_vkeyboard_class(self, cls):
	to_normalized_pos(self, x, y):
	to_widget(self, x, y, initial = True, relative = False):
	to_window(self, x, y, initial = True, relative = False):
	transform_motion_event_2d(self, me, widget = None):
	update_childsize(self, childs = None):
	update_viewport(self):

