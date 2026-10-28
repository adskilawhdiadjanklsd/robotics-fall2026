# Week 6: SLAM and Mapping

- email: weixi.huang15@login.cuny.edu
- name: Wei Xi Huang

## final.course_reflection

It was interesting that the mapping accuracy was not what I expected. The quality rating for the first map was 84.8 while the second map was 82.3. I expected the second map to be more accurate because had a longer route and visited every area of the house but the first map was more accurate. It is important for robots to know correctly where it is and where and what is in the area so that it doesn't crash into and break things.

## final.synthesis

For the first house, the robot knows most of the outline of the house and some of the objects in the room and the legs of the table. One corner of the map, some corners of a room, and under the tables are unknown  because the robot did not go far enough for the lidar to pick it up. For the second map, the robot had a longer route that covers more area and took more time moving around the house so it knows more about the objects of the house and has the outline of the entire house. However, the biggest issue of this map was that two of the left side table's legs are inside another room. A possible map correction is for the robot to revisit all the rooms and do the reverse of the route so it can correct it. I would trust the first map more because it has a quality rating of 84.8 and it has more accurate object placement but if the second map fixes the table placement then I would choose the second map because it covers more of the area with covering 91.36 m^2 compared to the first map which covers 85.7 m^2.

## mission_1.drift_and_revisit

The walls near the entrance is shifted and some are doubled. The left side of the entrance seems like there is 2 walls and there are some LiDAR that detected it is a free space. The right side of the entrance it already saw that it is free space but there is an extra wall that blocks the free space.

## mission_1.limitations

Under the table on the right side of the house. When going through the area, the robot did not go close enough to the area to see what is there. The middle left of the house is the place where the route did not go to so it is too far for the sensors to detect. 

## mission_1.route.original_prediction

Go forward then turn to enter the door way then go right then right again to get to the bottom right room go forward so it can map out the walls then turn back then go to y=5 then go left when it sees a wall then go down. When it see a wall then turn around and get out of the room then go down and go right to get to the left side of the house when it reaches a wall turn right then if there is an opening on the left side turn left then go down. It might not cover all the walls since the LiDAR might not reach it to map all the walls.

## mission_1.route.prediction_draft

It should go to every room. It will revisit the places where it has to go to get to another room and when it goes inside a room it has to go back out. It might not map out places that are too far away from it.

## mission_2.comparison

The first strategy since it has more known area per minute of 10.71 compared to 5.08 for strategy 2. Strategy 2 has more known fraction but it took a lot longer to map out while strategy 1 has fast but some areas are not mapped.

## mission_2.map_choice

I would trust strategy 1 more because for strategy 2, 2 of the legs of the table on the left side of the house is inside of one of the other rooms.  Strategy 1 mapped less of the area with know area of 85.7 m^2  but is more accurate because it has a quality score of 84.8. Strategy 2 has mapped with 91.36 m^2 more but less accurate with quality score of 82.3.

## mission_2.strategy.original_prediction

I will make this route try to explore more so it have less unknown areas. It should produce a clearer map because it will go to areas that it did not explore before.

## mission_2.strategy.prediction_draft

I will make this route try to explore more so it have less unknown areas. It should produce a clearer map because it will go to areas that it did not explore before.
