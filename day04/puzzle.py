from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def is_in_bounds(self, max_xy: tuple[int,int]) -> bool:
        return self.x < max_xy[0] and self.y < max_xy[1] and \
        self.x >= 0 and self.y >= 0

@dataclass
class Path:
    points: list[Point]

@dataclass
class Cross:
    center: Point
    paths: list[Path]

def get_paths_from(
    point: Point,
    max_xy: tuple[int, int],
    path_length: int = 4
) -> list[Path]:
    paths: list[Path] = []

    directions = [
        (0, -1), (0, 1), (-1, 0), (1, 0),  # orthogonal
        (-1, -1), (1, -1), (-1, 1), (1, 1)  # diagonal
    ]

    for dx, dy in directions:
        end_point = Point(point.x + ((path_length-1) * dx),
                         point.y + ((path_length-1) * dy))
        if end_point.is_in_bounds(max_xy):
            path_points = [
                point + Point(i * dx, i * dy)
                for i in range(path_length)
            ]
            paths.append(Path(path_points))

    return paths

def get_crosses_from(point: Point,
    max_xy: tuple[int, int],) -> list[Cross]:
    # get all possible cross endpoints from a point
    directions = {
        'orthoginal': [
            [(0,-1),(0,1)], # path 1 endpoints
            [(-1,0),(1,0)]  # path 2 endpoints
        ],
        'diagonal': [
            [(-1,-1),(1,1)], # path 1 endpoints
            [(1,-1),(-1,1)]  # path 2 endpoints
        ]
    }
    crosses: list[Cross] = []
    # for each direction in directions check each endpoint for
    # out of bounds and if all 4 points are inbounds,
    # create a cross and add it to the list of crosses
    for direction in directions.values():
        is_inbounds = True
        paths: list[Path] = []
        for endpoints in direction:
            p1 = point + Point(endpoints[0][0],endpoints[0][1])
            p2 = point
            p3 = point + Point(endpoints[1][0],endpoints[1][1])
            if p1.is_in_bounds(max_xy) and p3.is_in_bounds(max_xy):
                paths.append(Path([p1, p2, p3]))
            else:
                is_inbounds = False
        if is_inbounds:
            crosses.append(Cross(point, paths))
    return crosses

def print_matrix(
    matrix: list[list[str]],
    words: list[Path],
    max_xy: tuple[int,int]
) -> None:
    points: list[Point] = []
    for word in words:
        points.extend(word.points)
    # print the matrix using "." where xy is not in points
    for i in range(max_xy[1]):
        for j in range(max_xy[0]):
            if Point(i,j) in points:
                print(matrix[i][j], end="")
            else:
                print(".", end="")
        print()


with open('input.txt', 'r') as file:
    matrix = [list(line.strip()) for line in file.readlines()]
max_xy = (len(matrix[0]),len(matrix))

# Part 1
# Find all paths that spell XMAS
words: list[Path] = []
for i in range(max_xy[1]):
    for j in range(max_xy[0]):
        if matrix[i][j] == 'X':
            # print(f'Checking for XMAS at {j},{i}')
            for path in get_paths_from(Point(i,j), max_xy):
                # print(path)
                if matrix[path.points[1].x][path.points[1].y] == 'M' \
                and matrix[path.points[2].x][path.points[2].y] == 'A' \
                and matrix[path.points[3].x][path.points[3].y] == 'S':
                    # print(f"Found MAS at {j},{i}")
                    words.append(path)
print(f"Part 1: {len(words)}")

# Part 2
crosses = 0

VALID_PATTERNS = ["MMSS", "MSSM", "SSMM", "SMMS"]

for row in range(1, len(matrix) - 1):
    for col in range(1, len(matrix[0]) - 1):
        if matrix[row][col] != "A":
            continue
        corners = [
            matrix[row - 1][col - 1],  # top-left
            matrix[row - 1][col + 1],  # top-right
            matrix[row + 1][col + 1],  # bottom-right
            matrix[row + 1][col - 1]   # bottom-left
        ]
        corner_pattern = "".join(corners)
        if corner_pattern in VALID_PATTERNS:
            crosses += 1

print(f"Part 2: {crosses}")
