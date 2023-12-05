TextInput Properties
	readonly = BooleanProperty(False)
	text_validate_unfocus = BooleanProperty(True)
	multiline = BooleanProperty(True)
	do_wrap = BooleanProperty(True)
	password = BooleanProperty(False)
	password_mask = StringProperty('*')
	cursor_blink = BooleanProperty(True)
   cursor_row = AliasProperty(_get_cursor_row, None, bind=('cursor', ))
   cursor_pos = AliasProperty(_get_cursor_pos, None,
										bind = ('cursor', 'padding', 'pos',
                              'size', 'focus', 'scroll_x', 'scroll_y',
										'line_height', 'line_spacing'),
									cache = False)
	cursor_color = ColorProperty([1, 0, 0, 1])
	cursor_width = NumericProperty('1sp')
	line_height = NumericProperty(1)
	tab_width = NumericProperty(4)
	padding_x = VariableListProperty([0, 0], length = 2, deprecated = True)
	padding_y = VariableListProperty([0, 0], length = 2, deprecated = True)
	padding = VariableListProperty([6, 6, 6, 6])
	halign = OptionProperty('auto', options = ['left', 'center', 'right','auto'])
	scroll_x = NumericProperty(0)
	scroll_y = NumericProperty(0)
	selection_color = ColorProperty([0.1843, 0.6549, 0.8313, .5])
	border = ListProperty([4, 4, 4, 4])
	background_normal = StringProperty('textinput.image')
	background_disabled_normal = StringProperty('textinput_disabled')
	background_active = StringProperty('extinput_active')
	background_color = ColorProperty([1, 1, 1, 1])
	foreground_color = ColorProperty([0, 0, 0, 1])
	disabled_foreground_color = ColorProperty([0, 0, 0, .5])
	use_bubble = BooleanProperty(not _is_desktop)use_handles = BooleanProperty(not _is_desktop)
	scroll_from_swipe = BooleanProperty(not _is_desktop)
	scroll_distance = NumericProperty(_scroll_distance)
	scroll_timeout = NumericProperty(_scroll_timeout)
	font_name = StringProperty(DEFAULT_FONT)
	font_size = NumericProperty('15sp')
	font_context = StringProperty(None, allownone = True)
	font_family = StringProperty(None, allownone = True)
	base_direction = OptionProperty( None/'ltr'/'rtl'/'weak_rtl'/'weak_ltr')
	text_language = StringProperty(None, allownone = True)
   hint_text_color = ColorProperty([0.5, 0.5, 0.5, 1.0])
	auto_indent = BooleanProperty(False)
	replace_crlf = BooleanProperty(True)
	allow_copy = BooleanProperty(True)
	line_spacing = NumericProperty(0)
	input_filter = ObjectProperty(None, allownone = True)
	handle_image_middle = StringProperty('selector_middle')


TextInput Events
	on_text_validate
	on_double_tap
	on_triple_tap
	on_quad_touch
	
TextInput Methods
	on_text_validate(self):
	cursor_index(self, cursor = None):
	cursor_offset(self):
	get_cursor_from_index(self, index):
	select_text(self, start, end):
	select_all(self):
	insert_text(self, substring, from_undo = False):
	reset_undo(self):
	do_redo(self):
	do_undo(self):
	do_backspace(self, from_undo = False, mode='bkspc'):
	pgmove_speed(self):
	get_cursor_from_xy(self, x, y):
	cancel_selection(self):
	delete_selection(self, from_undo = False):
	long_touch(self, dt):
	cancel_long_touch_event(self):
	on_double_tap(self):
	on_triple_tap(self):
	on_quad_touch(self):
	on_touch_down(self, touch):
	on_touch_move(self, touch):
	on_touch_up(self, touch):
	scroll_text_from_swipe(self, touch):
	cut(self):
	copy(self, data=''):
	paste(self):
	on_cursor_blink(self, instance, value):
	on_cursor(self, instance, value):
	on_size(self, instance, value):
	keyboard_on_key_down(self, window, keycode, text, modifiers):
	keyboard_on_key_up(self, window, keycode):
	keyboard_on_textinput(self, window, text):
	window_on_textedit(self, window, ime_input):
	on__hint_text(self, instance, value):
	on_padding_x(self, instance, value):
	on_padding_y(self, instance, value):
	get_sel_from(self):
	get_sel_to(self):
	on_selection_text(self, instance, value):
	on_handle_image_middle(self, instance, value):
	on_handle_image_left(self, instance, value):
	on_handle_image_right(self, instance, value):
