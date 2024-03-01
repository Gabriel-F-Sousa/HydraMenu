import math
from lib import beeper
from lib import microhydra as mh

class Menu:
    def __init__(self, display, font, title: str = None, per_page: int = 3, y_padding: int = 20, ui_color: int = 53243, bg_color: int = 4421, ui_sound: bool = True, volume: int = 2):
        from lib import microhydra as mh
        self.display = display
        self.items = []
        self.cursor_index = 0
        self.prev_cursor_index = 0
        self.setting_screen_index = 0
        self.font = font
        self.per_page = per_page
        self.y_padding = y_padding
        self.ui_color = ui_color
        self.bg_color = bg_color
        self.mid_color = mh.mix_color565(ui_color, bg_color)
        self.ui_sound = ui_sound
        self.volume = volume
        self.in_submenu = False
        if ui_sound:
            self.beep = beeper.Beeper()

    def add_item(self, item):
        self.items.append(item)

    def display_menu(self):
        if self.cursor_index >= self.setting_screen_index + self.per_page:
            self.setting_screen_index += self.cursor_index - (self.setting_screen_index + (self.per_page - 1))

        elif self.cursor_index < self.setting_screen_index:
            self.setting_screen_index -= self.setting_screen_index - self.cursor_index
        
        self.display.fill(self.bg_color)
        visible_items = self.items[self.setting_screen_index:self.setting_screen_index+self.per_page]
        for i in range(self.setting_screen_index, self.setting_screen_index + self.per_page):
            y = self.y_padding + (i - self.setting_screen_index) * self.font.HEIGHT
            if i <= len(self.items) - 1:
                if i == self.cursor_index:
                    self.items[i].selected = 1
                    self.items[i].y_pos = y
                    self.items[i].draw()
                else:
                    self.items[i].selected = 0
                    self.items[i].y_pos = y
                    self.items[i].draw()
            self.display.hline(0, y, self.display.width, self.mid_color)# separation lines
        self.display.hline(0, y + self.font.HEIGHT, self.display.width, self.mid_color)# separation lines

    def update_scroll_bar(self):
        max_screen_index = len(self.items)
        scrollbar_height = 135 // max_screen_index
        scrollbar_position = math.floor((135 - scrollbar_height) * (self.cursor_index / max_screen_index))   
        self.display.fill_rect(238, 0, 2, 135, self.bg_color)
        self.display.fill_rect(238, scrollbar_position, 2, scrollbar_height, self.mid_color)

    def handle_input(self, key):
        if self.in_submenu:
            self.items[self.cursor_index].handle_input(key)
        
        elif key == 'up':
            self.cursor_index -= 1
            if self.ui_sound:
                self.beep.play(("E3","C3"), 100, self.volume)
            if self.cursor_index < 0:
                self.cursor_index = len(self.items) - 1
            self.display_menu()

        elif key == 'down':
            self.cursor_index += 1
            if self.ui_sound:
                self.beep.play(("D3","C3"), 100, self.volume)
            if self.cursor_index >= len(self.items):
                self.cursor_index = 0
            self.display_menu()
        
        elif key == 'press':
            return (self.items[self.cursor_index].handle_input("press"))

class bool_item:
    def __init__(self, menu, text: str = None, BOOL: bool = False, x_pos: int = 0, y_pos: int = 0, selected: bool = False, callback: callable = None):
        self.BOOL = BOOL
        self.menu = menu
        self.selected = selected
        self.text = text
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.callback = callback        
    
    def draw(self):
        if self.selected:
            self.menu.display.text(self.menu.font, '>', 5, self.y_pos, self.menu.ui_color, self.menu.mid_color)
            self.menu.display.text(self.menu.font, self.text, 20, self.y_pos, self.menu.ui_color, self.menu.mid_color)
        else:
            self.menu.display.text(self.menu.font, ' ', 5, self.y_pos, self.menu.ui_color, self.menu.bg_color)
            self.menu.display.text(self.menu.font, self.text, 20, self.y_pos, self.menu.ui_color, self.menu.bg_color)
            
        self.menu.display.fill_rect(int(self.menu.display.width / 2) + 20, self.y_pos, 100, self.menu.font.HEIGHT, self.menu.bg_color)# clear word
        self.menu.display.text(self.menu.font, str(self.BOOL), int(self.menu.display.width / 2) + 20, self.y_pos, self.menu.ui_color, self.menu.bg_color)
        self.menu.display.hline(0, self.y_pos, self.menu.display.width, self.menu.mid_color)

    def handle_input(self, key):
        if key == "press":
            self.BOOL = not self.BOOL
            self.menu.beep.play((("C3","E3","D3"),"D4","C4"), 100, self.menu.volume)
            self.draw()
            if self.callback != None:
                self.callback(self, self.BOOL)

class RGB_item:
    def __init__(self, menu, text: str = None, items: list = [], x_pos: int = 0, y_pos: int = 0, selected: bool = False, font = None, callback: callable = None):
        self.cursor_index = 0
        self.menu = menu
        self.text = text
        self.items = items
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.selected = selected
        self.rgb_select_index = 0
        self.in_item = False
        self.callback = callback
        if font:
            self.font = font
        else:
            self.font = self.menu.font
        pass

    def draw(self):
        if self.selected:
            self.menu.display.text(self.menu.font, '>', 5, self.y_pos, self.menu.ui_color, self.menu.mid_color)
            self.menu.display.text(self.menu.font, self.text, 20, self.y_pos, self.menu.ui_color, self.menu.mid_color)
        else:
            self.menu.display.text(self.menu.font, ' ', 5, self.y_pos, self.menu.ui_color, self.menu.bg_color)
            self.menu.display.text(self.menu.font, self.text, 20, self.y_pos, self.menu.ui_color, self.menu.bg_color)
        
        self.menu.display.fill_rect(int(self.menu.display.width / 2) + 20, self.y_pos, 100, self.menu.font.HEIGHT, self.menu.bg_color)# clear word
        titel = "{},{},{}".format(self.items[0], self.items[1], self.items[2])
        self.menu.display.text(self.font, str(titel), int(self.menu.display.width / 2) + 25 , self.y_pos + int(self.menu.font.HEIGHT / 4), self.menu.ui_color, self.menu.bg_color)
        
        self.menu.display.hline(0, self.y_pos, self.menu.display.width, self.menu.mid_color)
    
    def draw_rgb_win(self):
        win = pop_up_win(self.menu.display, self.text, self.menu.ui_color, self.menu.bg_color, self.font)
        win.draw()
        color = [63488, 2016, 31]
        rgb_text = ["R/31", "G/63", "B/31"]
        for i, item in enumerate(self.items):
            x = int(222/2 * (i * 0.5)) + int(222 / 5)
            y = int(20 + self.font.HEIGHT + 5)
            if i == self.cursor_index:
                self.menu.display.text(self.menu.font, str(item), x, y + self.font.HEIGHT, 16777215, 0)
            else:
                self.menu.display.text(self.menu.font, str(item), x, y + self.font.HEIGHT, 16777215, self.menu.bg_color)
            self.menu.display.text(self.font, str(rgb_text[i]), x, y, color[i], self.menu.bg_color)
        
        # draw pointer
        for i in range(0,16):
            self.menu.display.hline(
                x = (78 - i) + (44 * self.cursor_index),
                y = 94 + i,
                length = 2 + (i*2),
                color = mh.combine_color565(self.items[0],self.items[1],self.items[2]))
            self.menu.display.fill_rect(62 + (44 * self. cursor_index), 110, 34, 8, mh.combine_color565(self.items[0],self.items[1],self.items[2]))
        
        
    
    def handle_input(self, key):
        max_range = [31, 63, 31]
        self.menu.in_submenu = True
        if key == 'right':
            self.cursor_index += 1
            if self.menu.ui_sound:
                self.menu.beep.play(("D3","C3"), 100, self.menu.volume)
            if self.cursor_index >= len(self.items):
                self.cursor_index = 0
                
        elif key == "left":
            self.cursor_index -= 1
            if self.menu.ui_sound:
                self.menu.beep.play(("E3","C3"), 100, self.menu.volume)
            if self.cursor_index < 0:
                self.cursor_index = len(self.items) - 1
                
        elif key == "up":
            self.items[self.cursor_index] += 1
            if self.menu.ui_sound:
                self.menu.beep.play(("C3","A3"), 80, self.menu.volume)
            if self.items[self.cursor_index] > max_range[self.cursor_index]:
                self.items[self.cursor_index] = 0
                
        elif key == "down":
            self.items[self.cursor_index] -= 1
            if self.menu.ui_sound:
                self.menu.beep.play(("C3","A3"), 80, self.menu.volume)
            if self.items[self.cursor_index] < 0:
                self.items[self.cursor_index] = max_range[self.cursor_index]
                
        elif key == "press" and self.in_item != False:
            self.menu.in_submenu = False
            self.in_item = False
            self.menu.display_menu()
            if self.callback != None:
                self.callback(self, self.items)
                self.menu.beep.play(("C4","D4","E4"), 50, self.menu.volume)
            return
            
        self.in_item = True
        self.draw_rgb_win()

class do_item:
    def __init__(self, menu, text: str = None, x_pos: int = 0, y_pos: int = 0, selected: bool = False, callback: callable = None):
        self.menu = menu
        self.selected = selected
        self.text = text
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.callback = callback

    def draw(self):
        if self.selected:
            TEXT = "< {} >".format(self.text)
            self.menu.display.text(self.menu.font, TEXT, int(self.menu.display.width / 2) - get_text_center(TEXT, self.menu.font), self.y_pos, self.menu.ui_color, self.menu.mid_color)
        else:
            self.menu.display.text(self.menu.font, self.text, int(self.menu.display.width / 2) - get_text_center(self.text, self.menu.font), self.y_pos, self.menu.ui_color, self.menu.bg_color)
        
    def handle_input(self, key):
        if self.callback != None:
            self.callback(self)
            self.menu.beep.play(("C4","D4","E4"), 50, self.menu.volume)

class int_select_item:
    def __init__(self, menu, init_int, min_int, max_int, text: str = None, x_pos: int = 0, y_pos: int = 0, selected: bool = False, callback: callable = None):
        self.menu = menu
        self.selected = selected
        self.current_value = init_int
        self.min_int = min_int
        self.max_int = max_int
        self.text = text
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.in_item = False
        self.callback = callback
    
    def draw(self):
        if self.selected:
            self.menu.display.text(self.menu.font, '>', 5, self.y_pos, self.menu.ui_color, self.menu.mid_color)
            self.menu.display.text(self.menu.font, self.text, 20, self.y_pos, self.menu.ui_color, self.menu.mid_color)
        else:
            self.menu.display.text(self.menu.font, ' ', 5, self.y_pos, self.menu.ui_color, self.menu.bg_color)
            self.menu.display.text(self.menu.font, self.text, 20, self.y_pos, self.menu.ui_color, self.menu.bg_color)
        self.menu.display.text(self.menu.font, str(self.current_value), int(self.menu.display.width / 2) + 20, self.y_pos, self.menu.ui_color, self.menu.bg_color)
    
    def draw_win(self):
        win = pop_up_win(self.menu.display, self.text, self.menu.ui_color, self.menu.bg_color, self.menu.font)
        win.draw()
        for i in range(0,8):
            self.menu.display.hline(
                x = (119 - i),
                y = 60 + i,
                length = 2 + (i*2),
                color = self.menu.ui_color)
            self.menu.display.hline(
                x = (119 - i),
                y = 116 - i,
                length = 2 + (i*2),
                color = self.menu.ui_color)
        x = 112 - ((self.current_value == 10) * 8)
        if self.current_value < 0:
            x = 112 - ((self.current_value == 10) * 8) - self.menu.font.WIDTH
        self.menu.display.text(self.menu.font, str(self.current_value), x, 75, self.menu.ui_color, self.menu.bg_color)
    
    def handle_input(self, key):
        self.menu.in_submenu = True
        if key == "up":
            self.current_value += 1
            if self.menu.ui_sound:
                self.menu.beep.play(("C3","A3"), 80, self.menu.volume)
            if self.current_value > self.max_int:
                self.current_value = self.min_int
                
        elif key == "down":
            self.current_value -= 1
            if self.menu.ui_sound:
                self.menu.beep.play(("C3","A3"), 80, self.menu.volume)
            if self.current_value < self.min_int:
                self.current_value = self.max_int
                
        elif key == "press" and self.in_item != False:
            self.menu.in_submenu = False
            self.in_item = False
            self.menu.display_menu()
            if self.callback != None:
                self.callback(self, self.current_value)
                self.menu.beep.play(("C4","D4","E4"), 50, self.menu.volume)
            return
            
        self.in_item = True
        self.draw_win()
        pass

class pop_up_win:
    def __init__(self, display, text: str = None, ui_color: int = 53243, bg_color: int = 4421, font = None):
        self.display = display
        self.text = text
        self.ui_color = ui_color
        self.bg_color = bg_color
        self.font = font
        pass
    
    def draw(self):
        self.display.fill_rect(10, 10, 220, 115, self.bg_color)
        self.display.rect(9, 9, 222, 117, self.ui_color)
        self.display.hline(10, 126, 222, 0)
        self.display.hline(11, 127, 222, 0)
        self.display.hline(12, 128, 222, 0)
        self.display.hline(13, 129, 222, 0)
        self.display.vline(231, 10, 117, 0)
        self.display.vline(232, 11, 117, 0)
        self.display.vline(233, 12, 117, 0)
        self.display.vline(234, 13, 117, 0)
        if self.text and self.font:
            center_x = int(222/2) - get_text_center(self.text, self.font)
            self.display.text(self.font, str(self.text + ":"), center_x, 20, self.ui_color, self.bg_color)

def get_text_center(text:str, font):
    center = int((len(text) * font.WIDTH) // 2)
    return (center)
