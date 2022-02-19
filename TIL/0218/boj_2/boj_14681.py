dot_x = int(input())
dot_y = int(input())

if dot_x > 0 and dot_y > 0:
    print('1')
elif dot_x < 0 and dot_y > 0:
    print('2')
elif dot_x < 0 and dot_y < 0:
    print('3')
elif dot_x > 0 and dot_y < 0:
    print('4')
