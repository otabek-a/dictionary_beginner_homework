def find_max_value(data: dict):
    """
    Return the maximum int or float value in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The maximum value in the dictionary.
    """
    l=[]
    for i in data.values():
        l.append(i)
    max=l[0]
    for i in l:
        if max<i:
            max=i
    return max




result=find_max_value({
    1:  10000,
    2: 23456789,
    3: 689899899773
  })
print(result)