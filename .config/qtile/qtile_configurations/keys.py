from libqtile.config import Key
from libqtile.command import lazy


mod = "mod4"
terminal = "kitty"


keys = [

    #change focused window
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),

    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
   


    #change to the left and right group 
    Key([mod, "shift"], "Right", lazy.screen.next_group()),
    Key([mod, "shift"], "Left", lazy.screen.prev_group()),



    #grow windows
    Key([mod, "control"], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    


    #launch programs
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "f", lazy.spawn("firefox"), desc="browser"),
    Key([mod], "m", lazy.spawn("rofi -show drun -theme ~/.config/rofi/launchers/type-2/style-10.rasi")),
    Key([mod], "e", lazy.spawn("thunar"), desc="thunar"),           
    Key([mod], "v", lazy.spawn("vmware"), desc="vmware"),
    

    Key([mod], "e", lazy.spawn("thunar"), desc="thunar"),       
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.spawn("rofi -show windowcd -theme ~/.config/rofi/launchers/type-2/style-15.rasi"), desc="Toggle between layouts"),
    Key([mod], "F11", lazy.next_layout(), desc="next layout"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    Key([mod], "z", lazy.window.toggle_floating()),

   ]
