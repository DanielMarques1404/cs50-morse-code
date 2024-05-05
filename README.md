# MORSE CODE TRAINNER
#### Video Demo:  <https://youtu.be/DkQTBRsq5VY>
#### Description:
**MorseCodeTrainner** is a web-based application using *JavaScript*, *Python* and *SQL*, that allows the users to learn and practice their morse code skills.

The app has a **red button** that simulate the dit's ( ▄ ) and dah's ( ▄▄▄ ) that are used in the nowadays practice of morse coding. For understanding sakes, we can also say, dots and dashs, respectively.

A short duration click represents a dit and a longer click a dah. After each click, the application measures the duration of the pause (time between two consecutive clicks). A short duration pause will indicate that a letter has just finished and the next click will compose the next one. When the pause is bigger, it'll indicate that the user's intent was to finish a word, making the next clicks the first letter of a new word.

> **NOTE:**
> The application holds these time parameters in a *SQLite3 database* called **morse_code.db**. Allowing the users to change these informations anytime, by going to the applications' **config section**.

When the work is finished, the user clicks in the **translate button** to let the application translates from morse code to english, finally showing the result to the user. This will finish the main use case of the system.

#### Technical details:
The application has a typical *flask python* file structure:

- static
    - images
        - [bnt_snd.png](static/images/bnt_snd.png)
        - [morse-chart-2.png](static/images/morse-chart-2.png)
    - sounds
        - [short-beep.wav](static/sounds/short-beep.wav)
    - [main.js](static/main.js)
    - [style.css](static/styles.css)
- templates
    - [config.html](templates/config.html)
    - [index.html](templates/index.html)
- [app.py](app.py)
- [morse_code.sql](morse_code.sql)
- [morse_code.db](morse_code.db)
- README.md

##### [**`static/images`**](static/images)
The first image, [**bnt_snd.png**](static/images/bnt_snd.png), is the html image element that exists to be clicked. Later on we'll see how the application computes the duration of the *onmousedown* and *onmouseup* events over this element. Each click will represent a symbol (dit or dah). For didactic reasons, I will henceforth call it the **red button**.

The second image, [**morse-chart-2.png**](static/images/morse-chart-2.png), is placed at the bottom of the page and has the purpose to help the users with a morse code dictionary. For didactic reasons, I will henceforth call it the **morse code chart**.

##### [**`static/sounds`**](static/sounds)
This folder holds the sound file [**short-beep.wav**](static/sounds/short-beep.wav). It's just a sound effect representing the dots and dashs after each click on the **red button**. For didactic reasons, I will henceforth call it the **beep sound**.

##### [**`static/main.js`**](static/main.js)
In this file we have all the app's *javascript* logic.

The most important functions are:

**beep()**:
This function is triggered on the *onmousedown* event of the **red button** and is responsible for:
- Checking if it's time to separate a letter or a word, by calling the *wrtSeparators()* function;
- Storing the time that this function has started. It will allow the app to calculate the duration of the click;
- Executing the **beep sound**.

**stopbeep()**:
This function is triggered on the *onmouseup* event of the **red button** and is responsible for:
- Stopping the **beep sound** execution;
- Storing the time that this function has ended. It will allow the app to calculate the duration of the click;
- Calling the *wrtSymbol()* function to write the dot or the dash.

**wrtSymbol()**:
This function is responsible for calculating the duration of the click. If its value is equal or smaller than the *dit_duration* parameter, it'll print a dot. Otherwise a dash.

**wrtSeparators()**:
This function is responsible for calculating the duration of the pause between two consecutive clicks. If its value is between the *letters_duration* and *words_duration* parameters, a space will be print (representing the letter's end). If its value is greater than *words_duration* parameter, it'll print a slash (representing the word's end).

##### [**`static/style.css`**](static/styles.css)
The app uses *bootstrap* and this css file to decorate its html pages (*index.html* and *config.html*)

##### [**`templates/config.html`**](templates/config.html)
This is the html page that allows the users to configure the time parameters of the app. These parameters are persisted in a *SQLite3* database.

We have 3 (three) int parameters:
- **dit_duration**: Indicates the max duration (in milliseconds) of a click that represents a dot. Bigger durations will represent a dash.
- **letters_duration**: We know that the morse code's letters are a composition of dots and dashs. So, we have to signal to the application when we are still on the same letter, a new one or even a new word. The duration (in milliseconds) of the pauses between clicks was the device used to identify each of these situations. A duration smaller than this parameter will indicate that we are still in the same letter.
- **words_duration**: A pause duration smaller than this parameter and bigger than the last one will indicate that we are starting a new letter. And when the pause is bigger than this parameter we have a new word beginning.

##### [**`templates/index.html`**](templates/index.html)
This is the main page of the app. Here we find the main elements of interaction with users. Besides, from here we can go to:
- **\\**: Going to the main page;
- **\clear**: To clear the last symbols;
- **\translate**: To translate the symbols already written;
- **\config**: Going to the *config.html* page.

##### [**`app.py`**](app.py)
This app is running over a *flask python* architecture and, according to [**realpython.com**](https://realpython.com/flask-blueprint/#:~:text=The%20file%20app.py%20will,you%20associate%20views%20to%20routes.): 

> The file app.py will contain the definition of the application and its views.
>
> When you create a Flask application, you start by creating a Flask object that represents your application, and then you associate views to routes. Flask takes care of dispatching incoming requests to the correct view based on the request URL and the routes you’ve defined.

In addition to controlling all routes, the main functions of **app.py** are:

- There we defined a dictionary relating the English alphabet to Morse code in order to translate the messages sent from the user. Also responsible for the separation of the letters and the words;
- There we find all questions related to access to the *SQLite3 database*. To retrieve/save information from/to *config table*.

> **NOTE:**
> When the application doesn't reconize a morse code symbol it prints a **$**.

##### [**`morse_code.sql`**](morse_code.sql)
This file exists only for the purpose of storing the most basic configurations of the application database. A SQL script to create the database and to insert the first values. It's necessary to execute it only once.

##### [**`morse_code.db`**](morse_code.db)
This *SQLite3 database* file holds the *table config* that is responsible to store the time parameters used by the application. These parameters have already been discussed in previous sections.

------------

**A very simple but useful tool to morse code training. I hope you'll like it!**