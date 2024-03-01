from lib import st7789py, keyboard, HydraMenu
from machine import Pin, SPI, PWM
from font import vga1_8x16 as small_font
from font import vga2_16x32 as font
from lib import microhydra as mh

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
config = {}
with open("config.json", "r") as conf:
    config = json.loads(conf.read())
    bg_color = config["bg_color"]
    ui_color = config["ui_color"]
#     menu = HydraMenu.Menu(display, small_font, "Main Menu", 5, y_padding=0, bg_color=bg_color, ui_color=ui_color)
    menu = HydraMenu.Menu(display, font, "Main Menu", 4, y_padding=0, bg_color=bg_color, ui_color=ui_color)

test_var = False
r,g,b = mh.separate_color565(bg_color)
bg_rgb = [r,g,b]
r,g,b = mh.separate_color565(ui_color)
ui_rgb = [r,g,b]

def rgb_change(caller, rgb: list):
    global config
    color = mh.combine_color565(rgb[0],rgb[1],rgb[2])
    if caller.text == "ui_color":
        config["ui_color"] = color
    if caller.text == "bg_color":
        config["bg_color"] = color
    print(caller.text, color)

def bool_change(caller, BOOL):
    if caller.text == "Test 1":
        test_var = BOOL
        print(caller.text, BOOL)

def  save_conf(caller):
    global config
    with open("config.json", "w") as conf:
        conf.write(json.dumps(config))
    print("save config: ", config)

def change_vol(caller, numb):
    print(caller.text, numb)

menu.add_item(HydraMenu.RGB_item(menu, "ui_color", ui_rgb, font=small_font, callback=rgb_change))
menu.add_item(HydraMenu.RGB_item(menu, "bg_color", bg_rgb, font=small_font, callback=rgb_change))
menu.add_item(HydraMenu.bool_item(menu, "Test 1", test_var, callback=bool_change))
menu.add_item(HydraMenu.int_select_item(menu, 0, -10, 10, "Volume", callback=change_vol))
menu.add_item(HydraMenu.do_item(menu, "save config", callback=save_conf))
# menu.add_item(HydraMenu.bool_item(menu, "Test 5", True))
# menu.add_item(HydraMenu.bool_item(menu, "Test 6"))
# menu.add_item(HydraMenu.bool_item(menu, "Test 7", True))
# menu.add_item(HydraMenu.bool_item(menu, "Test 8"))


menu.display_menu()

def go_down():
    menu.handle_input("down")

def go_up():
    menu.handle_input("up")
    
def press():
    menu.handle_input("press")
 
while True:
    pressed_keys = kb.get_pressed_keys()
    if pressed_keys != prev_pressed_keys:
        if ";" in pressed_keys and ";" not in prev_pressed_keys:
            go_up()
            prev_pressed_keys = pressed_keys
        elif "." in pressed_keys and "." not in prev_pressed_keys:
            go_down()
            prev_pressed_keys = pressed_keys
        elif "/" in pressed_keys and "." not in prev_pressed_keys:
            menu.handle_input("right")
        elif "," in pressed_keys and "." not in prev_pressed_keys:
            menu.handle_input("left")
        elif "ENT" in pressed_keys and "ENT" not in prev_pressed_keys:
            press()
            prev_pressed_keys = pressed_keys
        prev_pressed_keys = pressed_keys
