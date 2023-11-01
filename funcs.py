def is_palindrome(sentence: str) -> bool:
    """Permite conocer si un string es, o no, un palindromo.

    Args:
        sentence (str): String a evaluar.

    Returns:
            bool: True or False.
        

    """

    sentence = sentence.lower().replace(' ', '')
    return sentence == sentence[::-1]