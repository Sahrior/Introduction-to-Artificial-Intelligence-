import copy

foo = [1,2,[]]

#bar = foo.copy()
#bar[-1].append(5)
#bar.append(5)


bar = copy.deepcopy(foo)
bar[-1].append(5)



print(foo, bar, '\n')

