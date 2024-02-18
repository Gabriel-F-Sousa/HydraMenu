class Menu:
    def __init__(self, font, per_page: int = 3, ui_color: int = 53243, bg_color: int = 4421):
        from lib import microhydra as mh
        self.items = []
        self.selected_item = 0
        self.scroll_offset = 0
        self.font = font
        self.per_page = 3
        self.ui_color = ui_color
        self.bg_color = bg_color
        self.mid_color = mh.mix_color565(ui_color, bg_color)

    def add_item(self, item):
        self.items.append(item)

    def display_menu(self):
        display.fill(self.bg_color)
        visible_items = self.items[self.scroll_offset:self.scroll_offset+self.per_page]
        for i, item in enumerate(visible_items):
            y = 20 + i * self.font.HEIGHT
            if i == self.selected_item - self.scroll_offset:
                display.text(self.font, '>', 5, y, self.ui_color, self.mid_color)
                display.text(self.font, item, 20, y, self.ui_color, self.mid_color)
            else:
                display.text(self.font, ' ', 5, y, self.ui_color, self.bg_color)
                display.text(self.font, item, 20, y, self.ui_color, self.bg_color)
            display.hline(0, y, display.width, self.mid_color)
        display.hline(0, 20 + (i+1) * self.font.HEIGHT, display.width, self.mid_color)
        
        if self.scroll_offset + self.per_page >= len(self.items):
            self.scroll_offset = 0

    def handle_input(self, button):
        if button == 'up':
            self.selected_item = (self.selected_item - 1) % len(self.items)
            if self.scroll_offset == 0 and self.selected_item == 7:
                self.scroll_offset = len(self.items) - self.per_page
                self.selected_item = len(self.items) - 1
            elif self.selected_item < self.scroll_offset:
                self.scroll_offset -= 1

        elif button == 'down':
            self.selected_item = (self.selected_item + 1) % len(self.items)
            if self.selected_item >= self.scroll_offset + self.per_page:
                self.scroll_offset += 1
        elif button == 'enter':
            selected_action = self.items[self.selected_item]
