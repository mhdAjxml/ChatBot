import re
import Longresponse_package as long
def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dic
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses -------------------------------------------------------------------------------------------------------
    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo','bot'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['doing'], required_words=['doing'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Thank you!', ['great','good','outstanding','best','awsome','stunning' ],single_response=True)
    response('Iam PLUTO', ['name'],single_response=True)
    response('I know only english',['language','speak','tounge','dialect'],required_words=['language','speak'])
    response('I like to feel useful , tell me what I can do for you?',['hobby','hobbies','activities','activity','leisure','entertainment','pastime','intrest','timepass','like'],required_words=['hobby','activity','entertainment','like'],single_response=True)
    response('I am PLUTO ,I\'m here to help you',['help','assistance','guidance','solution','support'],required_words=['help'])
    response('I\'m having a great day so far',['day'],single_response=True)
    response('Legends  made me!!',['made','master','created','creator'],single_response=True)
    response('I have lot more skills,what do you want?',['skills','talents','efficiency','capability','talent'],single_response=True)
    response('I\'m living in your PC :)',['stay','live','occupy','reside'],single_response=True)
    response('I was found on 23rd Feb,I\'ll help you forever',['age','old','span'],single_response=True)
    response('Don\'t worry I\'m there for you',['sad','fear','depressed','scared','lonely','alone','depression'],single_response=True)
    response('I can feel you 😊',['happy','joy','angry','sorrow','excited','upset'],single_response=True)
    response('I too adore you',['i','love','you'],required_words=['i','love','you'])
    response('I\'m Fine doing good',['how','are','you'],required_words=['how','are','you'])







    # Longer responses
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])
    response(long.x(), ['time'],single_response=True)
    response(long.weather() ,['climate','temperature','weather'],single_response=True)
    response(long.os_id(),['system','config','configuraion','specs','specifications','os','operating'],single_response=True)
   # response(long.Sleep(),['rest','sleep','down'],single_response=True)

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


# Testing the response system
while True:
    print('PLUTO: ' + get_response(input('You: ')))
