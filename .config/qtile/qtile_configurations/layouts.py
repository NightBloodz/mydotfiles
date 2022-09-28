from libqtile import layout
from libqtile.config import Match
from .themes import *


layouts = [
    layout.Columns(border_normal = CNormalwin, border_focus = CfocusWin, border_width = borderWidth, margin = layoutMargin),
    layout.Max(),
]
