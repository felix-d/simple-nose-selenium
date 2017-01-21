import os


def get_environ(var):
    env = os.environ.get(var, None)
    if env is None:
        raise TypeError('Environment variable {} needs to be set.'.format(var))
    return env
