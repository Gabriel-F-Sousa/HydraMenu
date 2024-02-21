import math
from lib import beeper

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

    def handle_input(self, button):
        if button == 'up':
            self.cursor_index -= 1
            if self.ui_sound:
                self.beep.play(("E3","C3"), 100, self.volume)
            if self.cursor_index < 0:
                self.cursor_index = len(self.items) - 1

        elif button == 'down':
            self.cursor_index += 1
            if self.ui_sound:
                self.beep.play(("D3","C3"), 100, self.volume)
            if self.cursor_index >= len(self.items):
                self.cursor_index = 0
        
        elif button == 'press':
            return (self.items[self.cursor_index].press())

class bool_item:
    def __init__(self, menu, text: str = None, BOOL: bool = False, x_pos: int = 0, y_pos: int = 0, selected: bool = False):
        self.BOOL = BOOL
        self.menu = menu
        self.selected = selected
        self.text = text
        self.x_pos = x_pos
        self.y_pos = y_pos
    
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

    def press(self):
        self.BOOL = not self.BOOL
        self.menu.beep.play((("C3","E3","D3"),"D4","C4"), 100, self.menu.volume)
        self.draw()
        return (self.BOOL)

class pop_up_win:
    def __init__(self, display, int = 20, ui_color: int = 53243, bg_color: int = 4421):
        self.display = display
        self.ui_color = ui_color
        self.bg_color = bg_color
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
