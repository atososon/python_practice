import time
fmt = "%Y-%m-%d\n"
with open('today.txt','rt') as input:
    today_string = input.read()
print(time.strptime(today_string,fmt))