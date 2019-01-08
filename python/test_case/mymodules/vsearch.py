# def search4vowels(word):
#     """Возвращает гласные, найденные в указанном слове."""
#     vowels = set('aeiou')
#     found = vowels.intersection(set(word))
#     return bool(found)

def search4vowels(phrase: str) -> set:
    """Возвращает гласные, найденные в указанном слове."""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))

def search4letters(phrase: str, letters: str) -> set:
#def search4letters(phrase: str, letters: str = 'aeiou' ) -> set:
    """Возвращает множество букв из 'letters', найденныx в указанном слове."""
    return set(letters).intersection(set(phrase))

# создание функций