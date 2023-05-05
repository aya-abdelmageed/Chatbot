import re
import random_responses as response

def message_prob(user_message, recognised_w, single_res=False, required_w=[]):
    message_certainty = 0
    has_required_w = True

    
    for word in user_message:
        if word in recognised_w:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_w))

    # Checks that the required words are in the string
    for word in required_w:
        if word not in user_message:
            has_required_w = False
            break

    # Must either have the required words, or be a single response
    if has_required_w or single_res:
        return int(percentage * 100)
    else:
        return 0



#check the messages and get responses
def check(msg):
    high_prob_list = {}

    def res(bot_res, words_list, single_res = False, required_w=[]):
        nonlocal high_prob_list
        high_prob_list[bot_res] = message_prob(msg, words_list, single_res, required_w)

    
    #responses

    res('Hey there!', ['hello', 'hi', 'hey'], single_res=True)
    res('Bye, See you!', ['bye', 'goodbye'], single_res=True)
    res("you're welcome!", ['thank you', 'thanks'], single_res=True)
    res("I'm doing well, How about you?", ['how', 'are', 'you', 'doing'], required_w=['how', 'are', 'you'])
    res("Start by typing: 'How to learn 'what are you want to learn' on Google.", ["how", "to", "learn", "code", "coding", "apps"], required_w=['learn'])
    res("The pleasure is all mine!", ["nice", "to", "meet", "you"], required_w=["nice", "meet", "you"])
    res('me too!', ['i', 'love', 'code', 'palace'], required_w=['code', 'love'])

    # other responses
    res(response.ADVICE, ['give', 'advice'], required_w=['advice'])
    res(response.EATING, ['what', 'you', 'eat'], required_w=['you', 'eat'])
    res(response.INFO, ['give','information','info'], required_w=['information'])

    The_best_match = max(high_prob_list, key=high_prob_list.get)
     
    return response.random_responses() if high_prob_list[The_best_match] < 1 else The_best_match

#get messege from user
def get_res(user_in):
    split_in = re.split(r'\s+|[,;?!.-]\s*', user_in.lower())
    ans = check(split_in)
    return ans


while True:
    print('Bot: ' + get_res(input('You: ')))

 