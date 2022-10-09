
num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))

# ******************************
# Make your Code
# ******************************
num3 = []
check = True
stop = 0
length = len(num2) if len(num1) < len(num2) else len(num1)
for i in range(length):
    try:
        num3.append(num1[i])
        num3.append(num2[i])
    except:
        stop = i
        check = False
        break
if check:
    print(num3)
else:
    for i in range(stop,length,1):
        try:
            num3.append(num1[i])
        except:
            num3.append(num2[i])
    print(num3)
