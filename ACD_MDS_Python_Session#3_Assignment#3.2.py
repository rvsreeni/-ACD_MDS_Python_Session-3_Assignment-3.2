# Program myreduce 
S = [x for x in 'ACADGILD']
print(S)
lst = ['x', 'y', 'z']
S = [l*i for l in lst for i in range(1,5)]
print(S)
S = [l*i for i in range(1,5) for l in lst]
print(S)
S = [ [[i+1], [i+2], [i+3]] for i in range(1,4) ]
print(S)
S = [ [i+1, i+2, i+3, i+4] for i in range(1,5) ]
print(S)
S = [ (j, i) for i in range(1,4) for j in range(1,4)]
print(S)