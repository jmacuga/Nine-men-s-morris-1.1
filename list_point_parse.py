import json
modes = [
    [
        [(0, 0), [[0, 3], [1, 1], [3, 0]]],
        [(0, 3), [[1, 3], [0, 0], [0, 6]]],
        [(0, 6), [[0, 3], [1, 5], [3, 6]]],
        [(1, 1), [[0, 0], [1, 3], [3, 1], [2, 2]]],
        [(1, 3), [[0, 3], [1, 1], [1, 5], [2, 3]]],
        [(1, 5), [[0, 6], [1, 3], [3, 5], [2, 4]]],
        [(2, 2), [[2, 3], [1, 1], [3, 2]]],
        [(2, 3), [[2, 2], [1, 3], [2, 4]]],
        [(2, 4), [[2, 3], [3, 4], [1, 5]]],
        [(3, 0), [[0, 0], [6, 0], [3, 1]]],
        [(3, 1), [[3, 0], [1, 1], [5, 1], [3, 2]]],
        [(3, 2), [[2, 2], [3, 1], [4, 2]]],
        [(3, 4), [[2, 4], [3, 5], [4, 4]]],
        [(3, 5), [[3, 4], [3, 6], [1, 5], [5, 5]]],
        [(3, 6), [[3, 5], [0, 6], [6, 6]]],
        [(4, 2), [[3, 2], [5, 1], [4, 3]]],
        [(4, 3), [[4, 2], [5, 3], [4, 4]]],
        [(4, 4), [[4, 3], [3, 4], [5, 5]]],
        [(5, 1), [[4, 2], [3, 1], [6, 0], [5, 3]]],
        [(5, 3), [[5, 1], [4, 3], [5, 5], [6, 3]]],
        [(5, 5), [[5, 3], [4, 4], [3, 5], [6, 6]]],
        [(6, 0), [[3, 0], [6, 3], [5, 1]]],
        [(6, 3), [[6, 0], [5, 3], [6, 6]]],
        [(6, 6), [[6, 3], [5, 5], [3, 6]]]
    ],
    [
        [(0, 0), [[0, 3], [3, 0]]],
        [(0, 3), [[1, 3], [0, 0], [0, 6]]],
        [(0, 6), [[0, 3], [3, 6]]],
        [(1, 1), [[1, 3], [3, 1]]],
        [(1, 3), [[0, 3], [1, 1], [1, 5], [2, 3]]],
        [(1, 5), [[1, 3], [3, 5]]],
        [(2, 2), [[2, 3], [3, 2]]],
        [(2, 3), [[2, 2], [1, 3], [2, 4]]],
        [(2, 4), [[2, 3], [3, 4]]],
        [(3, 0), [[0, 0], [6, 0], [3, 1]]],
        [(3, 1), [[3, 0], [1, 1], [5, 1], [3, 2]]],
        [(3, 2), [[2, 2], [3, 1], [4, 2]]],
        [(3, 4), [[2, 4], [3, 5], [4, 4]]],
        [(3, 5), [[3, 4], [3, 6], [1, 5], [5, 5]]],
        [(3, 6), [[3, 5], [0, 6], [6, 6]]],
        [(4, 2), [[3, 2], [4, 3]]],
        [(4, 3), [[4, 2], [5, 3], [4, 4]]],
        [(4, 4), [[4, 3], [3, 4]]],
        [(5, 1), [[3, 1], [5, 3]]],
        [(5, 3), [[5, 1], [4, 3], [5, 5], [6, 3]]],
        [(5, 5), [[5, 3], [3, 5]]],
        [(6, 0), [[3, 0], [6, 3]]],
        [(6, 3), [[6, 0], [5, 3], [6, 6]]],
        [(6, 6), [[6, 3], [3, 6]]],
    ],
    [
        ((0, 0), [(2, 0), (0, 2)]),
        ((0, 2), [(0, 0), (0, 4), (1, 2)]),
        ((0, 4), [(0, 2), (2, 4)]),
        ((1, 1), [(1, 2), (2, 1)]),
        ((1, 2), [(1, 1), (1, 3), (0, 2)]),
        ((1, 3), [(1, 2), (2, 3)]),
        ((2, 0), [(0, 0), (4, 0), (2, 1)]),
        ((2, 1), [(2, 0), (1, 1), (3, 1)]),
        ((2, 3), [(1, 3), (2, 4), (3, 3)]),
        ((2, 4), [(2, 3), (0, 4), (4, 4)]),
        ((3, 1), [(3, 2), (2, 1)]),
        ((3, 2), [(3, 1), (3, 3), (4, 2)]),
        ((3, 3), [(3, 2), (2, 3)]),
        ((4, 0), [(4, 2), (2, 0)]),
        ((4, 2), [(4, 0), (3, 2), (4, 4)]),
        ((4, 4), [(4, 2), (2, 4)])
    ],

    [
        ((0, 0), [(0, 1), (1, 0), (1, 1)]),
        ((0, 1), [(0, 0), (1, 1), (0, 2)]),
        ((0, 2), [(0, 1), (1, 2), (1, 1)]),
        ((1, 0), [(0, 0), (2, 0), (1, 1)]),
        ((1, 1), [(0, 0), (1, 0), (2, 0), (0, 1),
                  (2, 1), (0, 2), (1, 2), (2, 2)]),
        ((1, 2), [(0, 2), (2, 2), (1, 1)]),
        ((2, 0), [(2, 1), (1, 0), (1, 1)]),
        ((2, 1), [(2, 2), (2, 0), (1, 1)]),
        ((2, 2), [(2, 1), (1, 2), (1, 1)])
    ]
]





# make_points()
# openpoint()


def points_dump():
    with open("mode_points.json", "r+") as fp:
        modes_keys = ['4', "3", "2", "1"]
        modes_dict = {}
        for points_list, name in zip(modes, modes_keys):
            new_points_list =[]
            for point in points_list:
                new_points_list.append({"id" : point[0], "connected_p": point[1]})
            modes_dict[name] = new_points_list
        json.dump(modes_dict, fp, indent = 4)

points_dump()

# def pointtrans():
#     new_modes = []
#     new_points_list = []
#     for points_list in modes:
#         transpoints_list = []
#         for point in points_list:
#             posbl_mov = [list(element) for element in point[1]]
#             new_point = [list(point[0]), posbl_mov]
#             transpoints_list.append(new_point)
#         new_points_list.append(transpoints_list)
#     new_modes.append(new_points_list)
#     print(new_modes)


# pointtrans()

new_modes = [
    [
        [
            [[0, 0], [[0, 3], [1, 1], [3, 0]]],
            [[0, 3], [[1, 3], [0, 0], [0, 6]]],
            [[0, 6], [[0, 3], [1, 5], [3, 6]]],
            [[1, 1], [[0, 0], [1, 3], [3, 1], [2, 2]]],
            [[1, 3], [[0, 3], [1, 1], [1, 5], [2, 3]]],
            [[1, 5], [[0, 6], [1, 3], [3, 5], [2, 4]]],
            [[2, 2], [[2, 3], [1, 1], [3, 2]]],
            [[2, 3], [[2, 2], [1, 3], [2, 4]]],
            [[2, 4], [[2, 3], [3, 4], [1, 5]]],
            [[3, 0], [[0, 0], [6, 0], [3, 1]]],
            [[3, 1], [[3, 0], [1, 1], [5, 1], [3, 2]]],
            [[3, 2], [[2, 2], [3, 1], [4, 2]]],
            [[3, 4], [[2, 4], [3, 5], [4, 4]]],
            [[3, 5], [[3, 4], [3, 6], [1, 5], [5, 5]]],
            [[3, 6], [[3, 5], [0, 6], [6, 6]]],
            [[4, 2], [[3, 2], [5, 1], [4, 3]]],
            [[4, 3], [[4, 2], [5, 3], [4, 4]]],
            [[4, 4], [[4, 3], [3, 4], [5, 5]]],
            [[5, 1], [[4, 2], [3, 1], [6, 0], [5, 3]]],
            [[5, 3], [[5, 1], [4, 3], [5, 5], [6, 3]]],
            [[5, 5], [[5, 3], [4, 4], [3, 5], [6, 6]]],
            [[6, 0], [[3, 0], [6, 3], [5, 1]]],
            [[6, 3], [[6, 0], [5, 3], [6, 6]]],
            [[6, 6], [[6, 3], [5, 5], [3, 6]]]
        ],
        [
            [[0, 0], [[0, 3], [3, 0]]],
            [[0, 3], [[1, 3], [0, 0], [0, 6]]],
            [[0, 6], [[0, 3], [3, 6]]],
            [[1, 1], [[1, 3], [3, 1]]],
            [[1, 3], [[0, 3], [1, 1], [1, 5], [2, 3]]],
            [[1, 5], [[1, 3], [3, 5]]],
            [[2, 2], [[2, 3], [3, 2]]],
            [[2, 3], [[2, 2], [1, 3], [2, 4]]],
            [[2, 4], [[2, 3], [3, 4]]],
            [[3, 0], [[0, 0], [6, 0], [3, 1]]],
            [[3, 1], [[3, 0], [1, 1], [5, 1], [3, 2]]],
            [[3, 2], [[2, 2], [3, 1], [4, 2]]],
            [[3, 4], [[2, 4], [3, 5], [4, 4]]],
            [[3, 5], [[3, 4], [3, 6], [1, 5], [5, 5]]],
            [[3, 6], [[3, 5], [0, 6], [6, 6]]],
            [[4, 2], [[3, 2], [4, 3]]],
            [[4, 3], [[4, 2], [5, 3], [4, 4]]],
            [[4, 4], [[4, 3], [3, 4]]],
            [[5, 1], [[3, 1], [5, 3]]],
            [[5, 3], [[5, 1], [4, 3], [5, 5], [6, 3]]],
            [[5, 5], [[5, 3], [3, 5]]],
            [[6, 0], [[3, 0], [6, 3]]],
            [[6, 3], [[6, 0], [5, 3], [6, 6]]],
            [[6, 6], [[6, 3], [3, 6]]]
        ],
        [
            [[0, 0], [[2, 0], [0, 2]]],
            [[0, 2], [[0, 0], [0, 4], [1, 2]]],
            [[0, 4], [[0, 2], [2, 4]]],
            [[1, 1], [[1, 2], [2, 1]]],
            [[1, 2], [[1, 1], [1, 3], [0, 2]]],
            [[1, 3], [[1, 2], [2, 3]]],
            [[2, 0], [[0, 0], [4, 0], [2, 1]]],
            [[2, 1], [[2, 0], [1, 1], [3, 1]]],
            [[2, 3], [[1, 3], [2, 4], [3, 3]]],
            [[2, 4], [[2, 3], [0, 4], [4, 4]]],
            [[3, 1], [[3, 2], [2, 1]]],
            [[3, 2], [[3, 1], [3, 3], [4, 2]]],
            [[3, 3], [[3, 2], [2, 3]]],
            [[4, 0], [[4, 2], [2, 0]]],
            [[4, 2], [[4, 0], [3, 2], [4, 4]]],
            [[4, 4], [[4, 2], [2, 4]]]
        ],
        [
            [[0, 0], [[0, 1], [1, 0], [1, 1]]],
            [[0, 1], [[0, 0], [1, 1], [0, 2]]],
            [[0, 2], [[0, 1], [1, 2], [1, 1]]],
            [[1, 0], [[0, 0], [2, 0], [1, 1]]],
            [[1, 1], [[0, 0], [1, 0], [2, 0], [0, 1], [2, 1], [0, 2], [1, 2], [2, 2]]],
            [[1, 2], [[0, 2], [2, 2], [1, 1]]],
            [[2, 0], [[2, 1], [1, 0], [1, 1]]],
            [[2, 1], [[2, 2], [2, 0], [1, 1]]],
            [[2, 2], [[2, 1], [1, 2], [1, 1]]]
        ]
    ]
]

# with open("points_list.json", 'r') as file_handle:
#     data = json.load(file_handle)
#     for point_list in data:
#         for point in point_list:
#             print(point['id'])
