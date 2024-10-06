def get_min_age_user_name(data:list) -> str:
    """
    Return the name of the user with the minimum age in a dictionary.

    Args:
        data (dict): A dictionary of values
    Returns:
        str: The name of the user with the minimum age in the dictionary
    """
    name=[]
    age=[]
    for i in data:
        name.append(i['name'])
        age.append(i['age'])
    
    max=age[0]
    for i in age:
        if max>i:
            max=i
    
    index=age.index(max)
    return name[index]



result= get_min_age_user_name([
  {
    'name': 'John', 
    'age': 32
  }, 
  {
    'name': 'Mary', 
    'age': 18
  }, 
  {
    'name': 'Ann', 
    'age': 20
  },
  {
    'name': 'Ban', 
    'age': 29
  }
])
print('The Younger is')
print(result)