import os

from gtts import gTTS




def prank_play():
    text = 'роскомнадзор запретил букву'
    letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    result = []
    for letter in letters:
        if letter in text:
            result.append(F'{text} {letter}')
            text = text.replace(letter, '').replace('  ', ' ').strip()
        
    tts = gTTS(text='\n'.join(result), lang='ru')
    tts.save('roskomnadzor.mp3')
    os.system('roskomnadzor.mp3')

if __name__ == '__main__':
    prank_play()