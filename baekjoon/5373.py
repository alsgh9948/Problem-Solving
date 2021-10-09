# from sys import stdin
#
# input = stdin.readline
#
# tc = int(input())
#
# def solv():
#     for _ in range(tc):
#         cube = set_cube()
#         n = int(input())
#         ops = list(input().split())
#         for op in ops:
#             rotate_cube(op,cube)
#         print(cube['U'])
# def rotate_cube(op,cube):
#     target = op[0]
#     dir = op[1]
#
#     cube[target] = rotate(cube[target], dir)
#     tmp = ['','','']
#     if target == 'U':
#         tmp[0],tmp[1],tmp[2] = cube['L'][0][2],cube['L'][1][2],cube['L'][2][2]
#         cube['L'][0][2],cube['L'][1][2],cube['L'][2][2] = cube['B'][2][0],cube['B'][2][1],cube['B'][2][2]
#         cube['B'][2][0],cube['B'][2][1],cube['B'][2][2] = cube['R'][0][0],cube['R'][1][0],cube['R'][2][0]
#         cube['R'][0][0],cube['R'][1][0],cube['R'][2][0] = cube['F'][0][0],cube['F'][0][1],cube['F'][0][2]
#         cube['F'][0][0],cube['F'][0][1],cube['F'][0][2] = tmp[0],tmp[1],tmp[2]
#     elif target == 'R':
#         tmp[0],tmp[1],tmp[2] = cube['D'][0][2],cube['D'][1][2],cube['D'][2][2]
#         cube['D'][0][2],cube['D'][1][2],cube['D'][2][2] = cube['F'][0][2],cube['F'][1][2],cube['F'][2][2]
#         cube['F'][0][2],cube['F'][1][2],cube['F'][2][2] = cube['U'][0][2],cube['U'][1][2],cube['U'][2][2]
#         cube['U'][0][2],cube['U'][1][2],cube['U'][2][2] = cube['B'][0][2],cube['B'][1][2],cube['B'][2][2]
#         cube['B'][0][2],cube['B'][1][2],cube['B'][2][2] = tmp[0],tmp[1],tmp[2]
#     elif target == 'L':
#         tmp[0],tmp[1],tmp[2] = cube['D'][0][0],cube['D'][1][0],cube['D'][2][0]
#         cube['D'][0][0],cube['D'][1][0],cube['D'][2][0] = cube['F'][0][0],cube['F'][1][0],cube['F'][2][0]
#         cube['F'][0][0],cube['F'][1][0],cube['F'][2][0] = cube['U'][0][0],cube['U'][1][0],cube['U'][2][0]
#         cube['U'][0][0],cube['U'][1][0],cube['U'][2][0] = cube['B'][0][0],cube['B'][1][0],cube['B'][2][0]
#         cube['B'][0][0],cube['B'][1][0],cube['B'][2][0] = tmp[0],tmp[1],tmp[2]
#     elif target == 'B':
#         tmp[0],tmp[1],tmp[2] = cube['U'][0][0],cube['U'][0][1],cube['U'][0][2]
#         cube['U'][0][0],cube['U'][0][1],cube['U'][0][2] = cube['L'][0][0],cube['L'][0][1],cube['L'][0][2]
#         cube['L'][0][0],cube['L'][0][1],cube['L'][0][2] = cube['D'][2][0],cube['D'][2][1],cube['D'][2][2]
#         cube['D'][2][0],cube['D'][2][1],cube['D'][2][2] = cube['R'][0][0],cube['R'][0][1],cube['R'][0][2]
#         cube['R'][0][0],cube['R'][0][1],cube['R'][0][2] = tmp[0],tmp[1],tmp[2]
#     elif target == 'F':
#         tmp[0],tmp[1],tmp[2] = cube['U'][0][0],cube['U'][0][1],cube['U'][0][2]
#         cube['U'][2][0],cube['U'][2][1],cube['U'][2][2] = cube['L'][0][2],cube['L'][1][2],cube['L'][2][2]
#         cube['L'][0][2],cube['L'][1][2],cube['L'][2][2] = cube['D'][0][0],cube['D'][0][1],cube['D'][0][2]
#         cube['D'][0][0],cube['D'][0][1],cube['D'][0][2] = cube['R'][2][0],cube['R'][2][1],cube['R'][2][2]
#         cube['R'][2][0],cube['R'][2][1],cube['R'][2][2] = tmp[0],tmp[1],tmp[2]
#     elif target == 'D':
#         tmp[0],tmp[1],tmp[2] = cube['F'][2][0],cube['F'][2][1],cube['F'][2][2]
#         cube['F'][2][0],cube['F'][2][1],cube['F'][2][2] = cube['R'][2][2],cube['R'][1][2],cube['R'][0][2]
#         cube['R'][2][2],cube['R'][1][2],cube['R'][0][2] = cube['B'][0][0],cube['B'][0][1],cube['B'][0][2]
#         cube['B'][0][0],cube['B'][0][1],cube['B'][0][2] = cube['L'][0][0],cube['L'][1][0],cube['L'][2][0]
#         cube['L'][2][0],cube['L'][1][0],cube['L'][0][0] = tmp[0],tmp[1],tmp[2]
#
# def rotate(board,dir):
#     tmp = []
#     for x in range(3):
#         row = []
#         for y in range(3):
#             row.append(board[x][y])
#         tmp.append(row)
#     print(board,dir)
#     if dir == '+':
#         for x in range(3):
#             for y in range(3):
#                 board[y][2-x] = tmp[x][y]
#     else:
#         for x in range(3):
#             for y in range(3):
#                 board[2-y][x] = tmp[x][y]
#     return board
# def set_cube():
#     cube = {}
#     cube['U'] = [['w']*3 for _ in range(3)]
#     cube['D'] = [['y']*3 for _ in range(3)]
#     cube['F'] = [['r']*3 for _ in range(3)]
#     cube['B'] = [['o']*3 for _ in range(3)]
#     cube['L'] = [['g']*3 for _ in range(3)]
#     cube['R'] = [['b']*3 for _ in range(3)]
#     return cube
#
# solv()

