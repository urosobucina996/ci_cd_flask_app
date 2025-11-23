import os
from flask import Flask, Response
from dotenv import load_dotenv

import random

# Load environment variables from .env if present
load_dotenv()

app = Flask(__name__)
positive_sentences = [
    ("Every day is a new opportunity to grow.", "🌱"),
    ("Keep going, your efforts will pay off.", "💪"),
    ("Nah, better days are coming.", "☀️"),
    ("Bad today, better tomorrow.", "🌈"),
    ("You are stronger than you think.", "🔥"),
    ("Small progress is still progress.", "✨"),
    ("This too shall pass.", "🌊"),
    ("Believe in yourself, even when it’s hard.", "💖"),
    ("Keep your head up; brighter moments are ahead.", "🌞"),
    ("Take it one step at a time.", "👣"),
    ("Challenges make you stronger.", "🏋️‍♂️"),
    ("Nah, today was rough, but tomorrow’s a blank page.", "📖"),
    ("Focus on what you can control and let go of the rest.", "🕊️"),
    ("Mistakes are just lessons in disguise.", "🎓"),
    ("You’ve survived everything so far, you’ve got this!", "🛡️"),
    ("Every setback is a setup for a comeback.", "🚀"),
    ("Keep moving forward, even slowly.", "🐢"),
    ("Better things are on their way.", "🌸"),
    ("Don’t stress the storm; rainbows follow storms.", "🌈"),
    ("Bad today, better tomorrow — keep the faith.", "🙏"),
    ("Your potential is limitless.", "🌌"),
    ("Even small victories are worth celebrating.", "🏆"),
    ("Nah, it’s okay to pause, better days will come.", "🛋️"),
    ("You are capable of amazing things.", "💎"),
    ("Every difficulty is temporary.", "⏳"),
    ("Stay positive; the universe has a plan.", "🌟"),
    ("One day at a time is enough.", "🕰️"),
    ("Nah, some days are tough, but brighter ones are near.", "🌅"),
    ("You are doing better than you think.", "🙌"),
    ("Happiness is built in small steps.", "👣"),
    ("Storms don’t last forever.", "⛈️"),
    ("Keep trying, success is ahead.", "🏹"),
    ("Believe in progress, not perfection.", "⚡"),
    ("Nah, today might be messy, but tomorrow is clean.", "🧹"),
    ("Your journey is unique and valuable.", "🗺️"),
    ("Focus on the good in each day.", "🌼"),
    ("Tomorrow is another chance to shine.", "☀️"),
    ("Never underestimate your inner strength.", "💪"),
    ("Nah, rough patches happen, better days are coming.", "🌻"),
    ("Stay hopeful; every ending is a new beginning.", "🕊️"),
    ("You are worthy of all good things.", "💝"),
    ("Take breaks, but never give up completely.", "☕"),
    ("Nah, bad moments are temporary, the future is bright.", "🌤️"),
    ("Life is about learning, not just winning.", "📚"),
    ("Trust yourself and keep moving.", "🚶‍♂️"),
    ("Every effort counts, no matter how small.", "⭐"),
    ("Nah, setbacks happen, but your comeback is real.", "🏹"),
    ("Smile at progress, even if it’s tiny.", "😄"),
    ("Keep planting seeds; flowers take time to bloom.", "🌷"),
    ("Better days are closer than you think.", "🌞"),
    ("Nah, things feel heavy today, tomorrow will feel lighter.", "🎈")
]

@app.route("/")
def home():
    sentence, emoji = random.choice(positive_sentences)
    return Response(f"{sentence} {emoji}", mimetype="text/plain")

if __name__ == "__main__":
    host = os.environ.get("HOST", "0.0.0.0")
    port = int(os.environ.get("PORT", 10000))
    debug = os.environ.get("DEBUG", "True").lower() == "true"
    
    app.run(host=host, port=port, debug=debug)
