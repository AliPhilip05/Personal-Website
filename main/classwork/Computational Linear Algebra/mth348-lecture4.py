# Markov chain review 
def f(x):
    if x <= 1/2:
        return x * 2
    if x > 1/2:
        return 2*x - 1
    
x = 1/10
for i in range(80):
    print(x)
    x = f(x)