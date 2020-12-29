number = int(input("Enter line : "))
line = number - 1

for x in range(number):
    space = ""
    star = ""
    for i in range(line):
        space += " "
    line -= 1
    for y in range(x+1):
        star += '*'
        if star == '*':
            continue
        else:
            star += '*'
    print(space+star)


# Test logic star each line
# for i in range(5):
#     star = ''
#     for y in range(i+1):
#         star += '*'
#         if star == '*':
#             continue
#         else:
#             star += "*"
#     print(star)



"""
        *
       ***
      *****
     *******
    *********
"""

