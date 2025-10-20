import unicodedata


def normalizar_cadena(cadena):
    s_decomposed = unicodedata.normalize('NFD', cadena)
    s_filtered = ''.join(
        c for c in s_decomposed if unicodedata.category(c) != 'Mn')
    return s_filtered.lower()
