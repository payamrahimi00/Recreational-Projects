from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.text import LabelBase
LabelBase.register(name='Roboto', fn_regular='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf')
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', 
    '(': '-.--.', ')': '-.--.-'
}

class MorseApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        
        self.input_text = TextInput(hint_text='Enter text to convert to Morse code', multiline=False)
        self.layout.add_widget(self.input_text)
        
        self.convert_button = Button(text='Convert to Morse Code')
        self.convert_button.bind(on_press=self.convert_to_morse)
        self.layout.add_widget(self.convert_button)
        
        self.output_label = Label(text='Morse Code will appear here')
        self.layout.add_widget(self.output_label)
        
        return self.layout
    
    def convert_to_morse(self, instance):
        text = self.input_text.text.upper()
        morse_code = ' '.join(MORSE_CODE_DICT.get(char, '') for char in text)
        self.output_label.text = morse_code

if __name__ == '__main__':
    MorseApp().run()