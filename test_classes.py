import tabulate

from classes import Player, Point, Board

# coordinates = [1, 1]
# board = [[[], "_", "_", [], "_", "_", []],
#          ["_", [], "_", [], "_", [], "_"],
#          ["_", "_", [], [], [], "_", "_"],
#          [[], [], [], "_", [], [], []],
#          ["_", "_", [], [], [], "_", "_"],
#          ["_", [], "_", [], "_", [], "_"],
#          [[], "_", "_", [], "_", "_", []],
#          ]
# board[coordinates[0]][coordinates[1]] = "X"
# print(tabulate.tabulate(board, headers="0123456", tablefmt="fancy_grid",
#       showindex=True, numalign="center", stralign="center"))


def test_player_class():
    point00 = Point((0, 0), [(0, 3), (1, 1), (3, 0)])
    player1 = Player(1)
    player2 = Player(2)
    player1.place_piece(point00)
    assert player1.id() == 1
    assert player1.occupied()[0].coord() == (0, 0)
    assert player1._points == 0
    assert player2._points == 0
    assert player2._occupied == []


def test_point_class():
    player1 = Player(1, [(0, 0), (1, 0)])
    player2 = Player(2)

# def test_point_class():
#     player1 = Player()
#     point_list = [Point((0,0),[(0,3),(1,1), (3,0)], True, player1)]
