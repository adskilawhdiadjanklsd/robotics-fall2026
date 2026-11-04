# Lab 7 saved answers

## final.course_reflection
It is important to make robots to be able to detect correctly so that it would not cause many errors and not detect things it is supposed to. Something interesting is the trade off of classical and learned detection.

## final.synthesis
Classical detection is faster in time but it is less accurate than learned detection. Masks identify things by color and if the there is another thing with a similar color then it might think that it is the item or if the color is slightly off like if it is in the dark then it might not think it is the item. For pillar centering, having higher steering gain made the robot be inconsistent on getting the center. Lowering it and putting center tolerance lower made it closer to the center. For line following, increasing the gain made it correct its angle error better when it turns and decreasing its speed made it so that it uses lower speed when turning and helps it to be moving more on the path. Perception affect the outcome because if there is sudden lighting change then it might not work properly. 

## line_following.comparison
At first I did 0.08 gain and it was very bad for the curved path. It had a very hard time putting the camera at the center when curving. I increased the gain to 0.22 and it followed the curve more accurately.  Decreased speed to 0.10 so that it slows down on the curves so it can correct it better. 

## line_following.limits
A failure in control. The robot is slightly off of the line when turning the curve. Additional tests is if the robot can sense people around it and if it can stop when there is an object in front of it.

## mission_1.diagnosis
normal_1 has the mug in the box while dim_1 does not.  The mask was to determine the object's color in normal brightness but when the it is dimmer than it will get the color wrong and so it detected the wrong thing. Contour table is to determine the shapes that it detected. The contour table for dim_1 did not work because it makes it seem like the mug is part of the table.

## mission_1.limitations
I decreased lower and upper bound of saturation. This separated the cup's shadow from the actual cup. Saturation looks at how intense a color so it can help differentiate between the cup and the shadow. The limitation is that if the background is different and has a different reflection of the table then it might still get the shadow in the box.

## mission_2.choice
0.05 is good because it can detect the mug on occluded for learned. If you want the detection to be quick then classic is better. If you want it to be more accurate and do not care for time then learned is better. For larger images, learned might take even longer to process. Detailed foreground mask does not by itself identify the requested mug because if something has a similar color then it might get it wrong or if it is too dark it might not pick it up.

## mission_2.comparison
on 0.05 comparison detection threshold
normal: classic and learned has 2 correct-box, 0 false-box and 0 missed-mug counts. They both detected the mug.
dim: classic got 0 correct-box, 1 false-box, and 2 missed mug while learned still has 2 correct-box, 0 false-box and 0 missed-mug counts.
occluded: classic got 0 correct-box, 0 false-box, and 2 missed mug while learned has 2 correct-box, 0 false-box and 0 missed-mug counts.


## pillar_search.diagnosis
Attempt 20261104T032239-a2d0a7cb was the most centered. I increased the steering gain 1.00 to make it centered. Attempt 20261104T032917-6cb989f2 had steering gain of 0.2 and it was under shooting.  Attempt 20261104T034706-20aca9da had 0.5 and it was still over shooting. 

## pillar_search.evidence
Attempt 20261104T034905-63e13d9d had steering gain of 1.0. Some of the pillars looked more centered than the others. Attempt 20261104T034047-52d92ee6 had lower steering gain of 0.5 but has center tolerance of 0.02. This made it more centered and more consistent between pillars. Centered colored region and a stable hold not prove object identity or distance because another object can have the same color and the camera positioning.
