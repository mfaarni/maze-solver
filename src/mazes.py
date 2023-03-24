

def maze():
    maze_8x8=[
    "XXXGXXXX-0",
    "X      X-1",
    "X XXXX X-2",
    "X X    X-3",
    "X X X  X-4",
    "X   X  X-5",
    "XXX X XX-6",
    "XXXXXSXX-7"
    ]

    return maze_8x8

for i in maze():
    print(i)