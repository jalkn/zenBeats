import numpy as np
import os
from scipy.io import wavfile

class AudioGenerator:
    @staticmethod
    def print_3d_shape(action_type, action_code):
        """
        Generates and saves a 3D/Text representation and an SVG element of the action.
        """
        os.makedirs('output/3d', exist_ok=True)
        os.makedirs('output/svg', exist_ok=True)
        
        filename_txt = f"{action_code}Brick.txt"
        filepath_txt = os.path.join('output/3d', filename_txt)
        
        filename_svg = f"{action_code}Brick.svg"
        filepath_svg = os.path.join('output/svg', filename_svg)
        
        shapes = {
            'saltar': """
  [===]             [===]
  |   \\           /   |
  |    \\         /    |
  |     \\_______/     | (Reloj de arena horizontal - Chlorella)
  |     /       \\     |
  |    /         \\    |
  |   /           \\   |
  [===]             [===]
            """,
            'levantarse': """
                    ^
                   / \\
                  / * \\
                 /=====\\ (Pirámide hacia arriba)
            """,
            'caminar': """
                    |\\
                    | \\ > (Flecha a la derecha)
                    | / >
                    |/
            """,
            'caer': """
                 \\=====/ 
                  \\ * /
                   \\ /
                    V (Flecha hacia abajo)
            """
        }
        
        shape_text = shapes.get(action_type, "  [Shape not defined]")
        
        # Escribe la representación geométrica de texto
        with open(filepath_txt, "w", encoding="utf-8") as f:
            f.write(shape_text)
            
        print(f"\n[Archivo de geometría 3D creado] Ruta: {filepath_txt}")
        print(shape_text)

        # SVG 3D para el modelo de césped
        svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="100%" height="100%">
  <defs>
    <linearGradient id="chlorellaGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#76B900" stop-opacity="1" />
      <stop offset="100%" stop-color="#2C5E1B" stop-opacity="1" />
    </linearGradient>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="5" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>
  <rect width="100%" height="100%" fill="#1a1a1a"/>
  <circle cx="250" cy="250" r="200" fill="url(#chlorellaGrad)" filter="url(#glow)"/>
  <text x="250" y="260" font-family="monospace" font-size="20" fill="#ffffff" text-anchor="middle">
    {action_type.upper()}
  </text>
</svg>'''

        with open(filepath_svg, "w", encoding="utf-8") as f:
            f.write(svg_content)
        print(f"[Archivo SVG 3D creado] Ruta: {filepath_svg}")

    @staticmethod
    def create_percussion(base_freq, action_code, duration_seconds=5, sample_rate=44100):
        """
        Generates a dense and punchy sub-bass percussion pulse of 5 seconds,
        simulating a tight and heavy heartbeat-like pulse.
        """
        os.makedirs('output/raw', exist_ok=True)
        
        filename = f"{action_code}beat.wav"
        
        num_samples = int(sample_rate * duration_seconds)
        t = np.linspace(0, duration_seconds, num_samples, endpoint=False)
        
        base_sub = base_freq * 0.25
        mod = np.sin(2 * np.pi * 5 * t)
        wave = np.sin(2 * np.pi * base_sub * t + mod * 15.0)
        
        envelope = np.exp(-np.mod(t, 0.5) * 5.5)
        wave = wave * envelope
        
        wave = 0.8 * (wave / np.max(np.abs(wave)))
        wave_int = (wave * 32767).astype(np.int16)
        
        filepath = os.path.join('output/raw', filename)
        wavfile.write(filepath, sample_rate, wave_int)
        print(f"Secuencia percusiva generada exitosamente en: {filepath}")
        return filepath, filename