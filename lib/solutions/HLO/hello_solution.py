

# noinspection PyUnusedLocal
# friend_name = unicode string
def hello(friend_name=None):
    if friend_name is not None and friend_name != '':
        return 'Hello, %s!' % friend_name
    else:
        return 'Hello, World!'
