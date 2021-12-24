import re
data = input().strip()
if re.fullmatch("(100+1+|01)+",data):
    print('SUBMARINE')
else:
    print('NOISE')
