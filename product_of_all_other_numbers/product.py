def my_function(arg):
    # write the body of your function here
    result = []
    for i in range(0,len(arg)):
        curr = 1
        for j in range(0,len(arg)):
            if i is j:
                continue
            else:
                print("current is ",curr)
                curr *= arg[j]
        result.append(curr)
    return 'running with %s' % result

# run your function through some test cases here
# remember: debugging is half the battle!
x =[1,7,3,4]
print(my_function(x))