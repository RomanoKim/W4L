# W4L:
## Waifu 4 Laifu; search for the missing cock.


### Controls
Press 'e' to switch between English and Japanese.

Press '(space)' to advance dialog.

Press 'b' to reverse dialog.

Use the arrow keys to highlight a selection.

Press 'ENTER' to accept selection.

##### Mouse (works in some areas):

Left click on a menu option to select and accept it.

Left click and scroll down advance dialog.

Right click and scroll up reverse dialog.


## Design Notes/Specifications
#### Style
We're switching to spaces for indentation because atom and every
editor with auto indent just fucks everything up every time I switch back
to vim. 'Tab' width will be 4-spaces wide.


#### Graphics
ASCII art, made with http://glassgiant.com/ascii/ using a width of **80**
and a height of **18**.


#### Terminal Requirements
The game will use special characters as well as colour, most terminals can
support both of these given they've been updated in the last decade.

The game will have partial-mouse support, as in the mouse will work in most
areas of the game but the player will still require a keyboard. Note that
it is not necessary to use a terminal with mouse support (though most do),
the game will poll for mouse events and will move on if they are not
supported.

The minimum terminal size I've decided on is **76** half-width characters
across which is equivalent to **38** full-width characters across, as well as
**23** rows down. Which is just slightly lower than the standard 80x24. Meaning
that the game should be playable in pretty much any terminal that supports
colour and has adequate screen real-estate (resolution). Note that; that also
means that no line of text in the game can have more than **76** characters,
where japanese full-width characters will count as **2** and punctuation and
regular ASCII will count as **1**.

Including japanese terminal fonts, the following characters should be visible in
your terminal (copy and paste if you're seeing this in browser):

🢂 🢀 (heavy arrows)

█ (block)
