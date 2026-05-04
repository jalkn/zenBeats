import numpy as np
import os
from scipy.io import wavfile

class AudioGenerator:
    @staticmethod
    def create_melody(base_freq, filename, duration_seconds=10, sample_rate=44100):
        """
        Genera una melodía (arpegio + armónicos) para crear texturas sonoras orgánicas.
        """
        os.makedirs('output/raw', exist_ok=True)
        
        t = np.linspace(0, duration_seconds, int(sample_rate * duration_seconds), endpoint=False)
        
        # Progresión armónica: fundamental, quinta justa y octava
        harmonics = [base_freq, base_freq * 1.5, base_freq * 2]
        
        wave = np.zeros_like(t)
        for i, f in enumerate(harmonics):
            weight = 0.4 / (i + 1)
            wave += weight * np.sin(2 * np.pi * f * t)
            
        # Modulación de amplitud lenta para dar sensación de pulso / respiración
        modulator = 0.5 + 0.5 * np.sin(2 * np.pi * 0.2 * t) 
        wave = wave * modulator
        
        # Envolvente de entrada y salida (fade) para evitar clics
        fade_duration = 1.5
        fade_samples = int(sample_rate * fade_duration)
        envelope = np.ones_like(wave)
        envelope[:fade_samples] = np.linspace(0, 1, fade_samples)
        envelope[-fade_samples:] = np.linspace(1, 0, fade_samples)
        
        wave = wave * envelope
        
        # Normalizar y limitar volumen (-3 dB de margen)
        wave = 0.6 * (wave / np.max(np.abs(wave)))
        wave_int = (wave * 32767).astype(np.int16)
        
        filepath = os.path.join('output/raw', filename)
        wavfile.write(filepath, sample_rate, wave_int)
        print(f"Melodía generada en: {filepath}")
        return filepath