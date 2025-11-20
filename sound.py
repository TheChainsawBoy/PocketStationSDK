"""
sound.py - Play sounds using a frequency similar beeps to PocketStation
"""
import pygame
import numpy as np

class SoundManager:
    def __init__(self):
        pygame.mixer.init(frequency=44100, size=-16, channels=1)
        self.sounds = {}

    def generate_tone(self, frequency=440, duration=0.2, volume=0.5):
        sample_rate = 44100
        frequency = max(261, min(523, frequency))

        t = np.linspace(0, duration, int(sample_rate * duration), False)
        wave = 0.5 * np.sign(np.sin(2 * np.pi * frequency * t))
        wave = np.int16(wave * 32767 * volume)
        #Convert mono to stereo
        wave_stereo = np.column_stack((wave, wave))
        return pygame.sndarray.make_sound(wave_stereo)

    def add_sound(self, name, frequency=440, duration=0.2, volume=0.5):
        self.sounds[name] = self.generate_tone(frequency, duration, volume)

    def play(self, name):
        if name in self.sounds:
            self.sounds[name].play()
        else:
            print(f"Sound '{name}' not found!")