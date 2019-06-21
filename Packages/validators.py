import re
def phoneNumberValidatior(number):
    pattern = ' ^[6-9][0-9]{9}$ | ^[0][6-9][0-9]{9}$ | ^[+][9][1][6-9][0-9]'
    if re.match(pattern,str(number)):
            return True
    return False
phoneNumberValidatior(9332940846)


def EmailValidator(email):
    pattern = '[0-9a-z][0-9a-z_.]{4,13}[0-9a-z][@][0-9a-z]{3,18}[.][0-9a-z][a-z]{2,4}$'
    if re.match(pattern,email):
        return True
    return False
emailValidator("psd487@gmail.com")
    