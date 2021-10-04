import sys
import os
import glob

# gets wanted path
def main():
    if len(sys.argv) > 1:
        path = sys.argv[1]

        if len(sys.argv) > 2:
            file_types =  sys.argv[2].split(" ")
            for index in range(0, len(file_types)):
                file_types[index] = fr"*.{file_types[index]}"
        else:
            file_types = ["*.wav", "*.mp3", "*.rx2", "*.asd", "*.mid", "*.ogg"]
        print(file_types)
        find_sample(path, file_types)
    else:
        print('Usage: python main.py path "wav mp3 rx2 wav.asd mid ogg"')
    

def edit_file_name(path, file):
    word_emojis = {"bass": "🎸", "guitar": "🎸", "sustain": "🎸", "reese": "🎸", "screech": "🎸", "guitar": "🎸", "drum": "🥁", "snare": "🥁", "kick": "🥁", "fill": "🥁", "perc": "🥁", "synth": "🎹", "melodic": "🎹", "vocal": "🎤", "acapella": "🎤"}

    for word in word_emojis:
        if word in file.lower():
            os.rename(os.path.join(path, file), os.path.join(path, f"{word_emojis[word]} {file}"))

            return 0
    
    for word in word_emojis:
        if word in path.lower():
            os.rename(os.path.join(path, file), os.path.join(path, f"{word_emojis[word]} {file}"))

            return 0


def find_sample(path, file_types):
    emojis = ["🎸", "🥁", "🎹", "🎤"]

    for new_path in os.listdir(path):
        new_path = os.path.join(path, new_path)

        if 1 not in [1 for emoji in emojis if emoji in new_path]:
            if 1 in [1 for file_type in file_types if new_path in glob.glob(os.path.join(path, file_type))]:
                edit_file_name(path, os.path.basename(new_path))
            else:
                if os.path.isdir(new_path):
                    find_sample(new_path, file_types)


if __name__ == "__main__":
    main()