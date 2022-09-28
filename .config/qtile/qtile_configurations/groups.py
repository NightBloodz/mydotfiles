from libqtile.config import Key, Group
from libqtile.command import lazy
from .keys import mod, keys


groups = [Group(i) for i in [ "","","","","","漣" ]]

for i, group in enumerate(groups):
    n_escritorio = str(i+1)
    keys.extend(
        [
            #change to group
            Key([mod], n_escritorio, lazy.group[group.name].toscreen()),

            #pass window to group
            Key([mod, "shift"], n_escritorio, lazy.window.togroup(group.name, switch_group=False)),

                        
        ]
    )
