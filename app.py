from flask import Flask, render_template_string, redirect, url_for

app = Flask(__name__)

# Page 1: Greeting
PAGE1 = """
<!DOCTYPE html>
<html>
<head>
    <title>💌 Valentine 💌</title>
    <style>
        body { font-family: Arial; display:flex; justify-content:center; align-items:center; height:100vh;
               background: linear-gradient(135deg, #ff9a9e, #fad0c4);}
        .card { background:white; padding:30px; border-radius:20px; text-align:center; width:350px; box-shadow:0 10px 30px rgba(0,0,0,0.2);}
        button { padding:10px 20px; font-size:16px; border:none; border-radius:20px; cursor:pointer; background-color:#ff4d6d; color:white;}
        img { margin-bottom: 20px; border-radius:15px; }
    </style>
</head>
<body>
    <!-- Background music -->
    <audio autoplay loop>
        <source src="{{ url_for('static', filename='music.mp3') }}" type="audio/mpeg">
    </audio>

    <div class="card">
        <!-- Image placeholder -->
       <img src="{{ url_for('static', filename='page1.jpg') }}" alt="Page 1 Image" width="200">
        <h1>Hi Babi! 😘</h1>
        <p>I have a question for you…</p>
        <a href="{{ url_for('page2') }}"><button>Next 💌</button></a>
    </div>
</body>
</html>
"""

# Page 2: Valentine question
PAGE2 = """
<!DOCTYPE html>
<html>
<head>
    <title>💌 Valentine 💌</title>
    <style>
        body { font-family: Arial; display:flex; justify-content:center; align-items:center; height:100vh;
               background: linear-gradient(135deg, #ff9a9e, #fad0c4);}
        .card { background:white; padding:30px; border-radius:20px; text-align:center; width:350px; box-shadow:0 10px 30px rgba(0,0,0,0.2);}
        button { padding:10px 20px; margin:10px; font-size:16px; border:none; border-radius:20px; cursor:pointer;}
        .yes { background-color:#ff4d6d; color:white;}
        .no { background-color:#ccc; color:black;}
        img { margin-bottom: 20px; border-radius:15px; }
    </style>
</head>
<body>
    <!-- Background music -->
    <audio autoplay loop>
        <source src="{{ url_for('static', filename='music.mp3') }}" type="audio/mpeg">
    </audio>

    <div class="card">
        <!-- Image placeholder -->
         <img src="{{ url_for('static', filename='page2.jpg') }}" alt="Page 2 Image" width="200">
        <h1>💌 Will you be my Valentine? 💕</h1>
        <a href="{{ url_for('finale', response='yes') }}"><button class="yes">Yes 💖</button></a>
        <a href="{{ url_for('finale', response='no') }}"><button class="no">No 💔</button></a>
    </div>
</body>
</html>
"""

# Page 3: Finale page
FINALE_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>💌 Valentine 💌</title>
    <style>
        body { font-family: Arial; display:flex; justify-content:center; align-items:center; height:100vh;
               background: linear-gradient(135deg, #ff9a9e, #fad0c4);}
        .card { background:white; padding:30px; border-radius:20px; text-align:center; width:350px; box-shadow:0 10px 30px rgba(0,0,0,0.2);}
        h1 { color:#ff4d6d; }
        img { margin-bottom: 20px; border-radius:15px; }
    </style>
</head>
<body>
    <!-- Background music -->
    <audio autoplay loop>
        <source src="{{ url_for('static', filename='music.mp3') }}" type="audio/mpeg">
    </audio>

    <div class="card">
        <!-- Image placeholder -->
        <img src="{{ url_for('static', filename='finale.jpg') }}" alt="Finale Image" width="200">
        <h1>{{ message|safe }}</h1>
    </div>
</body>
</html>
"""

@app.route("/")
def page1():
    return render_template_string(PAGE1)

@app.route("/page2")
def page2():
    return render_template_string(PAGE2)

@app.route("/finale/<response>")
def finale(response):
    if response == "yes":
        message = "YAY!! 🥰💖 Happy Valentine’s Day 🌹"
    else:
        message = "It’s okay ❤️ You still mean a lot to me."
    return render_template_string(FINALE_PAGE, message=message)
