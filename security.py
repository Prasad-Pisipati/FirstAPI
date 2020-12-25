from user import user
users = [{
    'id': 1,
    'username': 'prasad',
    'password': 'welcome123'},
    {
        'id': 2,
        'username': 'ahalya',
        'password': 'welcome789'}
]

username_mapping = {'prasad': {
    'id': 1,
    'username': 'prasad',
    'password': 'welcome123'
}
}

userid_mapping = {1: {
    'id': 1,
    'username': 'prasad',
    'password': 'welcome123'
}
}


def authenticate(username, password):
    user = username_mapping.get(username)
    if user['password'] == 'welcome123':
       return ("authorized")
    else:
       return ("Un-authorized")


def identity(payload):
    userid = payload('identity')
    return UserModel.find_by_id(userid)
