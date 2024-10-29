import random
from captcha.audio import AudioCaptcha

def generate_random_captcha(lenght=6):
    characters = '1234567890'
    captcha_text = ''.join(random.choices(characters, k=lenght))
    return captcha_text

audio = AudioCaptcha()
captcha_text = generate_random_captcha()
print("Generated CAPTCHA text: ", captcha_text)
audio_captcha = audio.generate(captcha_text)
audio.write(captcha_text, 'Audio_Captcha.waw')
print("Audio CAPTCHA generated: Audio_Captcha.waw")