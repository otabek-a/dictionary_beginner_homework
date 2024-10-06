def get_user_country(data:list, name:str) -> list:
    """
    Return the country of a user with a given name

    Args:
        data (dict): A dictionary of values
        name (str): The name of the user to search for
    Returns:
        str: The country of the user with the given name
    """
    for i in data:
        if i['name']==name:
            return i['country']

result=get_user_country([
  {
    'name': 'John', 
    'country': 'uzb'
  }, 
  {
    'name': 'Mary', 
    'country': 'UK'
  }
],'John')
print(result)