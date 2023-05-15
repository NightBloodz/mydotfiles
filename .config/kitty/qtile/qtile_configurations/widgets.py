from libqtile import widget
from libqtile.command import lazy
from .variables import *


widget_defaults = dict(
    font = "sans",
    fontsize = 14,
    padding_x = 8,
    background = Cbar,    
)




widgets = [
    widget.GroupBox(
        fontsize = 32,
        margin_x = 0,
        highlight_method = "text",
        disable_drag = True,
        this_screen_border = "#404040",
        this_current_screen_border = Cwidget1, 
        active = "#999284"
        

    ),

    widget.Sep(
             background = Cbar,
             foreground = Cbar,
             linewidth = 555, 
             ),

    widget.LaunchBar(
             foreground = Cwidget1,
             background = Cbar,
             default_icon = '/home/nightbloodz/images/power.png',
             progs = [('Shutdown', '/home/nightbloodz/.config/rofi/powermenu/type-1/powermenu.sh', 'logout from qtile')] 

    ),


    widget.Sep(
             background = Cbar,
             foreground = Cbar,
             linewidth = 550, 
             ),
    
    widget.MemoryGraph(
        background = Cbar,
        fill_color = Cwidget1,
    ),        




    widget.Net(
        interface = interface,
        format = '{down} ↓↑ {up}',
        foreground = Cwidget1,
        background = Cbar,
        padding = 14,
        prefix = "M"
    ),

     


    widget.Clock(
        foreground = Cwidget1,
        background = Cbar,
        format = "%d/%m - %H:%M",
    ),



]


    
