with open('input.txt','r') as f:
    a=f.read()
    a=a.split('\n')
    a=list(a)
print("lista 2:",sorted(a))