import itertools


def find_intersections(s1, s2):
    pairs = []
    for i, letter1 in enumerate(s1):
        for j, letter2 in enumerate(s2):
            if letter1 == letter2:
                if i > 0 and i < len(s1) - 1 and j > 0 and j < len(s2) - 1:
                    pairs.append([letter1, [i, j]])
    return pairs


def find_widths(s1, s2, s3):
    s1_s2_pairs = find_intersections(s1, s2)
    s1_s3_pairs = find_intersections(s1, s3)
    widths = []
    for pair1 in s1_s2_pairs:
        for pair2 in s1_s3_pairs:
            if abs(pair1[1][0] - pair2[1][0]) > 1:
                widths.append([abs(pair1[1][0] - pair2[1][0]), pair1, pair2])
    return sorted(widths, reverse=True)


def find_solutions(top, left, bottom, right):
    solutions = []
    for width1 in find_widths(top, left, right):
        for width2 in find_widths(bottom, left, right):
            # pep8 still yells at me if i make this multiline so idk
            if width1[0] == width2[0] and width2[1][1][1] - width1[1][1][1] == width2[2][1][1] - width1[2][1][1] and width1[1][1][0] < width1[2][1][0] - 1 and width1[2][1][1] < width2[2][1][1] - 1 and width2[1][1][0] < width2[2][1][0] - 1 and width1[1][1][1] < width2[1][1][1] - 1:
                solutions.append(
                    [width1[1], width1[2], width2[1], width2[2]])
    return solutions


def find_rectangles(s1, s2, s3, s4):
    rectangles = []
    for set in list(itertools.permutations([s1, s2, s3, s4])):
        solutions = find_solutions(set[0], set[1], set[2], set[3])
        if solutions:
            for solution in solutions:
                rectangles.append(solution)
    max_area = 0
    for r in rectangles:
        area = (r[1][1][0] - r[0][1][0] - 1) * (r[2][1][1] - r[0][1][1] - 1)
        if area > max_area:
            max_area = area
    return max_area


def iterate_molecules(string):
    molecules = string.split('\n')
    for i, m in enumerate(molecules):
        if not (i + 4) % 4:
            result = find_rectangles(
                molecules[i], molecules[i+1], molecules[i+2], molecules[i+3])
            print(result)


iterate_molecules("""CDBADCBBEFEF
DACCBADAFEAB
EFBDCAADBDCD
ABCDABCDABCD
DACCBADAFEAB
EFBDCAADBDCD
ABCDABCDABCD
CDBADCBBEFEF
ABABABABABAB
CDCDCDCDCDCD
EEEEEEEEEEEE
FFFFFFFFFFFF
ABAAAAAAAABA
CBCCCCCCCCBC
DBDDDDDDDDBD
EBEEEEEEEEBE
ABBBBBBBBBBA
ACCCCCCCCCCA
ADDDDDDDDDDA
AEEEEEEEEEEA
BBBABBBABBBB
CCACCCACCCCC
DDDDADDADDDD
EEAEEAEEEEEE""")

# test = find_rectangles('CHJDBJMHPJKD', 'OIMDIHEIAFNL',
#                        'KAINLHLOLBEJ', 'LCBJOJGIEKBO')
# print(test)
