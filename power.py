def power(base, p):
    if p==0:
        return 1
    return power(base, p-1) * base
     

result = power(4,6)

print(result%3)

#added a new line