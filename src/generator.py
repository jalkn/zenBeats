import numpy as np
import os
from scipy.io import wavfile

class AudioGenerator:
    @staticmethod
    def print_3d_shape(action_type, action_code):
        """
        Generates and saves a 3D structural representation of the action.
        """
        os.makedirs('output/3d', exist_ok=True)
        # Cambiado el nombre del archivo a una estructura simple [Acción]Brick.txt
        filename = f"{action_code}Brick.txt"
        filepath = os.path.join('output/3d', filename)
        
        shapes = {
            'saltar': """
  [===]             [===]
  |   \\           /   |
  |    \\         /    |
  |     \\_______/     | (Hourglass horizontally)
  |     /       \\     |
  |    /         \\    |
  |   /           \\   |
  [===]             [===]
            """,
            'levantarse': """
                    ^
                   / \\
                  / * \\
                 /=====\\ (Pyramid arrow up)
            """,
            'caminar': """
                    |\\
                    | \\ > (Pyramid arrow right)
                    | / >
                    |/
            """,
            'caer': """
                 \\=====/ 
                  \\ * /
                   \\ /
                    V (Pyramid arrow down)
            """
        }
        
        shape_text = shapes.get(action_type, "  [Shape not defined]")
        
        # Write the 3D representation to file
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(shape_text)
            
        print(f"\n[Archivo de geometría 3D creado] Ruta: {filepath}")
        print(shape_text)

    @staticmethod
    def create_percussion(base_freq, action_code, duration_seconds=5, sample_rate=44100):
        """
        Generates a dense and punchy sub-bass percussion pulse of 5 seconds,
        simulating a tight and heavy heartbeat-like pulse.
        """
        os.makedirs('output/raw', exist_ok=True)
        
        # Actualizado para seguir la convención del usuario: Jbeat.wav, Fbeat.wav, etc.
        filename = f"{action_code}beat.wav"
        
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
        wavfile.write(filepath, sample_rate, wave_int)
        print(f"Secuencia percusiva generada exitosamente en: {filepath}")
        return filepath, filename