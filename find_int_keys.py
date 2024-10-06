def find_int_keys(data: dict) -> list:
    """
    Return a list of all keys in a dictionary that are integers.
    Args:
        data (dict): A dictionary of values
    Returns:
        list: A list of all keys in the dictionary that are integers.
    """
    a=data.keys()
    b=[]
    res=[]
    for i in a:
        b.append(i)
    for i in b:
        if type(i)==type(12):
            res.append(i)
    return res
result=find_int_keys({
    'a': 1, 
    3 : 2, 
    'c': 3,
    10:'a'
  })
print(result)