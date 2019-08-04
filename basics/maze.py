# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 01:17:44 2019

@author: Aryan Singh
"""

from array import Array2D
from lliststack import Stack

class Maze:
    # Define constants to represent contents of the maze cells
    MAZE_WALL = "*"
    PATH_TOKEN = "x"
    TRIED_TOKEN = "o"
    
    # Creates a maze object with all cells marked as open.
    def __init__(self, numRows, numCols):
        self._mazeCells = Array2D(numRows, numCols)
        self._startCells = None
        self._exitCell = None
        
    # Returns the number of rows in the maze.
    def numRows(self):
        return self._mazeCells.numRows()
    
    # Returns the number of columns in the maze.
    def numCols(self):
        return self._mazeCells.numCols()
    
    def setWall(self, row, col):
        assert row>=0 and row < self.numRows and \
        col>=0 and col < self.numCols, "Cell index out of range"
        self._mazeCells.set( row, col, self.MAZE_WALL )
        
    def setStart(self, row, col):
        assert row>=0 and row < self.numRows and \
        col>=0 and col < self.numCols, "Cell index out of range"
        self._startCell = _CellPosition( row, col )
        
    def setExit(self, row, col):
        assert row>=0 and row < self.numRows and \
        col>=0 and col < self.numCols, "Cell index out of range"
        self._exitCell = _CellPosition( row, col )
        
    # find the path from the start to the end, 
    # and return true if there is a path in the maze
    
    def findPath(self):
        return 2
    
    def reset(self):
        return 1
        
    def draw(self):
        return 0
    
    def _validMove(self, row, col):
        return row>=0 and row < self.numRows and \
        col>=0 and col < self.numCols \
        and self._mazeCells[row, col] is None
        
    def exitFound(self, row, col):
        return row == self._exitCell.row and \
               col == self._exitCell.col

    
# Private storage class for holding a cell position.
class _CellPosition( object ):
    def __init__( self, row, col ):
        self.row = row
        self.col = col
    
    