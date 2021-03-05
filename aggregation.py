class Guitar:
    def __init__(self, guitar_type, strings):
        self.guitar_type = guitar_type
        self.strings = strings


class GuitarString:
    def __init__(self, string_tone):
        self.string_tone = string_tone


string_A = GuitarString('A')
string_E = GuitarString('E')
string_G = GuitarString('G')
string_C = GuitarString('C')

guitar_strings = [string_A, string_E, string_G, string_C]
guitar = Guitar('ukulele', guitar_strings)
