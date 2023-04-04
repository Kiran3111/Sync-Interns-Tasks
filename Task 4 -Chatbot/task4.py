import requests
from train import pairs
from nltk.chat.util import Chat, reflections

chatbot = Chat(pairs, reflections)

def ask_question(question):
    bot_response = chatbot.respond(question)
    return bot_response


def joke():
    url = "https://bit.ly/3Ga62sP"
    response = requests.get(url)
    data = response.json()
    return data["joke"]


def fact():
    url = "https://uselessfacts.jsph.pl/api/v2/facts/random?language=en"
    response = requests.get(url)
    data = response.json()
    return data["text"]


def chat(prompt):
    try:
        if prompt.lower() in common_prompts.keys():
            print(f"\nChatBot> {common_prompts[prompt.lower()]}")
        elif prompt.lower() == "tell me a joke":
            print(f"\nChatBot> {joke()}")
        elif prompt.lower() == "tell me a fact":
            print(f"\nChatBot> {fact()}")
        else:
            response = ask_question(prompt)
            print(f"\nChatBot> {response}")
    except Exception as err:
        print(f"\nThere is an error in the bot or openai api. Error : {err}")


common_prompts = {
    "hi": "Hello! How can I help you?",
    "hello": "Hello there! Is there anything I can help you with?",
    "hey": "Hey Greetings!, I would love to help you if you have any problem?",
    "how are you": "I'm doing well, thank you for asking. How can I assist you today?",
    "whats up": "Not much, how about you? Do you have a question or need help with something?",
    "good morning": "Good morning! What brings you here today?",
    "good afternoon": "Good afternoon! How can I be of assistance?",
    "good evening": "Good evening! Is there anything I can help you with?",
    "how can you help me": "I can help you with a variety of tasks, such as answering questions or providing information. What do you need assistance with?",
    "what is your name": "My name is Chatbot, how can I assist you today?"
}


print("\nChatBot> Hello, I am AI Chat Bot, ask me any questions you want...")
while True:
    chat(input("\nYou > "))