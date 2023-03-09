import os
import random
import time
import winsound

# set the directory path containing sound files
dir_path = "C:/"

# get a list of all the sound files in the directory
sound_files = [f for f in os.listdir(dir_path) if f.endswith('.wav')

# wait for the computer to finish startup, optional
#time.sleep(1)

# randomly select a sound file from the list
selected_sound = random.choice(sound_files)

# play the selected sound file
winsound.PlaySound(os.path.join(dir_path, selected_sound), winsound.SND_FILENAME)
