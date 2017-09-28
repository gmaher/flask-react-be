import bcrypt

def hash_password(pw, rounds=10):
    """
    Uses the bcrypt algorithm to generate a salt and hash a password
    NOTE: ONLY PASSWORDS < 72 CHARACTERS LONG!!!!

    :param pw: (required) password to hash
    :param rounds: number of rounds the bcrypt algorithm will run for
    """
    if not type(pw) == str:
        raise RuntimeError('password {} is not a string!'.format(pw))

    if len(pw) >= 72:
        raise RuntimeError('password {} has length {} > 72!'.format(pw,len(pw)))

    return bcrypt.hashpw(pw,bcrypt.gensalt(rounds))


def pw_is_valid(pw,hashed_pw):
    """
    compare the entered password to the hashed one and see if they match up

    :param pw: (required) password entered by user
    :param hashed_pw: (required) the hashed password we stored in the database
    """
    if not type(pw) == str: return False

    if len(hashed_pw) != 60: return False
    
    return bcrypt.checkpw(pw,hashed_pw)
