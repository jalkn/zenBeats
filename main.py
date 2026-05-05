import json
import os
from src.generator import AudioGenerator
from src.effects import mix_fractal_audio

def load_frequencies():
    with open('config/frequencies.json', 'r') as f:
        return json.load(f)

def get_action_data(letter_or_word, frequencies):
    """
    Maps an action letter or word to the proper action parameters.
    Allows single letter ('J', 'U', 'W', 'F') or full Spanish action name.
    """
    mapping = {
        'F': ('caer', 'caer'),
        'U': ('levantarse', 'levantarse'),
        'W': ('caminar', 'caminar'),
        'J': ('saltar', 'saltar'),
        'CAER': ('caer', 'caer'),
        'LEVENTARSE': ('levantarse', 'levantarse'),
        'LEVANTARSE': ('levantarse', 'levantarse'),
        'CAMINAR': ('caminar', 'caminar'),
        'SALTAR': ('saltar', 'saltar')
    }
    
    key_input = letter_or_word.strip().upper()
    if key_input not in mapping:
        raise ValueError(f"Unknown action code: {key_input}")
    
    key, label = mapping[key_input]
    return frequencies[key], label

def main():
    print("==========================================")
    print("       Zenergia - zenBeats Module         ")
    print("==========================================")
    
    frequencies = load_frequencies()
    gen = AudioGenerator()
    
    user_input = input("Por favor ingrese la secuencia de acciones (ej. saltar, levantarse, caminar, caer): ").strip()
    
    sequence_elements = [x.strip() for x in user_input.replace(',', ' ').split() if x.strip()]
    print(f"\nProcesando secuencia de Zenergia: {sequence_elements}")
    
    for item in sequence_elements:
        try:
            f_data, action_key = get_action_data(item, frequencies)
            action_code = f_data['action']
            
            gen.print_3d_shape(action_key, action_code)
            
            filename = f"action_{action_code}_{''.join([get_action_data(x, frequencies)[0]['action'] for x in sequence_elements])}.wav"
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