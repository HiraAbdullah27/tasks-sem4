import nltk
nltk.download('punkt')
nltk.download('vader_lexicon')

# Import packages
from nltk.chat.util import Chat, reflections
from nltk.sentiment import SentimentIntensityAnalyzer
import gradio as gr

# Define chatbot pairs
pairs = [
    [r'(?i).*hello.*|.*hi.*|.*hey.*',
     ['Hello! How can I assist you?',
      'Hi there! Do you need help with anything?',
      'Hey! Welcome to the Restaurant.']],

    [r'(?i).*menu.*|.*list.*|.*dishes.*|.*food.*',
     ['Here is the menu:\nDish1: ₹100\nDish2: ₹150\nDish3: ₹200']],

    [r'(?i).*open.*time.*|.*hours.*|.*when.*open.*',
     ['We are open from 9 AM to 10 PM every day.']],

    [r'(?i).*location.*|.*where.*located.*|.*address.*',
     ['We are located at 123 Main Street, YourCity.']],

    [r'(?i).*book.*table.*|.*reservation.*|.*reserve.*',
     ['You can book a table by calling us at 123-456-7890.']],

    [r'(?i).*deliver.*|.*delivery.*available.*',
     ['Yes, we offer delivery through our app and popular delivery services.']],

    [r'(?i).*payment.*methods.*|.*pay.*with.*|.*accept.*card.*',
     ['We accept cash, cards, and mobile payments.']],

    [r'(?i).*special.*|.*offers.*|.*deal.*',
     ['Today’s special is Grilled Salmon with Lemon Butter Sauce.']],

    [r'(?i).*thank.*|.*thanks.*',
     ['You’re welcome!', 'Glad to assist you.']],

    [r'(?i).*bye.*|.*goodbye.*|.*see you.*',
     ['Goodbye! Have a great day!', 'See you soon at our restaurant!']]
]

# Set up chatbot and sentiment analyzer
chatbot = Chat(pairs, reflections)
sia = SentimentIntensityAnalyzer()

# Sentiment function
def analyze_sentiment(text):
    score = sia.polarity_scores(text)
    compound = score['compound']
    if compound >= 0.05:
        return "😊 Positive"
    elif compound <= -0.05:
        return "☹️ Negative"
    else:
        return "😐 Neutral"

# Combined chatbot and sentiment analyzer
def interact(user_input, mode):
    if mode == "Chat":
        response = chatbot.respond(user_input)
        return response if response else "I'm sorry, I don't understand that."
    else:
        return f"Sentiment Analysis: {analyze_sentiment(user_input)}"

# Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("## 🍽️ Restaurant ChatBot with Sentiment Analysis")
    gr.Markdown("Type your query below and select a mode.")

    with gr.Row():
        user_input = gr.Textbox(label="Your Message")
        mode = gr.Radio(choices=["Chat", "Sentiment"], label="Mode", value="Chat")
    
    output = gr.Textbox(label="Bot Response")
    submit_btn = gr.Button("Submit")

    submit_btn.click(fn=interact, inputs=[user_input, mode], outputs=output)

demo.launch()
