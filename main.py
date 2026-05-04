import json
import os
from src.generator import AudioGenerator
from src.effects import mix_fractal_audio

def load_frequencies():
    with open('config/frequencies.json', 'r') as f:
        return json.load(f)

def main():
    print("==========================================")
    print("       Zenergia - zenBeats Module        ")
    print("==========================================")
    
    # Input example: 30FU30
    workout_input = input("Please enter the workout sequence: ").strip().upper()
    print(f"\nProcessing Zenergia sequence: {workout_input}")
    
    frequencies = load_frequencies()
    gen = AudioGenerator()
    
    # Generate the 10 seconds of percussive beat using Fall frequency
    f_data = frequencies['caer']
    filename = f"caer_{workout_input}.wav"
    
    gen.create_percussion(f_data['base_freq_hz'], filename, duration_seconds=10)
    
    base_path = f"output/raw/{filename}"
    ambient_path = "data/santa_elena.wav"
    
    if os.path.exists(ambient_path):
        mix_fractal_audio(base_path, ambient_path, f"mixed_{filename}", volume_base=0.85, volume_ambient=0.15)
    else:
        print("\nAudio de ambiente no encontrado. Generando pista en su forma pura.")

if __name__ == "__main__":
    main()