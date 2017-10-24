# W4L:
## Waifu 4 Laifu; search for the missing cock.


### Controls
Press 'e' to switch between English and Japanese.

Press '(space)' to advance dialog.

Use the arrow keys to change selections.


## Design Notes/Specifications
#### Style
We're switching to spaces for indentation because atom and every
editor with auto indent just fucks everything up every time I switch back
to vim. 'Tab' width will be 4-spaces wide.


#### Graphics
Very few terminals support in-terminal image viewing, not to mention
requiring external libraries, I've decided to compromise on an ASCII
'block' (█) version. It will still be based on real image files but
instead of presenting them directly, an average of the RGB values
will be taken for every 4x8 section and a block will be printed for each
in the top 78% of the terminal window (scr). *When creating* **images**,
*their* **resolution must be 304x184**.


#### Terminal Requirements
The game will use special characters as well as colour, most terminals can
support both of these given they've been updated in the last decade.

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

🢂🢀 (heavy arrows)

█ (block)
