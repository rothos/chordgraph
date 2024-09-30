# https://www.songsterr.com/a/wsa/bob-dylan-like-a-rolling-stone-chords-s22345
# https://tabs.ultimate-guitar.com/tab/bob-dylan/like-a-rolling-stone-chords-371756
# https://www.e-chords.com/chords/jimi-hendrix/like-a-rolling-stone


import json

dbfile = "data/db.json"

data = {
    "songs": [
        {
            "id": 1,
            "name": "Like A Rolling Stone",
            "artist": "Bob Dylan",
            "key": "C",
            "chords": [
                "C","Fmaj7/C","C","Fmaj7/C","C","Fmaj7/C","C","Fmaj7/C","C","Dm7","Em","F","G","C","Dm7","Em","F","G","F","G","F","G","F","Em","Dm7","C","F","Em","Dm7","C","Dm7","F","G","C","F","G","C","F","G","C","F","G","C","F","G","C","F","G","C","F","G","C","Dm7","Em","F","G","C","Dm7","Em","F","G","F","G","F","G","F","Em","Dm7","C","F","Em","Dm7","C","Dm7","F","G","C","F","G","C","F","G","C","F","G","C","F","G","C","F","G","C","F","G","C","F","G","C","Dm7","Em","F","G","C","Dm7","Em","F","G","F","G","F","G","F","Em","Dm7","C","F","Em","Dm7","C","Dm7","F","G","C","F","G","C","F","G","C","F","G","C","F","G","C","F","G","C","F","G","C","F","G","C","Dm7","Em","F","G","C","Dm7","Em","F","G","F","G","F","G","F","Em","Dm7","C","F","Em","Dm7","C","Dm7","F","G","C","F","G","C","F","G","C","F","G","C","F","G","C","F","G","C","F","G","C","F","G"
            ]
        },
        {
            "id": 2,
            "name": "Wish You Were Here",
            "artist": "Pink Floyd",
            "key": "Em",
            "chords": [
                "Em7","G","Em7","A7sus4","G","C","D/F#","Am/E","G","D/F#","C","Am","G","C","D/F#","Am/E","G","D/F#","C","Am","G","Em7","G","Em7","G","Em7","A7sus4","Em7","A7sus4","G","C","D/F#","Am/E","G","D/F#","C","Am","G","Em7","G","Em7","G","Em7","A7sus4","Em7","A7sus4","G"
            ]
        }
    ],

}

with open("data/db.json", "w") as f:
    json.dump(data, f)
