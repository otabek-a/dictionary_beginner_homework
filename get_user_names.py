def get_user_names(data:list, country:str) -> list:
    """
    Return a list of users with a given country

    Args:
        data (dict): A dictionary of values
        country (str): The country to search for
    Returns:
        list: A list of users with the given country
    """
    res=[]
    for i in data:
        if i['country']==country:
            res.append(i['name'])
    return res



result = get_user_names([
    {
        'name': 'John', 
        'country': 'USA'
    }, 
    {
        'name': 'Mary', 
        'country': 'UK'
    },
    {
        'name': 'Henry', 
        'country': 'UK'
    },
    {
        'name': 'Sam', 
        'country': 'MEX'
    },
    {
        'name': 'Kevin', 
        'country': 'RUS'
    },
    {
        'name': 'Dustin', 
        'country': 'GER'
    }
], "UK")
print(result)
