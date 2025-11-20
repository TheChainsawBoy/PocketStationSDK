#Pixel data for each letter of the alphabet (5x5 grid)
from objects import PixelSprite
from engine import GameObject

#Letters A-Z
letter_a = [
    [0,1,0],
    [1,0,1],
    [1,1,1],
    [1,0,1],
    [1,0,1]
]

letter_b = [
    [1,1,0],
    [1,0,1],
    [1,1,0],
    [1,0,1],
    [1,1,0]
]

letter_c = [
    [0,1,1],
    [1,0,0],
    [1,0,0],
    [1,0,0],
    [0,1,1]
]

letter_d = [
    [1,1,0],
    [1,0,1],
    [1,0,1],
    [1,0,1],
    [1,1,0]
]

letter_e = [
    [1,1,1],
    [1,0,0],
    [1,1,0],
    [1,0,0],
    [1,1,1]
]

letter_f = [
    [1,1,1],
    [1,0,0],
    [1,1,0],
    [1,0,0],
    [1,0,0]
]

letter_g = [
    [0,1,1],
    [1,0,0],
    [1,0,1],
    [1,0,1],
    [0,1,1]
]

letter_h = [
    [1,0,1],
    [1,0,1],
    [1,1,1],
    [1,0,1],
    [1,0,1]
]

letter_i = [
    [1,1,1],
    [0,1,0],
    [0,1,0],
    [0,1,0],
    [1,1,1]
]

letter_j = [
    [0,0,1],
    [0,0,1],
    [0,0,1],
    [1,0,1],
    [0,1,0]
]

letter_k = [
    [1,0,1],
    [1,0,1],
    [1,1,0],
    [1,0,1],
    [1,0,1]
]

letter_l = [
    [1,0,0],
    [1,0,0],
    [1,0,0],
    [1,0,0],
    [1,1,1]
]

letter_m = [
    [1,0,0,0,1],
    [1,1,0,1,1],
    [1,0,1,0,1],
    [1,0,0,0,1],
    [1,0,0,0,1]
]

letter_n = [
    [1,0,1],
    [1,1,1],
    [1,1,1],
    [1,0,1],
    [1,0,1]
]

letter_o = [
    [0,1,0],
    [1,0,1],
    [1,0,1],
    [1,0,1],
    [0,1,0]
]

letter_p = [
    [1,1,0],
    [1,0,1],
    [1,1,0],
    [1,0,0],
    [1,0,0]
]

letter_q = [
    [0,1,0],
    [1,0,1],
    [1,0,1],
    [1,1,0],
    [0,1,1]
]

letter_r = [
    [1,1,0],
    [1,0,1],
    [1,1,0],
    [1,0,1],
    [1,0,1]
]

letter_s = [
    [0,1,1],
    [1,0,0],
    [0,1,0],
    [0,0,1],
    [1,1,0]
]

letter_t = [
    [1,1,1],
    [0,1,0],
    [0,1,0],
    [0,1,0],
    [0,1,0]
]

letter_u = [
    [1,0,1],
    [1,0,1],
    [1,0,1],
    [1,0,1],
    [0,1,0]
]

letter_v = [
    [1,0,1],
    [1,0,1],
    [1,0,1],
    [1,0,1],
    [0,1,0]
]

letter_w = [
    [1,0,1],
    [1,0,1],
    [1,0,1],
    [1,1,1],
    [1,0,1]
]

letter_x = [
    [1,0,1],
    [1,0,1],
    [0,1,0],
    [1,0,1],
    [1,0,1]
]

letter_y = [
    [1,0,1],
    [1,0,1],
    [0,1,0],
    [0,1,0],
    [0,1,0]
]

letter_z = [
    [1,1,1],
    [0,0,1],
    [0,1,0],
    [1,0,0],
    [1,1,1]
]

# Numbers 0-9
number_0 = [
    [0,1,0],
    [1,0,1],
    [1,0,1],
    [1,0,1],
    [0,1,0]
]

number_1 = [
    [0,1,0],
    [1,1,0],
    [0,1,0],
    [0,1,0],
    [1,1,1]
]

number_2 = [
    [1,1,0],
    [0,0,1],
    [0,1,0],
    [1,0,0],
    [1,1,1]
]

number_3 = [
    [1,1,0],
    [0,0,1],
    [0,1,0],
    [0,0,1],
    [1,1,0]
]

number_4 = [
    [1,0,1],
    [1,0,1],
    [1,1,1],
    [0,0,1],
    [0,0,1]
]

number_5 = [
    [1,1,1],
    [1,0,0],
    [1,1,0],
    [0,0,1],
    [1,1,0]
]

number_6 = [
    [0,1,1],
    [1,0,0],
    [1,1,0],
    [1,0,1],
    [0,1,0]
]

number_7 = [
    [1,1,1],
    [0,0,1],
    [0,1,0],
    [0,1,0],
    [1,0,0]
]

number_8 = [
    [0,1,0],
    [1,0,1],
    [0,1,0],
    [1,0,1],
    [0,1,0]
]

number_9 = [
    [0,1,0],
    [1,0,1],
    [0,1,1],
    [0,0,1],
    [1,1,0]
]

# Special Characters
exclamation = [
    [0,1,0],
    [0,1,0],
    [0,1,0],
    [0,0,0],
    [0,1,0]
]

question = [
    [0,1,0],
    [1,0,1],
    [0,0,1],
    [0,0,0],
    [0,1,0]
]

period = [
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,1,0]
]

comma = [
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,1,0],
    [1,0,0]
]

colon = [
    [0,0,0],
    [0,1,0],
    [0,0,0],
    [0,1,0],
    [0,0,0]
]

semicolon = [
    [0,0,0],
    [0,1,0],
    [0,0,0],
    [0,1,0],
    [1,0,0]
]

plus = [
    [0,0,0],
    [0,1,0],
    [1,1,1],
    [0,1,0],
    [0,0,0]
]

minus = [
    [0,0,0],
    [0,0,0],
    [1,1,1],
    [0,0,0],
    [0,0,0]
]

asterisk = [
    [1,0,1],
    [0,1,0],
    [1,1,1],
    [0,1,0],
    [1,0,1]
]

slash = [
    [0,0,1],
    [0,0,1],
    [0,1,0],
    [1,0,0],
    [1,0,0]
]

hash = [
    [1,0,1],
    [1,1,1],
    [1,0,1],
    [1,1,1],
    [1,0,1]
]

at_sign = [
    [0,1,0],
    [1,0,1],
    [1,1,1],
    [1,0,0],
    [0,1,1]
]

ampersand = [
    [0,1,0],
    [1,0,1],
    [0,1,0],
    [1,0,1],
    [0,1,1]
]

dollar = [
    [0,1,0],
    [1,1,1],
    [1,1,0],
    [0,1,1],
    [0,1,0]
]

percent = [
    [1,0,1],
    [0,0,1],
    [0,1,0],
    [1,0,0],
    [1,0,1]
]

space = [
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

#Character map dictionary for easy lookup
char_map = {
    'a': letter_a, 'b': letter_b, 'c': letter_c, 'd': letter_d,
    'e': letter_e, 'f': letter_f, 'g': letter_g, 'h': letter_h,
    'i': letter_i, 'j': letter_j, 'k': letter_k, 'l': letter_l,
    'm': letter_m, 'n': letter_n, 'o': letter_o, 'p': letter_p,
    'q': letter_q, 'r': letter_r, 's': letter_s, 't': letter_t,
    'u': letter_u, 'v': letter_v, 'w': letter_w, 'x': letter_x,
    'y': letter_y, 'z': letter_z,
    '0': number_0, '1': number_1, '2': number_2, '3': number_3,
    '4': number_4, '5': number_5, '6': number_6, '7': number_7,
    '8': number_8, '9': number_9,
    '!': exclamation, '?': question, '.': period, ',': comma,
    ':': colon, ';': semicolon, '+': plus, '-': minus,
    '*': asterisk, '/': slash, '#': hash, '@': at_sign,
    '&': ampersand, '$': dollar, '%': percent, ' ': space
}


class BitString(GameObject):
    def __init__(self, text, x, y, spacing=1):
        #Calculate width and height based on text
        self.text = text
        self.spacing = spacing
        self.pixel_height = 5  #Assuming 5 rows for 5x5 font
        self.pixel_width = 5   #Assuming 5 columns per character

        #Width is number of characters * character width + spacing between
        width = len(text) * self.pixel_width + (len(text)-1) * spacing if text else self.pixel_width
        height = self.pixel_height

        #Initialize GameObject
        super().__init__(x, y, width, height)

        #Create the PixelSprite for this string
        self.string_sprite = self.create_string_sprite()

    def create_string_sprite(self):
        #Create a single PixelSprite for the entire string
        if not self.text:
            return PixelSprite(self.x, self.y, space)

        #Build the combined pixel data
        combined_rows = [[] for _ in range(self.pixel_height)]

        for i, char in enumerate(self.text.lower()):
            pixel_data = char_map.get(char, space)

            for row_idx in range(self.pixel_height):
                combined_rows[row_idx].extend(pixel_data[row_idx])

                #Add spacing between characters except after last character
                if i < len(self.text) - 1:
                    combined_rows[row_idx].extend([0] * self.spacing)

        return PixelSprite(self.x, self.y, combined_rows)

    def update_string(self, text):
        self.text = text
        #Update width
        self.width = len(text) * self.pixel_width + (len(text)-1) * self.spacing if text else self.pixel_width
        #Recreate PixelSprite
        self.string_sprite = self.create_string_sprite()

    def update(self, dt):
        #Delegate update if needed, or implement custom behavior
        pass

    def draw(self, screen):
        #Draw the string via the PixelSprite
        if self.visible:
            self.string_sprite.draw(screen)
