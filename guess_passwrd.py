import time
from subprocess import call


def guess_passwrd():
    """Guesses the password for a given website."""
    call("clear")
    print()
    username = input('Username > ')
    target_website = input('Target Webpage Link > ')
    print()
    print(f"$ python ./tools/login_guess.py -u {username} -t {target_website}")
    print()
    try:
        call(f"python ./tools/login_guess.py -u {username} -t {target_website}", shell=True)
    except KeyboardInterrupt:
        time.sleep(1)
