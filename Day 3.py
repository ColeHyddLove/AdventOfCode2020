# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 01:40:34 2021

@author: colel
"""

"""
--- Day 3: Toboggan Trajectory ---
With the toboggan login problems resolved, you set off toward the airport. 
While travel by toboggan might be easy, it's certainly not safe: there's very 
minimal steering and the area is covered in trees. You'll need to see which 
angles will take you near the fewest trees.

Due to the local geology, trees in this area only grow on exact integer 
coordinates in a grid. You make a map (your puzzle input) of the open squares 
(.) and trees (#) you can see. For example:

..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#

These aren't the only trees, though; due to something you read about once 
involving arboreal genetics and biome stability, the same pattern repeats to 
the right many times:

..##.........##.........##.........##.........##.........##.......  --->
#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........#.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...##....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#  --->
You start on the open square (.) in the top-left corner and need to reach the 
bottom (below the bottom-most row on your map).

The toboggan can only follow a few specific slopes (you opted for a cheaper 
model that prefers rational numbers); start by counting all the trees you would
encounter for the slope right 3, down 1:

From your starting position at the top-left, check the position that is right 3
and down 1. Then, check the position that is right 3 and down 1 from there, 
and so on until you go past the bottom of the map.

The locations you'd check in the above example are marked here with O where 
there was an open square and X where there was a tree:

..##.........##.........##.........##.........##.........##.......  --->
#..O#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....X..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#O#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..X...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.X#.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#.O..#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........X.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.X#...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...#X....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...X.#.#..#...#.#.#..#...#.#.#..#...#.#  --->
In this example, traversing the map using this slope would cause you to 
encounter 7 trees.

Starting at the top-left corner of your map and following a slope of right 3 
and down 1, how many trees would you encounter?
"""

text_file = open("input_Day3.txt","r")
S = text_file.readlines()
#Very Important to clear the '\n' character from the end of the string
newline_del = len(S[0])-1
for i in range(len(S)):
    S[i] = S[i].rsplit("\n")[0]
    
text_file.close()

slope = [1,3]

print("How long is the hill?: ",len(S))

"""
Input: Slope tuple in the form: [Rise, Run], Set of Strings to represent a course
Output: Number of Crashes
"""
def count_crashes(slope,S):
    num_crashes = 0
    for i in range(0,len(S),slope[0]):
        x = i
        y = ((int(slope[1]*i/slope[0])))%len(S[i])
        #print(x,y)
        if S[x][y] == "#":
            num_crashes += 1
        
    return num_crashes

print("Part 1: ",count_crashes(slope, S))

"""
Time to check the rest of the slopes - you need to minimize the probability of
a sudden arboreal stop, after all.

Determine the number of trees you would encounter if, for each of the following
 slopes, you start at the top-left corner and traverse the map all the way to 
the bottom:

Right 1, down 1.
Right 3, down 1. (This is the slope you already checked.)
Right 5, down 1.
Right 7, down 1.
Right 1, down 2.
In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s)
respectively; multiplied together, these produce the answer 336.

What do you get if you multiply together the number of trees encountered on
each of the listed slopes?
"""
T = [[1,1],[1,3],[1,5],[1,7],[2,1]]

"""
Input: Set of slope tuples in the form: [Rise, Run], Set of Strings to represent a course
Output: Product of Crashes
"""
def multiply_crashes(slopes, S):
    crash_mult = 1
    for i in range(len(T)):
        print("Slope: ", T[i], " # of Crashes: ", count_crashes(T[i],S))
        crash_mult *= count_crashes(slopes[i], S)
    return crash_mult

print("Part 2: ", multiply_crashes(T,S))