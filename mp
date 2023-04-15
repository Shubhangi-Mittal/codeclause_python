import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, master):
        self.master = master
        master.title("Music Player")
        master.geometry("300x150")

        self.music_file = None
        self.playing = False

        # create widgets
        self.label = tk.Label(master, text="Select a Music File", font=("Arial", 12))
        self.label.pack(pady=10)

        self.select_button = tk.Button(master, text="Select", command=self.select_music)
        self.select_button.pack(pady=5)

        self.play_button = tk.Button(master, text="Play", command=self.play_music)
        self.play_button.pack(pady=5)

        self.stop_button = tk.Button(master, text="Stop", command=self.stop_music)
        self.stop_button.pack(pady=5)

    def select_music(self):
        # open a file dialog to select a music file
        self.music_file = filedialog.askopenfilename(defaultextension=".mp3", filetypes=[("Music Files", "*.mp3")])
        self.label.config(text=self.music_file)

    def play_music(self):
        if self.music_file and not self.playing:
            # initialize pygame mixer
            pygame.mixer.init()

            # load and play the music file
            pygame.mixer.music.load(self.music_file)
            pygame.mixer.music.play()

            self.playing = True

    def stop_music(self):
        if self.playing:
            # stop the music and quit pygame mixer
            pygame.mixer.music.stop()
            pygame.mixer.quit()

            self.playing = False

root = tk.Tk()
music_player = MusicPlayer(root)
root.mainloop()
