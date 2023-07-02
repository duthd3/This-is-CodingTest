data = input()
new_str = []
num = 0

for i in data:
    if 65 <= ord(i) and ord(i) <= 90:
        new_str.append(i)
    else:
       num += int(i)     
new_str.sort()
if num != 0:
    new_str.append(str(num))

print(''.join(new_str))


