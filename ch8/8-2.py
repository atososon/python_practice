test1 = 'This is a test of the emergency text system'
with open('test.txt','rt') as infile:
    test2 = infile.read()
print(len(test2))
print(test1 == test2)