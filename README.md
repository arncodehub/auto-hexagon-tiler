**Automated Hexagon Tiling**

This program generates hexagonal tile patterns for you

Note, there is no GUI, just the commands are in a class called `HexagonTiler`

`HexagonTiler()` class requires 2 parameters, *size* and *layer_colors*.



*size* is a whole number (representing about how large the hexagon is)

The 'unit' that *size* represents, is not well defined.

So, just try different size values and see what looks best to you.



*layer_colors* is a list of tuples.

Each tuple contains 3 values, being an RGB pair.

Layer 1, being the first tuple in the layer list, represents the central hexagon in the pattern.

Layer 2, being the second tuple, represents the hexagons around the central hexagon.

Layer 3, represents the hexagons around those, Layer 4 is around Layer 3, and so on...

The RGB values within each tuple inside of the list, 
represents the color of the hexagons in that layer. 

Index 0 of the list (1st tuple), is the color of the 1st layer, and so on...



Once a `HexagonTiler` class is defined, with the *size* and *layer_colors* arguments,
the class has a `.draw_pattern()` method/command, to draw the desired patter.



Here is an example, for a center of red, surrounding tiles of yellow, and layer 3 of blue.

`tiler = HexagonTiler(20, [(220, 100, 70), (220, 190, 50), (80, 100, 220)])`

^ This is to be put, within the 1st 'insert code here' block

`tiler.draw_pattern(window)`

^ This is to be put, within the 2nd 'insert code here' block



More on the example, replace the *size* and *layer_colors* arguments from the first code snip, with your own desired size and colors.

You are to, copy the full code within the GitHub repo, then within the 'insert code here',
blocks, paste in the code you want, based on this documentation here.

Specify the size (just try different sizes; there is no well defined unit size),
and the layer colors.

This makes it easy to generate aesthetic hexagonal tile patterns!