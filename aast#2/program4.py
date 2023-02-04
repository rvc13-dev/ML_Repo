def unique_list(vals):
    x =[]
    for a in vals:
        if a not in x:
            x.append(a)
    return x


print(unique_list([1,2,3,3,3,3,4,5]))