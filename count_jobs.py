def count_jobs(data: list, job: str) -> int:
    """
    Return the number of users with a given job

    Args:
        data (list): A list of dictionaries containing user data
        job (str): The job to search for
    Returns:
        int: The number of users with the given job
    """
    count = 0  # Initialize count variable
    for user in data:
        if user['job'] == job:  # Access the 'job' key
            count += 1  # Increment count
    return count

# Example usage
result = count_jobs([
    {
        'name': 'John', 
        'job': 'Developer'
    }, 
    {
        'name': 'Mary', 
        'job': 'Developer'
    }
], 'Developer')

print(result)  # This should output 2
