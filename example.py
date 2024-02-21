from lib import st7789py, keyboard
from machine import Pin, SPI, PWM
from font import vga1_8x16 as small_font
from font import vga2_16x32 as font
from apps import HydraMenu

max_bright = const(65535)
min_bright = const(22000)
bright_step = const(500)

kb = keyboard.KeyBoard()
pressed_keys = kb.get_pressed_keys()
prev_pressed_keys = pressed_keys

display = st7789py.ST7789(
    SPI(1, baudrate=40000000, sck=Pin(36), mosi=Pin(35), miso=None),
    135,
    240,
    reset=Pin(33, Pin.OUT),
    cs=Pin(37, Pin.OUT),
    dc=Pin(34, Pin.OUT),
    backlight=None,
    rotation=1,
    color_order=st7789py.BGR
    )

blight = PWM(Pin(38, Pin.OUT))
blight.freq(1000)
blight.duty_u16(max_bright)



import json
with open("config.json", "r") as conf:
    config = json.loads(conf.read())
    bg_color = config["bg_color"]
    ui_color = config["ui_color"]

    menu = HydraMenu.Menu(display, small_font, "Main Menu", 6, bg_color=bg_color, ui_color=ui_color)

test_var = False
menu.add_item(HydraMenu.bool_item(menu, "Test 1", test_var))
menu.add_item(HydraMenu.bool_item(menu, "Test 2", False))
menu.add_item(HydraMenu.bool_item(menu, "Test 3", True))
menu.add_item(HydraMenu.bool_item(menu, "Test 4", True))
menu.add_item(HydraMenu.bool_item(menu, "Test 5", True))
menu.add_item(HydraMenu.bool_item(menu, "Test 6"))
menu.add_item(HydraMenu.bool_item(menu, "Test 7", True))
menu.add_item(HydraMenu.bool_item(menu, "Test 8"))
menu.add_item(HydraMenu.bool_item(menu, "Test 9", True))
menu.add_item(HydraMenu.bool_item(menu, "Test 10"))
menu.add_item(HydraMenu.bool_item(menu, "Test 11", True))
menu.add_item(HydraMenu.bool_item(menu, "Test 12", True))


menu.display_menu()

def go_down():
    menu.handle_input("down")
    menu.display_menu()
    menu.update_scroll_bar()

def go_up():
    menu.handle_input("up")
    menu.display_menu()
    menu.update_scroll_bar()
    
def press():
    global test_var
    test_var = menu.handle_input("press")
    menu.display_menu()

 
while True:
    pressed_keys = kb.get_pressed_keys()
    if pressed_keys != prev_pressed_keys:
        if ";" in pressed_keys and ";" not in prev_pressed_keys:
            go_up()
            prev_pressed_keys = pressed_keys
        elif "." in pressed_keys and "." not in prev_pressed_keys:
            go_down()
            prev_pressed_keys = pressed_keys
        elif "ENT" in pressed_keys and "ENT" not in prev_pressed_keys:
            press()
            prev_pressed_keys = pressed_keys
        prev_pressed_keys = pressed_keys


