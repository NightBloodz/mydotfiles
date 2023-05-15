from libqtile import hook
from libqtile.utils import guess_terminal

from qtile_configurations.variables import *
from qtile_configurations.groups import *
from qtile_configurations.keys import *
from qtile_configurations.screens import *
from qtile_configurations.layouts import *
from qtile_configurations.mouse import *
from qtile_configurations.widgets import *



import os
import subprocess



auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

auto_minimize = True

wl_input_rules = None




@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])

wmname = "LG3D"





