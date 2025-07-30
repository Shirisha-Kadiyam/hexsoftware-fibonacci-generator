def my_generator():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
gen=my_generator()
print(gen) 
print(next(gen))
for _ in range(30):
    print(next(gen))
