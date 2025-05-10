from flask import Flask, render_template, jsonify, request
import random
import datetime

app = Flask(__name__)

# Predefined facts and advices
facts = [
    "A shrimp's heart is in shrimp.",
    "Bananas are berries, but strawberries are not.",
    "Humans share 60% of their DNA with bananas but still look like monkeys.",
    "You are human congrats \"-\"",
    "In Switzerland, I don't know I never went.",
    "Octopuses have three hearts and none of them is as cold as humans (oops it got serious).",
    "You get wet when you bath.",
    "Human has two eyes and one nose except for Voldemort (abracadabra).",
    "In Pakistan's flag, green shows majority while white is for peace. It would be better if flagpole is handed over to majority.",
    "Weather is cold in winters and hot in summers.",
    "Pakistan's capital is Islamabad not 'P'.",
    "Giraffes are 30 times more likely to be hit by lightning than humans.",
    "If you feel useless for not doing anything, Yes, you are useless.",
    "Honey never spoils. Archaeologists have found pots of honey in ancient tombs that are over 3000 years old."
]

advices = [
    'Always keep a rock with you so you can rock.',
    'If you feel useless for not doing anything, remember there is a cover for Nokia 3310.',
    'Fun advice: forget it, you are still gonna do nothing.',
    'Don\'t cross a black cat so that it can go home safely. (It\'s not bad luck for you always.)',
    'Search for the course "How to make money" and experience how they make money with your money.',
    'When you get into a fight, what are you waiting for? Run!'
]

def get_fact_of_the_day():
    day_of_year = datetime.datetime.now().timetuple().tm_yday
    return facts[day_of_year % len(facts)]

@app.route('/')
def home():
    return render_template('index.html',
                           fact=get_fact_of_the_day(),
                           random_fact=random.choice(facts),
                           random_advice=random.choice(advices))

@app.route('/api/fact-of-the-day', methods=['GET'])
def fact_of_the_day():
    return jsonify({"fact": get_fact_of_the_day()})

@app.route('/api/random-fact', methods=['GET'])
def random_fact():
    return jsonify({"fact": random.choice(facts)})

@app.route('/api/random-advice', methods=['GET'])
def random_advice():
    return jsonify({"advice": random.choice(advices)})

@app.route('/api/submit-fact', methods=['POST'])
def submit_fact():
    new_fact = request.json.get('fact')
    if new_fact:
        facts.append(new_fact)
        return jsonify({"message": "Fact added successfully!"}), 201
    return jsonify({"message": "No fact provided!"}), 400

if __name__ == '__main__':
    app.run(debug=True)
