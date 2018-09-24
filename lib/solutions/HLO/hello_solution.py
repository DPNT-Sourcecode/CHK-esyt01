

# noinspection PyUnusedLocal
# friend_name = unicode string
def hello(friend_name):
    if friend_name is not None or friend_name != '':
        return 'Hello, %s' % friend_name
    else:
        return 'Hello, World!'
