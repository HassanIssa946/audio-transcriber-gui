# Audio Transcriber GUI

A user-friendly Tkinter interface for transcribing audio files using OpenAI's Whisper model. This application supports both GPU and CPU for processing, automatically selecting the GPU if available.

## Features

- Simple and intuitive GUI for selecting audio files.
- Utilizes Whisper model for high-quality transcription.
- Supports multiple audio formats (MP3, WAV, M4A).
- Automatically detects and uses GPU if available, otherwise falls back to CPU.

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- ffmpeg

### Installing Dependencies

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/audio-transcriber-gui.git
    cd audio-transcriber-gui
    ```

2. Install required Python packages:
    ```bash
    pip install torch whisper numpy tkinter
    ```

3. Install ffmpeg:
    - On Windows, use Chocolatey:
      ```bash
      choco install ffmpeg
      ```
    - On macOS, use Homebrew:
      ```bash
      brew install ffmpeg
      ```
    - On Linux, use your distribution's package manager, for example:
      ```bash
      sudo apt-get install ffmpeg
      ```

## Usage

1. Run the Tkinter GUI:
    ```bash
    python audio_transcriber_gui.py
    ```

2. Use the interface to select an audio file. The transcription will be displayed in the window.

## Project Structure

- `audio_transcriber_gui.py`: Main script for running the Tkinter interface and performing transcription.
- `README.md`: This file, providing an overview of the project and setup instructions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Whisper model by OpenAI
- Tkinter for the GUI

## Issues

If you encounter any issues or have suggestions, please open an issue on GitHub.
