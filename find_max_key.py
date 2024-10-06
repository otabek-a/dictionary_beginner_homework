def find_max_key(data: dict):
    """
    Return the maximum int or float key in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The maximum key in the dictionary.
    """
    l=[]
    for i in data.keys():
        l.append(i)
    max=l[0]
    for i in l:
        if max<i:
            max=i
    return max




result=find_max_key({
    1: 'a', 
    2: 'b', 
    3: 'c'
  })
print(result)