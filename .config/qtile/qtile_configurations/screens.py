from libqtile.config import Screen
from libqtile import bar
from libqtile.log_utils import logger
from .themes import *
from .widgets import *


screens = [Screen(top=bar.Bar(widgets, barSize, background=Cbar, margin=barMargin))]

