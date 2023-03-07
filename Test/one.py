import os

div_result = int(input()) / int(input())

file = open('division_result.txt', 'w', encoding='utf-8')
file.write(str(div_result))
file.close()


