import random

EATING = "As I'm a bot! I can't eat anything"
ADVICE = "If I were you, I would go to the internet 'Google' and type exactly what you wrote there!"
INFO = "You can search on Google for more information."

def random_responses():
    random_res = ["Oh! It appears you wrote something I don't understand yet",
           "I can't answer that yet, please try asking something else.",
           "Can you please explain it?",
           "Please try writing something more descriptive.",
           "Oh! It appears you wrote something I don't understand yet.",
           "What does that mean?",
           "Do you mind trying to rephrase that?",
           "sorry, I don't know."
           ][random.randrange(8)]
    
    return random_res

