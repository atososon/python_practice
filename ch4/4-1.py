guess_me = 7
if guess_me < 7 :
    print("too low")
elif guess_me > 7 :
    print("too high")
else :
    print("just right")

start = 1
while True:
    if(start < guess_me):
        print("too low")
    elif(start == guess_me):
        print("found it!")
    else:
        print("oops")
        break
    start+=1
