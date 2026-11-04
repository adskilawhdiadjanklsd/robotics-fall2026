# mission_2

## choice
0.05 is good because it can detect the mug on occluded for learned. If you want the detection to be quick then classic is better. If you want it to be more accurate and do not care for time then learned is better. For larger images, learned might take even longer to process. Detailed foreground mask does not by itself identify the requested mug because if something has a similar color then it might get it wrong or if it is too dark it might not pick it up.

## comparison
on 0.05 comparison detection threshold
normal: classic and learned has 2 correct-box, 0 false-box and 0 missed-mug counts. They both detected the mug.
dim: classic got 0 correct-box, 1 false-box, and 2 missed mug while learned still has 2 correct-box, 0 false-box and 0 missed-mug counts.
occluded: classic got 0 correct-box, 0 false-box, and 2 missed mug while learned has 2 correct-box, 0 false-box and 0 missed-mug counts.

