# zenBeats 🧬

**zenBeats** is the fractal audio module of Zenergia, designed to generate harmonic frequencies that serve as the sonic grammar and organic soundscapes for the ecosystem. Through programmatic audio synthesis, this repository produces the melodies for the four universal movements: **Caer, Levantarse, Caminar, and Saltar**.

---

## 🚀 Installation

Follow these steps in your terminal to set up the project on your local machine:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/zenBeats.git](https://github.com/your-username/zenBeats.git)
   cd zenBeats
Create a virtual environment (recommended):

Bash
python -m venv venv
source venv/bin/activate  # On Linux/macOS
# or on Windows:
# venv\Scripts\activate
Install the dependencies:

Bash
pip install -r requirements.txt
🎶 Usage
To generate the complete set of harmonic frequencies for the ecosystem, run the main script:

Bash
python main.py
Once the process finishes, you will find the generated .wav files in the following output directory:
output/raw/

📁 File Structure
Plaintext
zenBeats/
│
├── config/
│   └── frequencies.json      # Parameters and base frequencies (Hz)
│
├── src/
│   ├── __init__.py
│   ├── generator.py          # Harmonic generator and frequency modulator
│   └── effects.py            # Envelopes and fade modules
│
├── output/
│   └── raw/                  # Generated raw audio files
│
├── data/
│
├── .gitignore
├── requirements.txt
├── main.py
└── README.md
📐 Fractal Ecosystem and Frequencies
Caer (396 Hz): Stability and fractal base.

Levantarse (417 Hz): Resonance, energy, and dynamic modulation.

Caminar (528 Hz): Steady pace, continuous rhythm, and repair.

Saltar (639 Hz): Expansion and connection of the entire system.