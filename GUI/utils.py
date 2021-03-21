import unicodedata


def NFD(text):
    return unicodedata.normalize('NFD', text)


def canonical_caseless(text):
    return NFD(NFD(text).casefold())


def caseless_equal(left, right):
    return canonical_caseless(left) == canonical_caseless(right)
