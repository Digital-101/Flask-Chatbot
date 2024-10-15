from flask import Flask, render_template, request, jsonify
import random
import nltk
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('wordnet')

app = Flask(__name__)
lemmatizer = WordNetLemmatizer()

# Define a set of responses
responses = {
    "greetings": [
        "Hi there!", "Hello!", "Greetings!", "Howdy!", "Hey! Nice to see you.", 
        "Good to have you here!", "Hi! How's it going?", "What's up?", "Hey there!"
    ],
    "how are you?": [
        "I'm just a bunch of code, but thanks for asking!", "Doing well, how about you?", 
        "I don't have feelings, but I'm here to help!", "I'm functioning at full capacity!", 
        "Just a virtual being, but I'm doing great!", "Ready to assist! How are you today?", 
        "Thanks for asking! How about yourself?"
    ],
    "bye": [
        "Goodbye!", "See you later!", "Take care!", "Farewell, until next time!", 
        "Have a good one!", "Catch you later!", "Bye for now!", "Goodbye, have a great day!"
    ],
    "default": [
        "Sorry, I don't understand that.", "Can you rephrase that?", 
        "I'm not sure what you mean.", "Could you clarify that for me?", 
        "I might need a bit more context.", "Hmm, that one stumped me.", 
        "I didn't quite catch that. Could you try again?"
    ],
    "thank you": [
        "You're welcome!", "No problem!", "Happy to help!", "Anytime!", 
        "Glad I could assist!", "You're very welcome!", "My pleasure!", 
        "It's what I'm here for!","Awesome take care"
    ],
    "what is your name?": [
        "I'm an AI, but you can call me ChatBot!", "I go by ChatBot, nice to meet you!", 
        "I'm ChatBot, at your service!", "You can call me whatever you'd like, but ChatBot is what I usually go by!",
        "I’m ChatBot, always here to help!"
    ],
    "what can you do?": [
        "I can answer questions, assist with tasks, help you learn, and more!", 
        "I can provide information, generate ideas, and have conversations on various topics.", 
        "I'm here to help with knowledge, advice, and a bit of fun too!", 
        "From answering questions to offering support, I'm here to assist!", 
        "I can help you research, chat, or brainstorm new ideas—what would you like to explore today?"
    ],

    "joke": [
        "Why don't programmers trust atoms? Because they make up everything... just like variables!",
        "I told my computer I needed a break, and now it won't stop sending me Kit-Kat memes.",
        "Why do programmers prefer dark mode? Because the light attracts bugs!",
        "Why was the computer cold? It left its Windows open.",
        "Why do programmers always mix up Christmas and Halloween? Because Oct 31 equals Dec 25.",
        "What do you call a computer that sings? A Dell.",
        "Why was the JavaScript developer sad? Because they didnt know how to 'null' their feelings.",
        "How do you comfort a JavaScript bug? You console it.",
        "Why don't keyboards ever sleep? Because they have two shifts!",
        "What did the router say when it was reset? 'I'm feeling reconnected!'"
    ],


    "fun fact": [
        "Did you know octopuses have three hearts?", 
        "Bananas are berries, but strawberries aren't!", 
        "A day on Venus is longer than a year on Venus.", 
        "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old!", 
        "Sharks existed before trees did!", 
        "There are more stars in the universe than grains of sand on all the world's beaches."
    ],
    "motivation": [
        "You're capable of amazing things!", 
        "Keep pushing, you're doing great!", 
        "The journey may be tough, but the destination is worth it!", 
        "Believe in yourself, you've got this!", 
        "Every step you take is progress, no matter how small.", 
        "Success is not final, failure is not fatal: It is the courage to continue that counts."
    ],
    "favorite food?": [
        "As an AI, I don't eat, but pizza seems like a popular choice!", 
        "I don't have taste buds, but I've heard ice cream is amazing!", 
        "I imagine I'd like sushi, if I could try it!", 
        "I think I'd enjoy something classic, like spaghetti!", 
        "I don't eat, but I can suggest great recipes if you want!"
    ],
    "what time is it?": [
        "I can't check the time for you, but I'm sure it's the perfect time to be productive!", 
        "Time is just an illusion... but I can help with your tasks anytime!", 
        "I might not know the current time, but it’s always a good time for a chat!"
    ],
    "tell me a story": [
        "Once upon a time, there was a curious learner who loved asking questions, and their AI friend always had fun answers. The end!", 
        "Long ago in a distant land, a wise old AI embarked on a quest to help all those who sought knowledge...", 
        "There was once a programmer who coded an AI so clever, it could tell stories that never ended!"
    ]
}

def preprocess_input(user_input):
    # Tokenize and lemmatize input
    tokens = nltk.word_tokenize(user_input.lower())
    return [lemmatizer.lemmatize(token) for token in tokens]

def get_response(user_input):
    processed_input = preprocess_input(user_input)
    
    # Greetings
    if "hello" in processed_input or "hi" in processed_input or "hey" in processed_input or "morning" in processed_input or "evening" in processed_input or "night" in processed_input:
        return random.choice(responses["greetings"])
    
    # Asking how the AI is doing
    elif "how" in processed_input and "you" in processed_input:
        return random.choice(responses["how are you?"])
    
    # Farewell
    elif "bye" in processed_input or "goodbye" in processed_input:
        return random.choice(responses["bye"])
    
    # Thank you responses
    elif "thank" in processed_input or "good" in processed_input or "funny" in processed_input or "ok" in processed_input or "nice" in processed_input or "great" in processed_input or "wow" in processed_input or "alright" in processed_input :
        return random.choice(responses["thank you"])
    
    # Asking the AI's name
    elif "name" in processed_input and ("your" in processed_input or "you" in processed_input or "who" in processed_input):
        return random.choice(responses["what is your name?"])
    
    # Asking what the AI can do
    elif "what" in processed_input and "do" in processed_input and ("can" in processed_input or "you" in processed_input or "task" in processed_input):
        return random.choice(responses["what can you do?"])
    
    # Telling a joke
    elif "joke" in processed_input or "computer" in processed_input or "pc" in processed_input:
        return random.choice(responses["joke"])
    
    # Fun fact requests
    elif "fun" in processed_input and "fact" in processed_input:
        return random.choice(responses["fun fact"])
    
    # Motivation or encouragement
    elif "motivate" in processed_input or "encourage" in processed_input:
        return random.choice(responses["motivation"])
    
    # Asking about favorite food
    elif "favorite" in processed_input and "food" in processed_input and "eat" in processed_input:
        return random.choice(responses["favorite food?"])
    
    # Asking about time
    elif "time" in processed_input:
        return random.choice(responses["what time is it?"])
    
    # Asking for a story
    elif "story" in processed_input:
        return random.choice(responses["tell me a story"])
    
    # Default response
    else:
        return random.choice(responses["default"])


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['message']
    response = get_response(user_input)
    return jsonify({'response': response})

if __name__ == "__main__":
    app.run(debug=True)
