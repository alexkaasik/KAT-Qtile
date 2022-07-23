#default
# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import layout, bar, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import os
import re
import subprocess
   
from keyconfig import *

def get_lang():
    return subprocess.check_output(['/bin/xkblayout-state', 'print', '%s']).decode('utf-8').strip()
    
def uptime_run():
    return subprocess.check_output(['/bin/uptime', '-p']).decode('utf-8').strip()
   
def point_left(color_fg, color_bg):
    return widget.TextBox(
            text="",
            padding=-4,
            fontsize="37",
            foreground=color_fg,
            background=color_bg)

def point_right(color_fg, color_bg):
    return widget.TextBox(
            text="",
            padding=-4,
            fontsize="37",
            foreground=color_fg,
            background=color_bg)

def border():
    return {
            "border_width" : 4,
            "single_border_width" : 0,
            "margin": 4,
            "border_focus" : '#9a009a',} 

layouts = [
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], **border()),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    #layout.Stack(num_stacks=2),
    layout.Bsp(**border()),	
    layout.Matrix(**border()),
    layout.MonadTall(**border()),
    layout.MonadWide(**border()),
    layout.RatioTile(**border()),
    layout.Tile(**border()),
    layout.TreeTab(**border()),
    layout.VerticalTile(**border()),
    layout.Zoomy(),
    layout.Floating()
]

widget_defaults = dict(
    font="JetBrainsMono Nerd Font",
    fontsize=12,
    padding=5,
    )
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout( 
                    foreground="#000000",
                    background="#9c0307"
                    ),

                point_left("#9c0307", "ab0421"),
                
                widget.GroupBox(background="ab0421"),
                
                point_left("#ab0421", "#bb063e"),
                
                widget.Prompt(background="#bb063e", foreground="#000000"),
                
                point_left("#bb063e", "#000000"),

#                widget.Chord(
#                    chords_colors={
#                        "launch": ("#ff0000", "#ffffff"),
#                    },
#                    name_transform=lambda name: name.upper(),
#                ),

                widget.Spacer(),

                widget.Clock(
                    format="%Y/%m/%d %a %H:%M %p",
                    fontsize=15
                    ),

                widget.Spacer(),

                point_right("#ff0000", "#000000"),

                widget.PulseVolume(
                        update_interval=0.1,
                        fontsize=15,
                        background="#ff0000"
                        ),

                point_right("#ffff00", "#ff0000"),
                
                widget.TextBox(
                        text = " ",
                        mouse_callbacks={'Button1':lazy.spawn(browser)},
                        fontsize=12, 
                        foreground="#000000", 
                        background="#ffff00",
                        padding=4
                        ),

                point_right("#8902cb", "#ffff00"),

                widget.GenPollText(
                        update_interval=0.1,
                        func=get_lang,
                        fmt='Keyboard: {}',
                        background="#8902cb",
                        foreground="#000000",
                        fontsize=15
                        ),

                point_right("#6502c6", "#8902cb"),
          
                point_right("#3302c0", "#6502c6"),
                
                widget.GenPollText(
                        update_interval=0.1,
                        func=uptime_run, 
                        background="#3302c0",
                        foreground="#000000",
                        fontsize=15
                        ),

                point_right("#230198", "#3302c0"),

                widget.Wttr(
                        location={
                            'EETN':'Tallinn',
                            },
                        update_interval=1,
                        background="#230198",
                        fontsize=14,
                        ),

                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                # widget.Systray(),
            ],
            25,
            # border_width=[2, 2, 2, 2],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
#        bottom=bar.Bar([
#            widget.GroupBox(),
#            widget.WindowName()
#            ],
#            30,
#            ),
        ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
