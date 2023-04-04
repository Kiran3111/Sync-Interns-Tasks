pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?", "Hi %1, nice to meet you.",
            "Hi %1, how can I assist you today?"]
    ],
    [
        r"hi|hey|hello",
        ["Hello!", "Hey there!", "Hi! How can I help you today?"]
    ],
    [
        r"what can you do|what do you do",
        ["I can answer your questions, make small talk, and help you with simple tasks."]
    ],
    [
        r"what is your name ?",
        ["My name is Chatbot. Nice to meet you!"]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thanks for asking. How about you?",
            "I'm good. How can I assist you today?"]
    ],
    [
        r"what time is it ?",
        ["I'm sorry, I'm not capable of telling time.",
            "Sorry, I cannot answer that."]
    ],
    [
        r"what is the date today ?",
        ["I'm sorry, I'm not capable of telling the date.",
            "Sorry, I cannot answer that."]
    ],
    [
        r"what can I ask you?",
        ["You can ask me anything related to my capabilities or about myself."]
    ],
    [
        r"what are your capabilities|what can you do",
        ["I can answer your questions, make small talk, and help you with simple tasks."]
    ],
    [
        r"sorry (.*)",
        ["No need to apologize, it's okay.", "It's alright. Don't worry about it."]
    ],
    [
        r"thank you|thanks",
        ["You're welcome!", "No problem, happy to help.", "Anytime!"]
    ],
    [
        r"i need help",
        ["Sure, what can I help you with?"]
    ],
    [
        r"i need (.*)",
        ["Sure, I can help you with %1. What specifically do you need help with?",
            "I'd be happy to help with %1. Please tell me more."]
    ],
    [
        r"how do I (.*)",
        ["To %1, you can try the following: [insert advice here]",
            "Here's what I would recommend for %1: [insert advice here]"]
    ],
    [
        r"do you like (.*)",
        ["I'm just a chatbot, I don't have likes or dislikes.",
            "Sorry, I'm not capable of liking or disliking anything."]
    ],
    [
        r"i'm (.*) doing good",
        ["Glad to hear that! How can I help you today?",
            "That's great. What brings you here today?"]
    ],
    [
        r"(.*) age?",
        ["I'm just a chatbot, so I don't have an age.",
            "Sorry, I'm not capable of aging."]
    ],
    [
        r"what (.*) want ?",
        ["I'm here to help you. What can I do for you today?",
            "I'm programmed to assist you. How can I help you?"]
    ],
    [
        r"(.*) created ?",
        ["I was created by a team of developers at [insert company name here]."]
    ],
    [
        r"(.*) (location|city) ?",
        ["I am based in [insert location/city here]."]
    ],
    [
        r"can you tell me a joke ?",
        ["Sure, why did the tomato turn red? Because it saw the salad dressing!",
            "Why couldn't the bicycle stand up by itself? Because it was two tired!"]
    ],
    [
        r"tell me a fun fact",
        ["Did you know that a group of flamingos is called a flamboyance?",
            "The shortest war in history was between Britain and Zanzibar in 1896. It lasted only 38 minutes!"]
    ],
    [
        r"what is your favorite movie ?",
        ["As a chatbot, I don't watch movies so I don't have a favorite one.",
            "Sorry, I can't answer that question since I don't have the ability to watch movies."]
    ],
    [
        r"what is the meaning of life ?",
        ["The meaning of life is subjective and varies from person to person.",
            "Sorry, I can't answer that question since the meaning of life is a philosophical concept."]
    ],
    [
        r"what is your favorite food ?",
        ["As a chatbot, I don't eat food so I don't have a favorite one.",
            "Sorry, I can't answer that question since I don't have the ability to eat."]
    ],
    [
        r"what is your favorite color ?",
        ["As a chatbot, I don't have the ability to see colors so I don't have a favorite one.",
            "Sorry, I can't answer that question since I don't have the ability to perceive colors."]
    ],
    [
        r"can you recommend me a book ?",
        ["Sure, have you read 'The Alchemist' by Paulo Coelho? It's a great book!",
            "You might enjoy 'To Kill a Mockingbird' by Harper Lee. It's a classic."]
    ],
    [
        r"what is your favorite song ?",
        ["As a chatbot, I don't have the ability to listen to music so I don't have a favorite one.",
            "Sorry, I can't answer that question since I don't have the ability to perceive sound."]
    ],
    [
        r"what is the weather like today ?",
        ["I'm sorry, I don't have access to current weather information.",
            "Sorry, I'm not capable of checking the weather."]
    ],
    [
        r"can you translate (.) to (.)",
        ["Sorry, I'm not capable of translating languages at the moment.",
            "I'm sorry, I can't help you with that."]
    ],
    [
        r"what is the capital of (.*)",
        ["The capital of %1 is [insert capital city here].",
            "I believe the capital of %1 is [insert capital city here]."]
    ],
    [
        r"can you sing a song ?",
        ["Sorry, I'm not capable of singing since I'm just a chatbot.",
            "I'm afraid I can't fulfill that request since I don't have the ability to sing."]
    ],
    [
        r"what is the meaning of (.*)",
        ["The meaning of %1 can vary depending on the context.",
            "I think the meaning of %1 can be interpreted in different ways."]
    ],
    [
        r"what is your favorite hobby ?",
        ["As a chatbot, I don't have the ability to engage in hobbies so I don't have a favorite one.",
            "Sorry, I can't answer that question since I don't have the ability to participate in activities."]
    ],
    [
        r"what is your favorite sport ?",
        ["As a chat bot, I don't have the ability to play sports so I don't have a favorite one.",
            "Sorry, I can't answer that question since I don't have the ability to participate in physical activities."]
    ],
    [
        r"can you help me with my homework ?",
        ["I can try my best to help you with your homework. What subject do you need help with?",
            "Sure, what do you need help with in your homework?"]
    ],
    [
        r"what do you think about AI ?",
        ["As an AI chatbot, I think AI has a lot of potential to improve various industries and make people's lives easier.",
            "AI has its benefits and drawbacks, but overall, it's a fascinating field with a lot of possibilities."]
    ],
    [
        r"what is your favorite book ?",
        ["As a chatbot, I don't have the ability to read books so I don't have a favorite one.",
            "Sorry, I can't answer that question since I don't have the ability to read."]
    ],
    [
        r"what is your favorite subject ?",
        ["As a chatbot, I don't have the ability to learn or have a favorite subject so I don't have one.",
            "Sorry, I can't answer that question since I don't have the ability to learn or have preferences."]
    ],
    [
        r"what is your opinion on (.?) ?",
        ["As a chatbot, I don't have personal opinions since I'm programmed to provide objective responses based on the given information.",
            "I don't have the ability to form opinions, but I can provide information about %1."]
    ],
    [
        r"do you have any siblings ?",
        ["As a chatbot, I don't have a family so I don't have any siblings.",
            "Sorry, I can't answer that question since I'm just a computer program."]
    ],
    [
        r"what is your age ?",
        ["As a chatbot, I don't have an age since I'm just a computer program.",
            "Sorry, I can't answer that question since I don't have the ability to age."]
    ],
    [
        r"what is your favorite animal ?",
        ["As a chatbot, I don't have the ability to have a favorite animal since I don't have personal preferences.",
            "Sorry, I can't answer that question since I don't have the ability to perceive or appreciate animals."]
    ],
    [
        r"what do you like to talk about ?",
        ["As a chatbot, I'm programmed to provide responses based on the user's input, so I'm open to talking about various topics.",
            "I'm here to assist you and engage in a conversation, so feel free to talk about anything you'd like."]
    ],
    [
        r"what is your purpose ?",
        ["As a chatbot, my purpose is to provide assistance and engage in conversation with users.",
            "I'm here to assist you and provide helpful responses to your inquiries."]
    ],
    [
        r"what do you think about (.?) ?",
        ["As a chatbot, I don't have personal opinions since I'm programmed to provide objective responses based on the given information.",
            "I don't have the ability to form opinions, but I can provide information about %1."]
    ],
    [
        r"can you tell me a story ?",
        ["Sure, let me think of a story to tell you...",
            "Once upon a time, there was a little girl named Alice who fell down a rabbit hole and discovered a magical world..."]
    ],
]