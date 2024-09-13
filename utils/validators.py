
def fullname_validator(fullname) -> bool:
    """ userni to'liq ismini olib uni yaroqli yoki yaroqsiz ekanligini tekshiradi

    Args:
        fullname (string): userni to'liq ismi. misol uchun -> 'Muhiddin Kabraliv'

    Returns:
        bool: True - yaroqli, False - yaroqsiz
    """
    fullname = fullname.split(' ')

    if len(fullname) < 1:
        return False
    
    username = fullname[0]
    first_name = fullname[0]

    if not username.isalpha():
        return False
    
    if not first_name.isalpha():
        return False
    
    return True
    