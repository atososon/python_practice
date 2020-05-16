test1 = 'This is a test of the emergency text system'
with open('test.txt','wt') as outfile:
    outfile.write(test1)
print(len(test1))