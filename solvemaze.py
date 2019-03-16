# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 22:22:57 2019

@author: Aryan Singh
"""

'''
solve maze - solver for maze, backtracking

'''

from maze import Maze

def main():
    maze = buildMaze("mazefile.txt")
    if maze.findPath():
        print('Path found')
        maze.draw()
    else:
        print('Path not found')

def buildMaze(filename):
    infile = open(filename, "r")