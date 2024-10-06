def count_users_with_age(data:list, age:int) -> int:
    """
    Return the number of users with a given age

    Args:
        data (dict): A dictionary of values
        age (int): The age to search for
    Returns:
        int: The number of users with the given age
    """
    count = 0  
    for user in data:
        if user['age'] == age: 
            count += 1  
    return count


result = count_users_with_age([
    {
        'name': 'John', 
        'age':28
    }, 
    {
        'name': 'Mary', 
        'age':28
    }
], 28)

print(result)  