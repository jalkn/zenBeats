import json
from src.generator import AudioGenerator

def main():
    print("Iniciando generación de frecuencias para Zenergia...")
    
    # Cargar configuración de frecuencias
    with open('config/frequencies.json', 'r') as f:
        frequencies = json.load(f)
        
    for key, data in frequencies.items():
        base_hz = data['base_freq_hz']
        filename = f"{key}_{base_hz}hz_melodia.wav"
        
        AudioGenerator.create_melody(
            base_freq=base_hz,
            filename=filename,
            duration_seconds=data['duration_seconds']
        )
        
    print("¡Proceso finalizado! Los archivos están en la carpeta output/raw/")

if __name__ == "__main__":
    main()