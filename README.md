<p>This is a very early attempt at a menu module for MicroHydra <a href="https://github.com/echo-lalia/Cardputer-MicroHydra" data-fr-linked="true">https://github.com/echo-lalia/Cardputer-MicroHydra</a></p>
<p>&nbsp;</p>
<ul>
<li><a href="https://github.com/Gabriel-F-Sousa/HydraMenu/tree/main?tab=readme-ov-file#-menu">MENU</a></li>
<li><a href="https://github.com/Gabriel-F-Sousa/HydraMenu/tree/main?tab=readme-ov-file#-bool_item">bool_item</a></li>
<li><a href="https://github.com/Gabriel-F-Sousa/HydraMenu/tree/main?tab=readme-ov-file#-rgb_item">RGB_item</a></li>
<li><a href="https://github.com/Gabriel-F-Sousa/HydraMenu/tree/main?tab=readme-ov-file#-do_item">do_item</a></li>
<li><a href="https://github.com/Gabriel-F-Sousa/HydraMenu/tree/main?tab=readme-ov-file#-int_select_item">int_select_item</a></li>
<li><a href="https://github.com/Gabriel-F-Sousa/HydraMenu/tree/main?tab=readme-ov-file#-write_item">write_item</a></li>
</ul>
<p>&nbsp;</p>
<h2>&bull; MENU</h2>
<p>class Menu (display, font, title: str = None, per_page: int = 3, y_padding: int = 20, ui_color: int = 53243, bg_color: int = 4421, ui_sound: bool = True, volume: int = 2)</p>
<p>&nbsp; &nbsp; Description:</p>
<p style="margin-left: 20px;">&nbsp; &nbsp; The primary menu class.</p>
<p>&nbsp; &nbsp; Parameters:</p>
<ul>
<ul>
<li>&nbsp; &nbsp; &nbsp;display: The display object to be used for rendering.</li>
<li>&nbsp; &nbsp; &nbsp;font: The font object to be used for text rendering.</li>
<li>&nbsp; &nbsp; &nbsp;title (optional): The title of the display. Defaults to None.</li>
<li>&nbsp; &nbsp; &nbsp;per_page (optional): Number of items to display per page. Defaults to 3.</li>
<li>&nbsp; &nbsp; &nbsp;y_padding (optional): Vertical padding between top of the screen and the first item. Defaults to 20.</li>
<li>&nbsp; &nbsp; &nbsp;ui_color (optional): Color code for UI elements. Defaults to 53243.</li>
<li>&nbsp; &nbsp; &nbsp;bg_color (optional): Background color code. Defaults to 4421.</li>
<li>&nbsp; &nbsp; &nbsp;ui_sound (optional): Boolean flag to enable/disable UI sounds. Defaults to True.</li>
<li>&nbsp; &nbsp; &nbsp;volume (optional): Volume level for UI sounds. Defaults to 2.</li>
</ul>
</ul>
<p>&nbsp;</p>
<h2>&bull; bool_item</h2>
<p>class bool_item (menu, text: str = None, BOOL: bool = False, x_pos: int = 0, y_pos: int = 0, selected: bool = False, callback: callable = None)</p>
<p>&nbsp; &nbsp; Description:</p>
<p style="margin-left: 20px;">&nbsp; &nbsp; This class alternates between true and false states.</p>
<p>&nbsp; &nbsp; Parameters:</p>
<ul>
<ul>
<li>&nbsp; &nbsp; &nbsp;menu: The menu object to which the item belongs.</li>
<li>&nbsp; &nbsp; &nbsp;text (optional): The text to be displayed for the menu item. Defaults to None.</li>
<li>&nbsp; &nbsp; &nbsp;BOOL (optional): A boolean value associated with the menu item. Defaults to False.</li>
<li>&nbsp; &nbsp; &nbsp;x_pos (optional): The x-coordinate position of the menu item. Defaults to 0.</li>
<li>&nbsp; &nbsp; &nbsp;y_pos (optional): The y-coordinate position of the menu item. Defaults to 0.</li>
<li>&nbsp; &nbsp; &nbsp;selected (optional): Boolean flag indicating whether the menu item is selected. Defaults to False.</li>
<li>&nbsp; &nbsp; &nbsp;callback (optional): A callable object to be executed when the menu item is activated. Defaults to None.</li>
</ul>
</ul>
<p>&nbsp;</p>
<h2>&bull; RGB_item</h2>
<p>&nbsp;class RGB_item (self, menu, text: str = None, items: list = [], x_pos: int = 0, y_pos: int = 0, selected: bool = False, font = None, callback: callable = None)</p>
<p>&nbsp; &nbsp; Description:</p>
<p style="margin-left: 20px;">&nbsp; &nbsp; This class modifies RGB values.</p>
<p>&nbsp; &nbsp; Parameters:</p>
<ul>
<ul>
<li>&nbsp; &nbsp; &nbsp;menu: The menu object to which the submenu belongs.</li>
<li>&nbsp; &nbsp; &nbsp;text (optional): The text to be displayed for the submenu. Defaults to None.</li>
<li>&nbsp; &nbsp; &nbsp;items (optional): List of the RGB values. Defaults to an empty list.</li>
<li>&nbsp; &nbsp; &nbsp;x_pos (optional): The x-coordinate position of the submenu. Defaults to 0.</li>
<li>&nbsp; &nbsp; &nbsp;y_pos (optional): The y-coordinate position of the submenu. Defaults to 0.</li>
<li>&nbsp; &nbsp; &nbsp;selected (optional): Boolean flag indicating whether the submenu is selected. Defaults to False.</li>
<li>&nbsp; &nbsp; &nbsp;font (optional): The font object to be used for rendering text within the submenu. Defaults to None.</li>
<li>&nbsp; &nbsp; &nbsp;callback (optional): A callable object to be executed when the submenu is activated. Defaults to None.</li>
</ul>
</ul>
<p>&nbsp;</p>
<h2>&bull; do_item</h2>
<p>&nbsp;class do_item (self, menu, text: str = None, x_pos: int = 0, y_pos: int = 0, selected: bool = False, callback: callable = None)</p>
<p>&nbsp; &nbsp; Description:</p>
<p style="margin-left: 20px;">&nbsp; &nbsp; This class triggers a callback function.</p>
<p>&nbsp; &nbsp; Parameters:</p>
<ul>
<ul>
<li>&nbsp; &nbsp; &nbsp;menu: The menu object to which the item belongs.</li>
<li>&nbsp; &nbsp; &nbsp;text (optional): The text to be displayed for the menu item. Defaults to None.</li>
<li>&nbsp; &nbsp; &nbsp;x_pos (optional): The x-coordinate position of the menu item. Defaults to 0.</li>
<li>&nbsp; &nbsp; &nbsp;y_pos (optional): The y-coordinate position of the menu item. Defaults to 0.</li>
<li>&nbsp; &nbsp; &nbsp;selected (optional): Boolean flag indicating whether the menu item is selected. Defaults to False.</li>
<li>&nbsp; &nbsp; &nbsp;callback (optional): A callable object to be executed when the menu item is activated. Defaults to None.</li>
</ul>
</ul>
<p></p>
<h2>&bull; int_select_item</h2>
<p>&nbsp;class int_select_item (self, menu, init_int, min_int, max_int, text: str = None, x_pos: int = 0, y_pos: int = 0, selected: bool = False, callback: callable = None)</p>
<p>&nbsp; &nbsp; Description:</p>
<p style="margin-left: 20px;">&nbsp; &nbsp; This class changes and number.</p>
<p>&nbsp; &nbsp; Parameters:</p>
<ul>
<ul>
<li>&nbsp; &nbsp; &nbsp;menu: The menu object to which the item belongs.</li>
<li>&nbsp; &nbsp; &nbsp;init_int: The initial value.</li>
<li>&nbsp; &nbsp; &nbsp;min_int: The minimum allowed value.</li>
<li>&nbsp; &nbsp; &nbsp;max_int: The maximum allowed value.</li>
<li>&nbsp; &nbsp; &nbsp;text (optional): The text to be displayed for the menu item. Defaults to None.</li>
<li>&nbsp; &nbsp; &nbsp;x_pos (optional): The x-coordinate position of the menu item. Defaults to 0.</li>
<li>&nbsp; &nbsp; &nbsp;y_pos (optional): The y-coordinate position of the menu item. Defaults to 0.</li>
<li>&nbsp; &nbsp; &nbsp;selected (optional): Boolean flag indicating whether the menu item is selected. Defaults to False.</li>
<li>&nbsp; &nbsp; &nbsp;callback (optional): A callable object to be executed when the menu item is activated. Defaults to None.</li>
</ul>
</ul>
<p></p>
<h2>&bull; write_item</h2>
<p>&nbsp;class int_select_item (self, menu, text: str = None, show_text: str = None, hide: bool = False, x_pos: int = 0, y_pos: int = 0, font = None, selected: bool = False, callback: callable = None)</p>
<p>&nbsp; &nbsp; Description:</p>
<p style="margin-left: 20px;">&nbsp; &nbsp; This class allow you to write.</p>
<p>&nbsp; &nbsp; Parameters:</p>
<ul>
<ul>
<li>&nbsp; &nbsp; &nbsp;menu: The menu object to which the item belongs.&nbsp;&nbsp;</li>
<li>&nbsp; &nbsp; &nbsp;text (optional): The text to be displayed for the menu item. Defaults to None.</li>
<li>&nbsp; &nbsp; &nbsp;show_text: The text to display when this item is shown.</li>
<li>&nbsp; &nbsp; &nbsp;hide (bool, optional): A flag indicating whether show_text will be visible if true&nbsp; "****" will be displayed.</li>
<li>&nbsp; &nbsp; &nbsp;x_pos (optional): The x-coordinate position of the menu item. Defaults to 0.</li>
<li>&nbsp; &nbsp; &nbsp;y_pos (optional): The y-coordinate position of the menu item. Defaults to 0.</li>
<li>&nbsp; &nbsp; &nbsp;font: The font object to be used for text rendering.</li>
<li>&nbsp; &nbsp; &nbsp;selected (optional): Boolean flag indicating whether the menu item is selected. Defaults to False.</li>
<li>&nbsp; &nbsp; &nbsp;callback (optional): A callable object to be executed when the menu item is activated. Defaults to None.</li>
</ul>
</ul>
