"""Module providing the main funcionalities"""
import sqlite3
import os

from flask import Flask, flash, redirect, render_template, request, session
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

currentDirectory = os.path.dirname(os.path.abspath(__file__))


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


morse_map = {".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E", "..-.": "F",
             "--.": "G", "....": "H", "..": "I", ".---": "J", "-.-": "K", ".-..": "L",
             "--": "M", "-.": "N", "---": "O", ".--.": "P", "--.-": "Q", ".-.": "R",
             "...": "S", "-": "T", "..-": "U", "...-": "V", ".--": "W", "-..-": "X",
             "-.--": "Y", "--..": "Z", ".----": "1", "..---": "2", "...--": "3",
             "....-": "4", ".....": "5", "-....": "6", "--...": "7", "---..": "8",
             "----.": "9", "-----": "0"}

def getDurations():
    """This function gets the time parameters persisted on the SQLite3 database"""
    conn = sqlite3.connect(currentDirectory + '\morse_code.db')
    db = conn.cursor()
    db.execute("select * from config")
    config = db.fetchall()
    conn.commit()
    conn.close()

    return config[0][0], config[0][1], config[0][2]


@app.route("/", methods=["POST"])
def home():
    """Home page route - method POST. Translating from morse code to english and persisting the time parameters"""
    dit_duration, letters_duration, words_duration = getDurations()

    if request.form.get("origin") == "index":
        translation = ""
        morse_code = request.form.get("code")
        if (morse_code != None):
            letters = morse_code.split()
            for letter in letters:
                if (letter in morse_map):
                    translation += morse_map[letter]
                else:
                    if letter == "/":
                        translation += " "
                    else:
                        translation += "$"
        
        return render_template("index.html", morse_code=morse_code, translation=translation
                               ,dit_duration=dit_duration ,letters_duration=letters_duration
                               ,words_duration=words_duration)
    
    elif request.form.get("origin") == "config":
        dit_duration = request.form.get("dit_duration")
        letters_duration = request.form.get("letters_duration")
        words_duration = request.form.get("words_duration")

        conn = sqlite3.connect(currentDirectory + '\morse_code.db')
        db = conn.cursor()
        db.execute("""update config set dit_duration = ?
                   , letters_duration = ?
                   , words_duration = ?""", [dit_duration, letters_duration, words_duration])
        conn.commit()
        conn.close()

        return render_template("index.html", morse_code=" ", translation=" "
                               ,dit_duration=dit_duration, letters_duration=letters_duration
                               ,words_duration=words_duration)
    else:
        return render_template("index.html", morse_code=" ", translation=" "
                               ,dit_duration=dit_duration, letters_duration=letters_duration
                               ,words_duration=words_duration)


@app.route("/")
def simple_home():
    """Home page route - method GET"""
    dit_duration, letters_duration, words_duration = getDurations()
    return render_template("index.html", morse_code=" ", translation=" "
                           ,dit_duration=dit_duration ,letters_duration=letters_duration
                           ,words_duration=words_duration)


@app.route("/clear")
def clear():
    """It only redirects to the home page route - method GET"""
    return redirect("/")


@app.route("/translate", methods=["GET", "POST"])
def translate():
    """This function also translates from morse code to english"""
    dit_duration, letters_duration, words_duration = getDurations()
    if request.method == "POST":
        translation = ""
        morse_code = request.form.get("morse_code")
        if (morse_code != None):
            letters = morse_code.split()
            for letter in letters:
                if (letter in morse_map):
                    translation += morse_map[letter]
                else:
                    if letter == "/":
                        translation += " "
                    else:
                        translation += "$"
        return render_template("index.html", morse_code=morse_code, translation=translation
                               ,dit_duration=dit_duration, letters_duration=letters_duration
                               ,words_duration=words_duration)
    
    return render_template("index.html",dit_duration=dit_duration, letters_duration=letters_duration
                           ,words_duration=words_duration)

@app.route("/config", methods=["GET", "POST"])
def config():
    """This function gets the time parameters from the SQLite3 database"""
    conn = sqlite3.connect(currentDirectory + '\morse_code.db')
    db = conn.cursor()
    db.execute("select * from config")
    config = db.fetchall()
    conn.commit()
    conn.close()

    return render_template("config.html", dit_duration=config[0][0], letters_duration=config[0][1], words_duration=config[0][2])