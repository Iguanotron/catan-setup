#!/usr/bin/env python3

import random


class Tile(object):
	"""Represents a single Catan tile."""

	roll_pips = {
		2:  1,
		3:  2,
		4:  3,
		5:  4,
		6:  5,
		8:  5,
		9:  4,
		10: 3,
		11: 2,
		12: 1
	}

	def __init__(self, terrain="Desert", roll=0):
		self.terrain = terrain
		self.roll    = roll

	def pips(self):
		"""Return the number of pips on this tile, based on its roll value."""
		try:
			return self.roll_pips[self.roll]
		except KeyError:
			return 0
		
	def __repr__(self):
		return "Tile({:s}, {:s})".format(repr(self.terrain), repr(self.roll))

	def draw(self, row, col, grid):
		"""
		Draw self onto the character grid, with upper-left corner (row, col).
		A 13 (rows) by 7 (columns) space is required to draw a Tile.
		Tiles are drawn in the following format, where the % marks the
		upper-left corner and is not drawn:

			%  _______
			  /       \
			 /         \
			/ -terrain- \
			\ --roll--- /
			 \ -pips-- /
			  \_______/

		"""
		grid[row  ][col+3:col+10] =    "_______"
		grid[row+1][col+2:col+11] =   "/       \\"
		grid[row+2][col+1:col+12] =  "/         \\"
		grid[row+3][col  :col+13] = "/ {:^9s} \\".format(self.terrain)
		grid[row+4][col  :col+13] = "\\ {:^9d} /".format(self.roll)
		grid[row+5][col+1:col+12] =  "\\ {:^7s} /".format('*'*self.pips())
		grid[row+6][col+2:col+11] =   "\\_______/"

class Harbor(object):
	"""Represents a Catan harbor tile"""

	def __init__(self, direction="N", resource="?", ratio=None):
		self.direction = direction
		self.resource = resource
		if ratio:
			self.ratio = ratio
		elif resource == "?":
			self.ratio = (3, 1)
		else:
			self.ratio = (2, 1)

	def __repr__(self):
		return "Harbor({0:s}, {1:s}, {2})".format(repr(self.direction),
		                                          repr(self.resource),
		                                          self.ratio)

	def draw(self, row, col, grid):
		"""
		Draw self onto the character grid, with upper-left corner (row, col).
		A 13 (rows) by 7 (columns) space is required to draw a Harbor.
		Harbors are drawn in the following format, where the % marks the
		upper-left corner and is not drawn. This example has a direction
		of NE:

			%       __
			        \ \
			         \ \
			     -:-  \ \
			   ------- \/
			            
			           

		"""
		grid[row+3][col+3:col+10] = "{0:>3d}:{1:<3d}".format(*self.ratio)
		grid[row+4][col+3:col+10] = "{:^7s}".format(self.resource)

		if self.direction == "N":
			grid[row  ][col+3:col+10] =  "_______"
			grid[row+1][col+2:col+11] = "/_______\\"			
		elif self.direction == "NE":
			grid[row  ][col+8 :col+10] = "__"
			grid[row+1][col+8 :col+11] = "\\ \\"
			grid[row+2][col+9 :col+12] =  "\\ \\"
			grid[row+3][col+10:col+13] =   "\\ \\"
			grid[row+4][col+11:col+13] =    "\\/"
		elif self.direction == "SE":
			grid[row+3][col+11:col+13] =    "/\\"
			grid[row+4][col+10:col+13] =   "/ /"
			grid[row+5][col+9 :col+12] =  "/ /"
			grid[row+6][col+8 :col+11] = "/_/"
		elif self.direction == "S":
			grid[row+5][col+2:col+11] = "_________"
			grid[row+6][col+2:col+11] = "\\_______/"
		elif self.direction == "SW":
			grid[row+3][col  :col+2] = "/\\"
			grid[row+4][col  :col+3] = "\\ \\"
			grid[row+5][col+1:col+4] =  "\\ \\"
			grid[row+6][col+2:col+5] =   "\\_\\"
		elif self.direction == "NW":
			grid[row  ][col+3:col+5] =    "__"
			grid[row+1][col+2:col+5] =   "/ /"
			grid[row+2][col+1:col+4] =  "/ /"
			grid[row+3][col  :col+3] = "/ /"
			grid[row+4][col  :col+2] = "\\/"
		else:
			pass # error



class GameBoard(object):
	"""Represents a Catan game board."""

	col_lengths = [3, 4, 5, 4, 3] # in hexes
	offsets = [2, 1, 0, 1, 2] # in half-hex increments
	tile_quantities = {
		"Pasture":   4,
		"Fields":    4,
		"Forest":    4,
		"Mountains": 3,
		"Hills":     3,
		"Desert":    1
	}
	roll_quantities = { # quantities of each roll number
		2:  1,
		3:  2,
		4:  2,
		5:  2,
		6:  2,
		8:  2,
		9:  2,
		10: 2,
		11: 2,
		12: 1
	}
	pip_threshold = 5 # tiles with more pips than this cannot be neighbors

	def __init__(self):
		tiles = [Tile(terrain)
		         for terrain, qty in self.tile_quantities.items()
		         for i in range(qty)]
		random.shuffle(tiles)

		# board: the game board, stored as columns of Tiles
		self.board = [[tiles.pop(0) for i in range(x)]
		              for x in self.col_lengths]

	def number_tiles(self):
		"""
		Number the tiles in self.board, using the roll_quantities with quantities
		in self.roll_quantities.
		"""
		print("Numbering Tiles", end="")
		while True:
			print(".", end="")
			roll_quantities = [roll
			                   for roll, qty in self.roll_quantities.items()
			                   for i in range(qty)]
			random.shuffle(roll_quantities)

			for col in self.board:
				for tile in col:
					if (tile.terrain != "Desert"):
						tile.roll = roll_quantities.pop(0)

			if self.valid():
				print("Done.")
				return


	def valid(self):
		"""
		Returns whether the board numbering is valid, i.e. whether
		no tiles above the pip threshold are neighbors.
		"""
		for col, height in enumerate(self.col_lengths):
			for row in range(height):
				if self.board[col][row].pips() >= self.pip_threshold:
					for cell in self.neighbors(col, row):
						if cell.pips() >= self.pip_threshold:
							return False
		return True

	def neighbors(self, col, row):
		"""Returns a list of neighbors of the tile at the given location."""
		coords = [(col, row - 1),
		          (col, row + 1)]

		if col > 0:
			offset_diff = (self.offsets[col] - self.offsets[col - 1]) / 2
			coords.extend([(col - 1, row + int(offset_diff - 0.5)),
			               (col - 1, row + int(offset_diff + 0.5))])

		if col + 1 < len(self.col_lengths):
			offset_diff = (self.offsets[col] - self.offsets[col + 1]) / 2
			coords.extend([(col + 1, row + int(offset_diff - 0.5)),
			               (col + 1, row + int(offset_diff + 0.5))])

		return [self.board[r][c] for (r, c) in coords
		        if c >= 0 and c < self.col_lengths[r]]

	def print(self):
		"""Prints the board to standard output."""

		cells_tall = max([offset/2 + row_len for (row_len, offset) in zip(self.col_lengths, self.offsets)])
		cells_wide = len(self.col_lengths)

		char_grid = [[" " for j in range(10*cells_wide + 3)] for i in range(int(6*cells_tall) + 1)]

		for col, cells in enumerate(self.board):
			for row, cell in enumerate(cells):
				cell.draw(row*6 + 3*self.offsets[col], col*10, char_grid)

		for row in char_grid:
			print(''.join(row))


board = GameBoard()
board.number_tiles()
board.print()
print()
