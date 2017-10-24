# W4L
best vn


### Controls
Press 'e' to switch between english and japanese.


## Design Notes/Specifications
We're switching to spaces for indentation because atom and every
editor with auto indent just fucks everything up every time I switch back
to vim.

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