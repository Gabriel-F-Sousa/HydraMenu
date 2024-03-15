from lib import st7789fbuf, keyboard
import HydraMenubuf as HydraMenu
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

display = st7789fbuf.ST7789(
    SPI(1, baudrate=40000000, sck=Pin(36), mosi=Pin(35), miso=None),
    135,
    240,
    reset=Pin(33, Pin.OUT),
    cs=Pin(37, Pin.OUT),
    dc=Pin(34, Pin.OUT),
    backlight=Pin(38, Pin.OUT),
    rotation=1,
    color_order=st7789fbuf.BGR
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
#     menu = HydraMenu.Menu(display, small_font, "Main Menu", 8, y_padding=0, bg_color=bg_color, ui_color=ui_color)
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

def change_vol(caller, numb):
    global config
    config["volume"] = numb
    print(caller.text, numb)
    
def change_ssd(caller, text):
    global config
    config["wifi_ssid"] = text
    print(caller.text, text)
    
def change_wifi_pass(caller, text):
    global config
    config["wifi_pass"] = text
    print(caller.text, text)

def change_timezone(caller, numb):
    global config
    config["timezone"] = numb
    print(caller.text, numb)

def  save_conf(caller):
    global config
    with open("config.json", "w") as conf:
        conf.write(json.dumps(config))
    print("save config: ", config)

menu.add_item(HydraMenu.int_select_item(menu, config["volume"], 0, 10, "volume", callback=change_vol))
menu.add_item(HydraMenu.RGB_item(menu, "ui_color", ui_rgb, font=small_font, callback=rgb_change))
menu.add_item(HydraMenu.RGB_item(menu, "bg_color", bg_rgb, font=small_font, callback=rgb_change))
menu.add_item(HydraMenu.write_item(menu, "wifi_ssid", config["wifi_ssid"], font=small_font, callback=change_ssd))
menu.add_item(HydraMenu.write_item(menu, "wifi_pass", config["wifi_pass"], hide=True, font=small_font, callback=change_wifi_pass))
menu.add_item(HydraMenu.bool_item(menu, "sync_clock", config["sync_clock"], callback=bool_change))
menu.add_item(HydraMenu.int_select_item(menu, config["timezone"], -13, 13, "timezone", callback=change_timezone))
menu.add_item(HydraMenu.do_item(menu, "confirm", callback=save_conf))


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
        if menu.in_submenu and len(pressed_keys) > 0 and pressed_keys[-1] not in prev_pressed_keys:
            menu.handle_input(pressed_keys[-1])
            prev_pressed_keys = pressed_keys
        elif ";" in pressed_keys and ";" not in prev_pressed_keys:
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
        
        display.show()  
        prev_pressed_keys = pressed_keys
#     print(prev_pressed_keys)











