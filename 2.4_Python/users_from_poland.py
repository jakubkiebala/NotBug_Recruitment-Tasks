users = [
    {'name': 'Kamil', 'country': 'Poland'},
    {'name': 'John', 'country': 'USA'},
    {'name': 'Yeti'},
]


def new_list_with_polish_users(user_list):
    """
    Filters the list of users and returns only those from Poland.

    Args:
        user_list (list): A list of dictionaries, each representing a user with keys like 'name' and 'country'.

    Returns:
        list: A list containing users from Poland (if the 'country' key exists and equals 'Poland').
    """
    new_list = [user for user in user_list if user.get('country') == 'Poland']
    return new_list


print(new_list_with_polish_users(users))
