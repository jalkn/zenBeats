import json
import os
from src.generator import AudioGenerator
from src.effects import mix_fractal_audio

def load_frequencies():
    with open('config/frequencies.json', 'r') as f:
        return json.load(f)

def get_action_data(letter, frequencies):
    """Maps the letter to the specific action properties."""
    mapping = {
        'F': ('caer', 'caer'),
        'U': ('levantarse', 'levantarse'),
        'W': ('caminar', 'caminar'),
        'J': ('saltar', 'saltar')
    }
    
    letter = letter.upper()
    if letter not in mapping:
        raise ValueError(f"Unknown action code: {letter}")
    
    key, label = mapping[letter]
    return frequencies[key], label

def main():
    print("==========================================")
    print("       Zenergia - zenBeats Module         ")
    print("==========================================")
    
    frequencies = load_frequencies()
    gen = AudioGenerator()
    
    # Changed prompt to Spanish but kept behavior
    workout_input = input("Por favor ingrese la secuencia de acciones (ej. J, U, W, F): ").strip().upper()
    print(f"\nProcesando secuencia de Zenergia: {workout_input}")
    
    for char in workout_input:
        try:
            f_data, action_key = get_action_data(char, frequencies)
            
            # Generate shape output
            gen.print_3d_shape(action_key, char)
            
            filename = f"action_{char}_{workout_input}.wav"
            gen.create_percussion(f_data['base_freq_hz'], filename, duration_seconds=10)
            
            base_path = f"output/raw/{filename}"
            ambient_path = "data/santa_elena.wav"
            
            if os.path.exists(ambient_path):
                mix_fractal_audio(base_path, ambient_path, f"mixed_{filename}", volume_base=0.85, volume_ambient=0.15)
            else:
                print("\nAudio de ambiente no encontrado. Generando pista en su forma pura.")
                
        except ValueError as e:
            print(f"Acción desconocida omitida: {e}")

if __name__ == "__main__":
    main()