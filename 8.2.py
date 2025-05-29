def flatten(tpl):
    flat_lst = []
    for element in tpl:
        if not isinstance(element, tuple):
            flat_lst.append(element)
        else:
            flat_lst += flatten(element)
    return flat_lst


nestedTuple = (5, (2, 5), ((1, 5), (4, 7)), (2, (4, 3)))

flattenTuple = flatten(nestedTuple)
print("The flattened tuple : " + str(flattenTuple))
