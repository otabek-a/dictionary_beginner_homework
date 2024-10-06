def sum_age_values(data:list) -> int:
    """
    Return the sum of all age values in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The sum of all age values in the dictionary
    """
    res=0
    for i in data:
        if 'age' in i:
            res+=i['age']
    return res
   


result=sum_age_values([
  {
    'name': 'John', 
    'age': 27
  }, 
  {
    'name': 'Mary', 
    'age': 42
  }
])
print(result)