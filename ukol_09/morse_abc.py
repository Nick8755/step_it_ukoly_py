alphabet = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    ' ': ' ',
}

alphabet_reverse = {value: key for key, value in alphabet.items()}


class Morse:
    def encode(self, text):
        """ implementuji metodu encode """
        words = text.split(' ') # rozdělíme text na slova
        encode_words = []
        for word in words:
            morse_ch = [alphabet[ch] for ch in word] # převedeme slovo na pismena v morseovce
            encode_words.append(' '.join(morse_ch)) # pismena spojíme do slov
        return '   '.join(encode_words) # slova spojíme do věty

    def decode(self, morse):
        """ implementuj tuto metodu, decode znamená dekódovat """
        words = morse.split('   ') # rozdělíme text na slova
        decoded_words = []
        for word in words:
            decoded_ch = [alphabet_reverse[ch] for ch in word.split(' ')] # převedeme slovo na pismena v morseovce
            decoded_words.append(''.join(decoded_ch)) # pismena spojíme do slov
        return ' '.join(decoded_words) # slova spojíme do věty




morse = Morse()
print(morse.encode('SOME TEXT HERE'))
# toto by mělo vrátit:
# ... --- -- .   - . -..- -   .... . .-. .

print(morse.decode('... --- -- .   - . -..- -   .... . .-. .'))
# toto by mělo vrátit:
# SOME TEXT HERE

# zde je tajná zakodáváná zpráva pro vás
print(morse.decode(
    '-- .- .-. .-. -.--   -.-. .... .-. .. ... - -- .- ...   .- -. -..   .... .- .--. .--. -.--   -. . .--   -.-- . .- .-.'))