import random
import string


def account_ID(size=20, chars=string.ascii_uppercase + string.digits):
    return 'User_' + ''.join(random.choice(chars) for _ in range(size))
