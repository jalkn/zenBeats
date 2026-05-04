import numpy as np
import os
from scipy.io import wavfile

class AudioGenerator:
    @staticmethod
    def create_percussion(base_freq, filename, duration_seconds=5, sample_rate=44100):
        """
        Generates a dense and punchy sub-bass percussion pulse of 5 seconds,
        simulating a tight and heavy heartbeat-like pulse.
        """
        os.makedirs('output/raw', exist_ok=True)
        
        num_samples = int(sample_rate * duration_seconds)
        t = np.linspace(0, duration_seconds, num_samples, endpoint=False)
        
        # Sub-bass synthesis for a deep punch
        base_sub = base_freq * 0.25
        mod = np.sin(2 * np.pi * 5 * t)
        wave = np.sin(2 * np.pi * base_sub * t + mod * 15.0)
        
        # Envelope: adjusted to make the pulse much more dense (repetition every 0.5 seconds)
        envelope = np.exp(-np.mod(t, 0.5) * 5.5)
        wave = wave * envelope
        
        # Normalize
        wave = 0.8 * (wave / np.max(np.abs(wave)))
        wave_int = (wave * 32767).astype(np.int16)
        
        filepath = os.path.join('output/raw', filename)
        wavfile.write(filepath, wave_int)
        print(f"Percussive beat successfully generated at: {filepath}")
        return filepath