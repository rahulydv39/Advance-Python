# lambda arguments : expression

add10 = lambda x: x + 10
print(add10(5))

# to multiply also

mult = lambda x, y : x*y
print(mult(2,4))


### map function (fun, seq)
a = [1,2,3,4,5]
b = map(lambda x: x*2 , a)
print(list(b))