import tkinter as tk
from tkinter import filedialog, messagebox
import whisper
import torch

class AudioTranscriberApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Audio Transcriber")
        
        self.label = tk.Label(root, text="Select an audio file to transcribe:", font=("Helvetica", 14))
        self.label.pack(pady=20)

        self.select_button = tk.Button(root, text="Select Audio File", command=self.select_file, font=("Helvetica", 12))
        self.select_button.pack(pady=10)

        self.transcription_label = tk.Label(root, text="Transcription will appear here.", font=("Helvetica", 12), wraplength=600, justify="left")
        self.transcription_label.pack(pady=20)

    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav *.m4a")])
        if file_path:
            self.transcribe_audio(file_path)

    def transcribe_audio(self, audio_file_path):
        try:
            # Check if a GPU is available and use it if present
            device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

            # Load the whisper model for English transcription and move it to the GPU
            model = whisper.load_model("base.en").to(device)
            
            # Transcribe the audio file using the loaded model
            result = model.transcribe(audio_file_path)
            
            # Display the transcribed text
            self.transcription_label.config(text=result["text"])
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while transcribing the audio file:\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = AudioTranscriberApp(root)
    root.geometry("800x400")
    root.mainloop()
