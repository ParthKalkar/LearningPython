from itertools import product, islice
 
 
def expression(p):
    return "{}1{}2{}3{}4{}5{}6{}7{}8{}9".format(*p)
 
 
def gen_expression():
    op = ['+', '-', '']
    return [expression(p) for p in product(op, repeat=9) if p[0] != '+']
 
 
def all_expressions():
    values = {}
    for expression in gen_expression():
        val = eval(expression)
        if val not in values:
            values[val] = 1
        else:
            values[val] += 1
    return values
 
 
def sum_till_100(val):
    for s in filter(lambda x: x[0] == val, map(lambda x: (eval(x), x), gen_expression())):
        print(s)
 
 
def max_sol():
    print("Sum {} has the maximum number of solutions = {}".
          format(*max(all_expressions().items(), key=lambda x: x[1])))
 

 
sum_till_100(100)
max_sol()


