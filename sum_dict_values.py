def sum_dict_values(data: dict) -> int:
    '''
    Return the sum of all values in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The sum of all values in the dictionary
    '''
    sum=0
    for i in data.keys():
        sum+=data[i]
    return sum

result=sum_dict_values({
    1: 23, 
    2: 3.5, 
    4: 1, 
    6: 7, 
    5: 2, 
    7: 3
  })
print(result)