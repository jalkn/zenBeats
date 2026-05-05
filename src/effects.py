import numpy as np
from scipy.io import wavfile
import os

def mix_fractal_audio(base_audio_path, ambient_audio_path, output_filename, volume_base=0.6, volume_ambient=0.4):
    """
    Mixes a generated beat with an ambient environmental sound (e.g., Santa Elena forest).
    """
    if not os.path.exists(base_audio_path) or not os.path.exists(ambient_audio_path):
        print("Error: Los archivos de audio no existen. Por favor genere el beat primero.")
        return
    
    # Read the audio files
    sr_base, base_data = wavfile.read(base_audio_path)
    sr_amb, amb_data = wavfile.read(ambient_audio_path)
    
    # Match data dimensions
    min_len = min(len(base_data), len(amb_data))
    base_data = base_data[:min_len]
    amb_data = amb_data[:min_len]
    
    # Weighted mixing
    mixed_signal = (base_data * volume_base) + (amb_data * volume_ambient)
    
    # Normalize to avoid distortion
    mixed_signal = np.int16(mixed_signal / np.max(np.abs(mixed_signal)) * 32767)
    
    # Save the output file
    output_path = f"output/{output_filename}"
    os.makedirs('output', exist_ok=True)
    wavfile.write(output_path, sr_base, mixed_signal)
    print(f"Archivo mezclado creado exitosamente en: {output_path}")

if __name__ == "__main__":
    print("Módulo de efectos listo para el ecosistema Zenergia.")