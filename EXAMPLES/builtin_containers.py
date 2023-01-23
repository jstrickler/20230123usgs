alist = ['alpha', 'beta', 'gamma', 'eta', 'zeta']
atuple = ('123 Elm Street', 'Toledo', 'Ohio')
adict = {'alpha': 5, 'beta': 10, 'gamma': 15}
aset = {'alpha', 'beta', 'gamma', 'eta', 'zeta'}

print(alist[0], atuple[0], adict['alpha'])
print(alist[-1], atuple[-1])
print(alist[:3], alist[3:], alist[2:5], alist[-2:])
print('alpha' in alist, 'Ohio' in atuple, 'gamma' in adict, 'zeta' in aset)
print(len(alist), len(atuple), len(adict), len(aset))
print(alist.count('alpha'), atuple.count('Ohio'))
