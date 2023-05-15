from libqtile import layout
from libqtile.config import Match

from .variables import *

layouts = [
    layout.Columns(border_normal = CNormalwin, border_focus = CfocusWin, border_width = borderWidth, margin = layoutMargin),
    layout.Max(border_normal = CNormalwin, border_focus = CfocusWin, border_width = borderWidth, margin = layoutMargin),
]
