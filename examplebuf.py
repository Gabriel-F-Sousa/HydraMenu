from lib import st7789fbuf, keyboard, mhconfig, HydraMenu
from machine import Pin, SPI
from lib import microhydra as mh

"""
This example app is designed to show off the capabilities of the HydraMenu module!

The code below includes a heavy amount of comments, and docstrings, to help explain what every step is doing.
This code requires some additional modules from MicroHydra's library.
"""


""" Create some global objects to use for this app:
"""

# init our display
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

# create keyboard, and 'dry run' the get_new_keys function, just to initialize it's values.
kb = keyboard.KeyBoard()
kb.get_new_keys()

# create a config object to pass to the menu.
config = mhconfig.Config()

# mhconfig loads stored values set in config.json.
# But, if we'd like, we can overwrite them with some custom values for our app.
# as long as you dont call "config.save()", these values will be temporary.
# you can even create multiple config objects if you'd like.
config['volume'] = 5
config['ui_sound'] = True
config['bg_color'] = 160
config['ui_color'] = 65526
# this regenerates the full config color palette based on our new colors.
config.generate_palette()




""" Create our HydraMenu.Menu:
"""
menu = HydraMenu.Menu(
    # display_fbuf is passed to signal that we are using the st7789fbuf driver.
    # we would use display_py if we were using st7789py.
    display_fbuf=display,
    # pass our config object, which was created above.
    # if omitted, HydraMenu will create it's own config object.
    config=config,
    )




""" Define some callback functions:
"""
# this function is called whenever a changed value is submitted:
def print_menu_callback(caller, new_value):
    print(f"Callback called by {type(caller).__name__}. It passed this {type(new_value).__name__}: {new_value}")

# this function is called as value is modified (even before confirming the change):
def print_instant_callback(caller, current_value):
    print(f"Instant callback: {current_value}")
    
# this function is called when the "confirm" button is pressed:
def menu_confirm(caller):
    print("Called menu_confirm.")





"""Add menu items to the menu:
"""

# this is an integer menu item:
menu.append(HydraMenu.IntItem(
    # items should be passed their parent menu, and they can be given display text.
    menu=menu, text="IntItem",
    # Items can be given a value as well. For an IntItem, this value should be an int
    value=5,
    # some MenuItems also have special keywords that can be used for further options.
    # int items, for example, can be given a minimum and maximum value.
    min_int=0, max_int=10,
    # callbacks are what makes this all functional.
    # Pass the function you want to be called every time a value is confirmed. 
    callback=print_menu_callback,
    # You can also use an 'instant_callback' if you want to track the value as it changes.
    # this is what the main settings app uses to update the volume, and ui colors as they're changed.
    instant_callback=print_instant_callback
    ))

# this is an item which selects a 16 bit "RGB 565" color.
# the returned value will be a single integer, representing the color choice.
menu.append(HydraMenu.RGBItem(
    menu=menu, text="RGBItem",
    value=65535, # white (0xffff)
    callback=print_menu_callback
    ))

# this item allows the user to enter some text. It's value is a string.
menu.append(HydraMenu.WriteItem(
    menu=menu, text="WriteItem",
    value="Testing",
    callback=print_menu_callback
    ))

# Write items can also have their text hidden by setting "hide=True"
menu.append(HydraMenu.WriteItem(
    menu=menu, text="Write2",
    value="Secret!",
    callback=print_menu_callback,
    hide=True
    ))

# BoolItems just work as a toggle switch, and return bool
menu.append(HydraMenu.BoolItem(
    menu=menu, text="BoolItem",
    value=True,
    callback=print_menu_callback
    ))

# "DoItems" are used just for calling a specific callback.
# They can be used to place buttons in the menu.
# this can be used for a "confirm" button:
menu.append(HydraMenu.DoItem(
    menu, "Confirm",
    callback=menu_confirm
    ))
# it can also be used to do any random thing you'd like:
menu.append(HydraMenu.DoItem(
    menu, "Hello",
    callback=(lambda x:print("Hello World!"))
    ))




# create a variable to remember/decide when we need to redraw the menu:
redraw = True

# this loop will run our menu's logic.
while True:
    
    # get our newly pressed keys
    keys = kb.get_new_keys()
    
    # pass each key to the handle_input method of our menu.
    for key in keys:
        menu.handle_input(key)
    
    
    # when any key is pressed, we must redraw:
    if keys:
        redraw = True
    
    # this is used to prevent unneeded redraws (and speed up the app)
    # just calling menu.draw and display.show every loop also works, but it feels slower.
    if redraw:
        # menu.draw returns True when it is mid-animation,
        # and False when the animation is done (therefore, does not need to be redrawn until another key is pressed)
        redraw = menu.draw()
        display.show()  


