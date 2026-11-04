# mission_1

## diagnosis
normal_1 has the mug in the box while dim_1 does not.  The mask was to determine the object's color in normal brightness but when the it is dimmer than it will get the color wrong and so it detected the wrong thing. Contour table is to determine the shapes that it detected. The contour table for dim_1 did not work because it makes it seem like the mug is part of the table.

## limitations
I decreased lower and upper bound of saturation. This separated the cup's shadow from the actual cup. Saturation looks at how intense a color so it can help differentiate between the cup and the shadow. The limitation is that if the background is different and has a different reflection of the table then it might still get the shadow in the box.
