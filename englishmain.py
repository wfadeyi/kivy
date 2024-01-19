# English Lessons Program

import tkinter as tk
from tkinter import messagebox
import os, sys, subprocess, time
from datetime import date
import allquestions

##from englishtest import *


LARGE_FONT = ("Verdana", 12)

# Paste code of englishtest.py
'''
Create template for tests in tense and concord
'''

import random, json, os


class Test:

    verb_inflections = {

        'abide':['abide', 'abides', 'abiding', 'abided', 'abided'], 
'beat':['beat', 'beats', 'beating', 'beat', 'beaten'], 
'begin':['begin', 'begins', 'beginning', 'began', 'begun'], 
'bend':['bend', 'bends', 'bending', 'bent', 'bent'], 
'bet':['bet', 'bets', 'betting', 'bet', 'bet'], 
'bid':['bid', 'bids', 'bidding', 'bid', 'bid'], 
'bind':['bind', 'binds', 'binding', 'bound', 'bound'], 
'bite':['bite', 'bites', 'biting', 'bit', 'bitten'], 
'bleed':['bleed', 'bleeds', 'bleeding', 'bled', 'bled'], 
'blow':['blow', 'blows', 'blowing', 'blew', 'blown'], 
'break':['break', 'breaks', 'breaking', 'broke', 'broken'], 
'breed':['breed', 'breeds', 'breeding', 'bred', 'bred'], 
'bring':['bring', 'brings', 'bringing', 'brought', 'brought'], 
'build':['build', 'builds', 'building', 'built', 'built'], 
'burst':['burst', 'bursts', 'bursting', 'burst', 'burst'], 
'buy':['buy', 'buys', 'buying', 'bought', 'bought'], 
'cast':['cast', 'casts', 'casting', 'cast', 'cast'], 
'catch':['catch', 'catches', 'catching', 'caught', 'caught'], 
'choose':['choose', 'chooses', 'choosing', 'chose', 'chosen'], 
'cling':['cling', 'clings', 'clinging', 'clung', 'clung'], 
'clothe':['clothe', 'clothes', 'clothing', 'clothed', 'clothed'], 
'come':['come', 'comes', 'coming', 'came', 'come'], 
'cost':['cost', 'costs', 'costing', 'cost', 'cost'], 
'creep':['creep', 'creeps', 'creeping', 'crept', 'crept'], 
'cut':['cut', 'cuts', 'cutting', 'cut', 'cut'], 
'dare':['dare', 'dares', 'daring', 'dared', 'dared'], 
'deal':['deal', 'deals', 'dealing', 'dealt', 'dealt'], 
'dig':['dig', 'digs', 'digging', 'dug', 'dug'], 
'do':['do', 'does', 'doing', 'did', 'done'], 
'draw':['draw', 'draws', 'drawing', 'drew', 'drawn'], 
'drink':['drink', 'drinks', 'drinking', 'drank', 'drunk'], 
'drive':['drive', 'drives', 'driving', 'drove', 'driven'], 
'dwell':['dwell', 'dwells', 'dwelling', 'dwelt', 'dwelt'], 
'eat':['eat', 'eats', 'eating', 'ate', 'eaten'], 
'fall':['fall', 'falls', 'falling', 'fell', 'fallen'], 
'feed':['feed', 'feeds', 'feeding', 'fed', 'fed'], 
'feel':['feel', 'feels', 'feeling', 'felt', 'felt'], 
'fight':['fight', 'fights', 'fighting', 'fought', 'fought'], 
'find':['find', 'finds', 'finding', 'found', 'found'], 
'flee':['flee', 'flees', 'fleeing', 'fled', 'fled'], 
'fling':['fling', 'flings', 'flinging', 'flung', 'flung'], 
'fly':['fly', 'flies', 'flying', 'flew', 'flown'], 
'forbid':['forbid', 'forbids', 'forbidding', 'forbade', 'forbidden'], 
'forget':['forget', 'forgets', 'forgetting', 'forgot', 'forgotten'], 
'freeze':['freeze', 'freezes', 'freezing', 'froze', 'frozen'], 
'give':['give', 'gives', 'giving', 'gave', 'given'],  
'go':['go', 'goes', 'going', 'went', 'gone'], 
'grind':['grind', 'grinds', 'grinding', 'ground', 'ground'], 
'grow':['grow', 'grows', 'growing', 'grew', 'grown'], 
'hang':['hang', 'hangs', 'hanging', 'hung ', 'hung'], 
'hang':['hang', 'hangs', 'hanging', 'hanged', 'hanged'], 
'have':['have', 'has', 'having', 'had', 'had'], 
'hear':['hear', 'hears', 'hearing', 'heard', 'heard'], 
'heave':['heave', 'heaves', 'heaving', 'heaved', 'heaved'], 
'hide':['hide', 'hides', 'hiding', 'hid', 'hidden'], 
'hit':['hit', 'hits', 'hitting', 'hit', 'hit'], 
'hold':['hold', 'holds', 'holding', 'held', 'held'], 
'hurt':['hurt', 'hurts', 'hurting', 'hurt', 'hurt'], 
'keep':['keep', 'keeps', 'keeping', 'kept', 'kept'], 
'kneel':['kneel', 'kneels', 'kneeling', 'knelt', 'knelt'], 
'know':['know', 'knows', 'knowing', 'knew', 'known'], 
'lay':['lay', 'lays', 'laying', 'laid', 'laid'], 
'lead':['lead', 'leads', 'leading', 'led', 'led'], 
'leave':['leave', 'leaves', 'leaving', 'left', 'left'], 
'lend':['lend', 'lends', 'lending', 'lent', 'lent'], 
'let':['let', 'lets', 'letting', 'let', 'let'], 
'lie':['lie', 'lies', 'lying', 'lay', 'lain'], 
'lose':['lose', 'loses', 'losing', 'lost', 'lost'], 
'make':['make', 'makes', 'making', 'made', 'made'], 
'mean':['mean', 'means', 'meaning', 'meant', 'meant'], 
'meet':['meet', 'meets', 'meeting', 'met', 'met'], 
'melt':['melt', 'melts', 'melting', 'melted', 'melted'], 
'pay':['pay', 'pays', 'paying', 'paid', 'paid'], 
'put':['put', 'puts', 'putting', 'put', 'put'], 
'read':['read', 'reads', 'reading', 'read', 'read'], 
'ride':['ride', 'rides', 'riding', 'rode', 'ridden'], 
'ring':['ring', 'rings', 'ringing', 'rang', 'rung'], 
'rise':['rise', 'rises', 'rising', 'rose', 'risen'], 
'run':['run', 'runs', 'running', 'ran', 'run'], 
'say':['say', 'says', 'saying', 'said', 'said'], 
'see':['see', 'sees', 'seeing', 'saw', 'seen'], 
'seek':['seek', 'seeks', 'seeking', 'sought', 'sought'], 
'sell':['sell', 'sells', 'selling', 'sold', 'sold'], 
'send':['send', 'sends', 'sending', 'sent', 'sent'], 
'set':['set', 'sets', 'setting', 'set', 'set'], 
'shake':['shake', 'shakes', 'shaking', 'shook', 'shaken'], 
'shave':['shave', 'shaves', 'shaving', 'shaved', 'shaved'], 
'shed':['shed', 'sheds', 'shedding', 'shed', 'shed'], 
'shine':['shine', 'shines', 'shining', 'shone', 'shone'], 
'shoot':['shoot', 'shoots', 'shooting', 'shot', 'shot'], 
'shut':['shut', 'shuts', 'shutting', 'shut', 'shut'], 
'sing':['sing', 'sings', 'singing', 'sang', 'sung'], 
'sink':['sink', 'sinks', 'sinking', 'sank', 'sunk'], 
'sit':['sit', 'sits', 'sitting', 'sat', 'sat'], 
'slay':['slay', 'slays', 'slaying', 'slew', 'slain'], 
'sleep':['sleep', 'sleeps', 'sleeping', 'slept', 'slept'], 
'slide':['slide', 'slides', 'sliding', 'slid', 'slid'], 
'sling':['sling', 'slings', 'slinging', 'slung', 'slung'], 
'slink':['slink', 'slinks', 'slinking', 'slunk', 'slunk'], 
'slit':['slit', 'slits', 'slitting', 'slit', 'slit'], 
'speak':['speak', 'speaks', 'speaking', 'spoke', 'spoken'], 
'spend':['spend', 'spends', 'spending', 'spent', 'spent'], 
'spit':['spit', 'spits', 'spiting', 'spat', 'spat'], 
'split':['split', 'splits', 'splitting', 'split', 'split'], 
'spread':['spread', 'spreads', 'spreading', 'spread', 'spread'], 
'spring':['spring', 'springs', 'springing', 'sprang', 'sprung'], 
'stand':['stand', 'stands', 'standing', 'stood', 'stood'], 
'steal':['steal', 'steals', 'stealing', 'stole', 'stolen'], 
'stick':['stick', 'sticks', 'sticking', 'stuck', 'stuck'], 
'sting':['sting', 'stings', 'stinging', 'stung', 'stung'], 
'stink':['stink', 'stinks', 'stinking', 'stank', 'stunk'], 
'stride':['stride', 'strides', 'striding', 'strode', 'stridden'], 
'strike':['strike', 'strikes', 'striking', 'struck', 'struck'], 
'string':['string', 'strings', 'stringing', 'strung', 'strung'], 
'swear':['swear', 'swears', 'swearing', 'swore', 'sworn'], 
'sweep':['sweep', 'sweeps', 'sweeping', 'swept', 'swept'], 
'swim':['swim', 'swims', 'swimming', 'swam', 'swum'], 
'swing':['swing', 'swings', 'swinging', 'swung', 'swung'], 
'take':['take', 'takes', 'taking', 'took', 'taken'], 
'teach':['teach', 'teaches', 'teaching', 'taught', 'taught'], 
'tear':['tear', 'tears', 'tearing', 'tore', 'torn'], 
'tell':['tell', 'tells', 'telling', 'told', 'told'], 
'think':['think', 'thinks', 'thinking', 'thought', 'thought'], 
'throw':['throw', 'throws', 'throwing', 'threw', 'thrown'], 
'thrust':['thrust', 'thrusts', 'thrusting', 'thrust', 'thrust'], 
'tread':['tread', 'treads', 'treading', 'trod', 'trodden'], 
'wake':['wake', 'wakes', 'waking', 'woke', 'woken'], 
'wear':['wear', 'wears', 'wearing', 'wore', 'worn'], 
'weave':['weave', 'weaves', 'weaving', 'wove', 'woven'], 
'weep':['weep', 'weeps', 'weeping', 'wept', 'wept'], 
'win':['win', 'wins', 'winning', 'won', 'won'], 
'wind':['wind', 'winds', 'winding', 'wound', 'wound'], 
'work':['work', 'works', 'working', 'worked', 'worked'], 
'wring':['wring', 'wrings', 'wringing', 'wrung', 'wrung'], 
'write':['write', 'writes', 'writing', 'wrote', 'written'] 

        }

    timingIndicators = {

                  "Recurrent" : ["frequently", 'usually', 'often', "every day", "daily", "every week",
                                   "every now and then", 'every weekend', 'on weekends', 'on Mondays', 'on Sundays',
                                   'every Saturday', 'every Wednesday', 'from time to time', 'repeatedly', 'again and again', 'all the time', 'every time'],
                  'Current' : ['right now', 'at this moment', 'as we speak', 'at this very moment'],
                  'Past' : ['before now', 'one hour ago', 'two hours ago', 'three hours ago', 'earlier today',
                            'the day before yesterday', 'yesterday', 'last night', 'last week', 'last weekend',
                            'last month', 'last year', 'two days ago', 'three days ago', 'two weeks ago',
                            'three months ago'],
                  'Since' : ['since yesterday', 'since last night', 'since this morning', 'since last week',
                             'since last weekend', 'since last month', 'since last year',
                             'since the beginning of the year','since I was a child'],
                  'Future' : ['tomorrow', 'next time', 'in the future', 'next week', 'next year', 'next month',
                              'next Saturday', 'next Sunday', 'next Monday', 'next Friday', 'the day after tomorrow',
                              'next weekend', 'after now'],
                  'Already' : ['already', 'many times this week', 'today', 'several times this year',
                               'a few times this month'],
                  'At past time' : ['when you called me', 'by this time yesterday',
                                    'when you came in', 'by this time last year', 'when the rain started'],
                  'Before past event' : ['before you called me', 'before she arrived', 'before it rained',
                               'before that thing happened'],
                  'For past period' : ['for the past three days', 'for the past one week', 'for the past two months'],
                  'By future time' : ['by the time you arrive', 'by this time tomorrow', 'by the time the rain starts',
                                      'by 7 o\' clock tonight'],

                  'Never' : ['at all', 'at any time']
                  }


    subjectIndicators = {
                     'FirstSingular' : ['I'],
                     'SecondSingular' : ['You'],
                     'ThirdSingular' : ['He', 'She', 'My friend', 'The girl', 'That child', 'The boy'],
                     'FirstPlural' : ['We', 'All of us', 'My friend and I', 'Both of us', 'You and I', 'Some of us'],
                     'SecondPlural': ['You', 'All of you', 'Many of you', 'Both of you', 'Some of you', 'Many of you'],
                     'ThirdPlural' : ['They', 'My parents', 'My friends', 'The students', 'Our children']

                     }

    verbs_with_objects = {
        'go' : ['to the market', 'home', 'to that place', 'to school', 'there'],
        'come' : ['here', 'to this place', 'home', ' to Ibadan'],
        'buy' : ['food', 'bread', 'groundnuts', 'popcorn'],
        'eat' : ['food', 'rice', 'bread', 'yam', 'popcorn', 'groundnuts'],
        'read' : ['this book', 'that book'],
        'bring' : ['food to school'],
        'burn' : ['candles', 'food'],
        'choose' : ['good things'],
        'cut' : ['okro', 'wood'],
        'draw' : ['pictures'],
        'feel' : ['happy'],
        'forget' : ['things'],
        'keep' : ['quiet'],
        'learn' : ['English', 'songs'],
        'write' : ['messages'],
        'sweep' : ['the house', 'the floor'],
        'tell' : ['stories'],
        'wear' : ['native dresses'],
        'meet' : ['good people'],
        'ride' : ['bikes'],
        'see' : ['many people'],
        'spend' : ['money'],
        'spread' : ['good news']
        }


    verb_pool = ['eat', 'work', 'sleep', 'drink', 'sing',
                 'swim', 'speak']


    variable_states = ['angry', 'happy', 'sick', 'excited', 'quiet', 'cheerful']

    fixed_states = ['tall', 'gentle', 'beautiful', 'kind', 'strong', 'healthy', 'patient', 'nice',
                    'proud']

    variable_identities = ['architect', 'interpreter', 'politician', 'student', 'trader', 'agent',
                           'electrician','accountant', 'artist', 'dancer', 'musician', 'driver', 'teacher']

    
        


    
    def makejson(self, testcollection, folder):

        if not os.path.exists(folder):
            os.makedirs(folder)

        for i in range(len(testcollection)):

            json_file_path = f'{folder}/{self.topic}Exe{str(i+1)}.json'

            with open(json_file_path, 'w') as outfile:
                dictionary = {'questions_list':[], 'answers_list':[], 'options_list':[]}

                for j in range(len(testcollection[i])):
                    
                    dictionary['questions_list'].append(testcollection[i][j].question_string)
                    
                    

                    current_options = [testcollection[i][j].correct_option,
                               testcollection[i][j].wrong_option1,
                               testcollection[i][j].wrong_option2,
                               testcollection[i][j].wrong_option3,
                               testcollection[i][j].wrong_option4]

                    random.shuffle(current_options)

                    answer_index = current_options.index(testcollection[i][j].correct_option) + 1

                    dictionary['options_list'].append(current_options)
                    dictionary['answers_list'].append(answer_index)

                json.dump(dictionary, outfile)

                


class MultichoiceQuestion:

    def __init__(self):

        self.question_string      = ''
        self.correct_option       = ''
        self.options              = []
        self.wrong_option1        = ''
        self.wrong_option2        = ''
        self.wrong_option3        = ''
        self.wrong_option4        = ''
        self.topics               = []
        





'''
Program to test appropriate use of tense and concord

'''

class HasHappened(Test):

    topic = 'has happened'

   

    subList = list(Test.subjectIndicators.items())

    subList.append(subList[2] * 3) # adds more 3rd person singular members, to ensure better representation in question pool
                
    timingGroup = Test.timingIndicators['Already']

    def createaffirmative(self):

        question = MultichoiceQuestion()
        question.topics.append(self.topic)
        
        subjectGroup = random.choice(self.subList)

        subject = subjectGroup[1][0] if len(subjectGroup[1]) == 1 else random.choice(subjectGroup[1])

        timing = random.choice(self.timingGroup)

        verb = random.choice(self.verb_pool)


        verb_forms = self.verb_inflections[verb]
        
        if subjectGroup[0] == 'FirstSingular':

            question.correct_option = f'have {verb_forms[4]}' # choose the present perfect

            
            question.wrong_option1 = f'has {verb_forms[4]}' # I has done
            question.wrong_option2 = f'have {verb_forms[0]}' # I have do
            question.wrong_option3 = f'am {verb_forms[3]}' # I am did
            question.wrong_option4 = f'was {verb_forms[3]}' # I was did
                           
        elif subjectGroup[0] == 'ThirdSingular':
            
            question.correct_option = f'has {verb_forms[4]}' # choose the present perfect

            
            question.wrong_option1 = f'have {verb_forms[4]}' # He have done
            question.wrong_option2 = f'has {verb_forms[0]}' # He has do
            question.wrong_option3 = f'is {verb_forms[3]}' # He is did 
            question.wrong_option4 = f'was {verb_forms[3]}' # He was did

        else:
            
            question.correct_option = f'have {verb_forms[4]}' # choose the present perfect

            
            question.wrong_option1 = f'has {verb_forms[4]}' # You has done
            question.wrong_option2 = f'have {verb_forms[0]}' # You have do
            question.wrong_option3 = f'are {verb_forms[3]}' # You are did
            question.wrong_option4 = f'were {verb_forms[3]}' # You were did
  
        question.question_string = f'{subject} ______ {timing}.'


        return question




class Happens(Test):

    
    topic = 'happens'


    subList = list(Test.subjectIndicators.items())

    subList.append(subList[2] * 3) # adds more 3rd person singular members, to ensure better representation in question pool
                
    timingGroup = Test.timingIndicators['Recurrent']

    does_subjects = Test.subjectIndicators['ThirdSingular']

    do_subjects = {i:Test.subjectIndicators[i] for i in Test.subjectIndicators if i != 'ThirdSingular'}

    

    

    def createaffirmative(self):

        question = MultichoiceQuestion()
        question.topics.append(self.topic)
        
        subjectGroup = random.choice(self.subList)

        subject = random.choice(subjectGroup[1])

        timing = random.choice(self.timingGroup)

        verb = random.choice(self.verb_pool)

        verb_object = ''

        if verb in Test.verbs_with_objects:
            verb_object = f'{random.choice(Test.verbs_with_objects[verb])} '


        verb_forms = self.verb_inflections[verb]

                
        if subjectGroup[0] == 'FirstSingular':

            question.correct_option = verb_forms[0] # choose present simple - note could apply to other tenses correctly too

            
            question.wrong_option1 = f'am {verb_forms[0]}' # I am do
            question.wrong_option2 = f'{verb_forms[2]}' # I doing
            question.wrong_option3 = f'{verb_forms[1]}' # I does
            question.wrong_option4 = f'was {verb_forms[0]}' # I was do
                           
        elif subjectGroup[0] == 'ThirdSingular':
            
            question.correct_option = verb_forms[1]

            
            question.wrong_option1 = f'{verb_forms[2]}' # He doing
            question.wrong_option2 = f'{verb_forms[0]}' # He do
            question.wrong_option3 = f'is {verb_forms[1]}' # He is does
            question.wrong_option4 = f'is {verb_forms[0]}' # He is do


        else:
            
            question.correct_option = verb_forms[0] # choose present simple - note could apply to other tenses correctly too

            
            question.wrong_option1 = f'are {verb_forms[0]}' # You are do
            question.wrong_option2 = f'{verb_forms[2]}' # You doing
            question.wrong_option3 = f'{verb_forms[1]}' # You does
            question.wrong_option4 = f'was {verb_forms[0]}' # You was do

        question.question_string = f'{subject} ______ {verb_object}{timing}.'


        return question



    def createaffirmativesubject(self):

        question = MultichoiceQuestion()
        question.topics.append(self.topic)

        timing = random.choice(self.timingGroup)

        verb = random.choice(self.verb_pool)

        verb_object = ''

        if verb in Test.verbs_with_objects:
            verb_object = f'{random.choice(Test.verbs_with_objects[verb])} '



        verb_forms = self.verb_inflections[verb]
        
        current_verb_forms = [verb_forms[0], verb_forms[1]] # the relevant inflections for simple present tense

        verb = random.choice(current_verb_forms) # the inflection to be used in the current question

                
        if verb == current_verb_forms[0]: # the 'do' form

            

            question.correct_option = random.choice(random.choice(list(self.do_subjects.items()))[1])

            random.shuffle(self.does_subjects)
            question.wrong_option1 = self.does_subjects[0]
            question.wrong_option2 = self.does_subjects[1]
            question.wrong_option3 = self.does_subjects[2]
            question.wrong_option4 = self.does_subjects[3]
                           

        else:  # the 'does' form
            
            question.correct_option = random.choice(self.does_subjects)

            temp_list = list(self.do_subjects.items())
            random.shuffle(temp_list)

            question.wrong_option1 = temp_list[0][1][random.randrange(len(temp_list[0][1]))]

            question.wrong_option2 = temp_list[1][1][random.randrange(len(temp_list[1][1]))]

            question.wrong_option3 = temp_list[2][1][random.randrange(len(temp_list[2][1]))]

            question.wrong_option4 = temp_list[3][1][random.randrange(len(temp_list[3][1]))]

                           

        question.question_string = f'______ {verb} {verb_object}{timing}.'


        return question

    def test_timing_affirmative(self):

        question = MultichoiceQuestion()
        question.topics.append(self.topic)

        subjectGroup = random.choice(self.subList)

        subject = random.choice(subjectGroup[1])

        verb = random.choice(self.verb_pool)

        verb_object = ''

        if verb in Test.verbs_with_objects:
            verb_object = f'{random.choice(Test.verbs_with_objects[verb])} '



        verb_forms = self.verb_inflections[verb]

        
        if subjectGroup[0] == 'ThirdSingular':

            verb = verb_forms[1] # this changes the inflection to the 'does' form

        question.correct_option = random.choice(self.timingGroup) # choose a recurrent timing variant

        question.wrong_option1 = random.choice(Test.timingIndicators['Past'])
        question.wrong_option2 = random.choice(Test.timingIndicators['Since'])
        question.wrong_option3 = random.choice(Test.timingIndicators['At past time'])
        question.wrong_option4 = random.choice(Test.timingIndicators['For past period'])
            
        question.question_string = f'{subject} {verb} {verb_object}______.'


        return question
            


    def createtests(self, numfiles, numquestions):

        alltests = []

        for i in range(numfiles):

            alltests.append([])
            
            j = 1

            while True:
                alltests[i].append(self.createaffirmative())
                alltests[i].append(self.createaffirmativesubject())

                #alltests[i].append(self.test_timing_affirmative())


                j = j + 2

                if j >= numquestions:
                    break

                

        return alltests






class HadHappened(Test):
   
    topic = 'had happened'

    test_verbs = ['eat', 'work', 'read', 'run', 'sleep']

    subList = list(Test.subjectIndicators.items())

    subList.append(subList[2] * 3) # adds more 3rd person singular members, to ensure better representation in question pool
                
    timingGroup = Test.timingIndicators['Before past event']

    def createaffirmative(self):

        question = MultichoiceQuestion()
        question.topics.append(self.topic)
        
        subjectGroup = random.choice(self.subList)

        subject = subjectGroup[1][0] if len(subjectGroup[1]) == 1 else random.choice(subjectGroup[1])

        timing = random.choice(self.timingGroup)

        verb = random.choice(self.verb_pool)


        verb_forms = self.verb_inflections[verb]
        

                
        if subjectGroup[0] == 'FirstSingular':

            question.correct_option = f'had {verb_forms[4]}' # choose the past perfect

            
            question.wrong_option1 = f'have {verb_forms[4]}' # I have done
            question.wrong_option2 = f'will {verb_forms[0]}' # I will do
            question.wrong_option3 = f'am {verb_forms[2]}' # I am doing
            question.wrong_option4 = f'was {verb_forms[3]}' # I was did
                           
        elif subjectGroup[0] == 'ThirdSingular':
            
            question.correct_option = f'had {verb_forms[4]}' # choose the past perfect

            
            question.wrong_option1 = f'has {verb_forms[4]}' # He has done
            question.wrong_option2 = f'will {verb_forms[0]}' # He will do
            question.wrong_option3 = f'is {verb_forms[2]}' # He is doing 
            question.wrong_option4 = f'was {verb_forms[3]}' # He was did

        else:
            
            question.correct_option = f'had {verb_forms[4]}' # choose the past perfect

            
            question.wrong_option1 = f'have {verb_forms[4]}' # You have done
            question.wrong_option2 = f'will {verb_forms[0]}' # You will do
            question.wrong_option3 = f'are {verb_forms[2]}' # You are doing
            question.wrong_option4 = f'were {verb_forms[3]}' # You were did
  
        question.question_string = f'{subject} ______ {timing}.'


        return question



                    

    def createtests(self, numfiles, numquestions):

        alltests = []

        for i in range(numfiles):

            alltests.append([])
            
            for j in range(numquestions):
                alltests[i].append(self.createaffirmative())

        return alltests






class DoesHappen(Test):
    topic = 'does happen'

    subList = list(Test.subjectIndicators.items())

    subList.append(subList[2] * 3) # adds more 3rd person singular members, to ensure better representation in question pool
                
    timingGroup = Test.timingIndicators['Recurrent']

    does_subjects = Test.subjectIndicators['ThirdSingular']

    do_subjects = {i:Test.subjectIndicators[i] for i in Test.subjectIndicators if i != 'ThirdSingular'}

    

    

    def createaffirmative(self):

        question = MultichoiceQuestion()
        question.topics.append(self.topic)
        
        subjectGroup = random.choice(self.subList)

        subject = random.choice(subjectGroup[1])

        timing = random.choice(self.timingGroup)

        verb = random.choice(self.verb_pool)

        verb_object = ''

        if verb in Test.verbs_with_objects:
            verb_object = f'{random.choice(Test.verbs_with_objects[verb])} '

        verb_forms = []
        with open('SourceFolder/inflections1.txt', 'r') as infile:

            for line in infile:
                if line.strip().split('\t', 1)[0] == verb:

                    for form in line.strip().split('\t'):
                        verb_forms.append(form)
                    
                    break

                
        if subjectGroup[0] == 'FirstSingular':

            question.correct_option = f'do {verb_forms[0]}' # choose present simple - note could apply to other tenses correctly too

            
            question.wrong_option1 = f'am not {verb_forms[0]}' # I am not do
            question.wrong_option2 = f'are not {verb_forms[2]}' # I are not doing
            question.wrong_option3 = f'does {verb_forms[0]}' # I does do
            question.wrong_option4 = f'was not {verb_forms[0]}' # I was not do
                           
        elif subjectGroup[0] == 'ThirdSingular':
            
            question.correct_option = f'does {verb_forms[0]}'

            
            question.wrong_option1 = f'are not {verb_forms[2]}' # He are not doing
            question.wrong_option2 = f'do {verb_forms[0]}' # He do do
            question.wrong_option3 = f'was not {verb_forms[1]}' # He was not does
            question.wrong_option4 = f'is not {verb_forms[0]}' # He is not do


        else:
            
            question.correct_option = f'do {verb_forms[0]}' # choose present simple - note could apply to other tenses correctly too

            
            question.wrong_option1 = f'are not {verb_forms[0]}' # You are not do
            question.wrong_option2 = f'was not {verb_forms[2]}' # You was not doing
            question.wrong_option3 = f'does {verb_forms[0]}' # You does do
            question.wrong_option4 = f'was not {verb_forms[0]}' # You was not do

        question.question_string = f'{subject} ______ {verb_object}{timing}, I am sure.'


        return question



    def createaffirmativesubject(self):

        question = MultichoiceQuestion()
        question.topics.append(self.topic)

        timing = random.choice(self.timingGroup)

        verb = random.choice(self.verb_pool)

        verb_object = ''

        if verb in Test.verbs_with_objects:
            verb_object = f'{random.choice(Test.verbs_with_objects[verb])} '

        verb_forms = ['do', 'does'] # the relevant inflections for the negative

        verb = f'{random.choice(verb_forms)} {verb}' # the inflection to be used in the current question

                
        if not verb.startswith(verb_forms[1]): # the 'do' form

            

            question.correct_option = random.choice(random.choice(list(self.do_subjects.items()))[1])

            random.shuffle(self.does_subjects)
            question.wrong_option1 = self.does_subjects[0]
            question.wrong_option2 = self.does_subjects[1]
            question.wrong_option3 = self.does_subjects[2]
            question.wrong_option4 = self.does_subjects[3]
                           

        else:  # the 'does' form
            
            question.correct_option = random.choice(self.does_subjects)
            

            temp_list = list(self.do_subjects.items())
            random.shuffle(temp_list)

            question.wrong_option1 = temp_list[0][1][random.randrange(len(temp_list[0][1]))]

            question.wrong_option2 = temp_list[1][1][random.randrange(len(temp_list[1][1]))]

            question.wrong_option3 = temp_list[2][1][random.randrange(len(temp_list[2][1]))]

            question.wrong_option4 = temp_list[3][1][random.randrange(len(temp_list[3][1]))]

                           

        question.question_string = f'______ {verb} {verb_object}{timing}, I am very sure.'


        return question

    def test_timing_affirmative(self):

        question = MultichoiceQuestion()
        question.topics.append(self.topic)

        subjectGroup = random.choice(self.subList)

        subject = random.choice(subjectGroup[1])

        verb = random.choice(self.verb_pool)

        verb_object = ''

        if verb in Test.verbs_with_objects:
            verb_object = f'{random.choice(Test.verbs_with_objects[verb])} '

        verb_forms = []
        with open('SourceFolder/inflections1.txt', 'r') as infile:

            for line in infile:
                if line.strip().split('\t', 1)[0] == verb:

                    for form in line.strip().split('\t'):
                        verb_forms.append(form)
                    
                    break

        if subjectGroup[0] == 'ThirdSingular':

            verb = verb_forms[1] # this changes the inflection to the 'does' form

        question.correct_option = random.choice(self.timingGroup) # choose a recurrent timing variant

        question.wrong_option1 = random.choice(Test.timingIndicators['Past'])
        question.wrong_option2 = random.choice(Test.timingIndicators['Since'])
        question.wrong_option3 = random.choice(Test.timingIndicators['At past time'])
        question.wrong_option4 = random.choice(Test.timingIndicators['For past period'])
            
        question.question_string = f'{subject} {verb} {verb_object}______.'


        return question
            

    def createtests(self, numfiles, numquestions):

        alltests = []

        for i in range(numfiles):

            alltests.append([])
            
            j = 1

            while True:
                alltests[i].append(self.createaffirmative())
                alltests[i].append(self.createaffirmativesubject())

                #alltests[i].append(self.test_timing_affirmative())


                j = j + 2

                if j >= numquestions:
                    break

                

        return alltests



'''
Testing status verbs 

'''


class IsSo(Test):

    topic = 'is so'

    subList = list(Test.subjectIndicators.items())

    subList.append(subList[2] * 3) # adds more 3rd person singular members, to ensure better representation in question pool
                
    past_indicators = [i for i in Test.timingIndicators['Past'] if not ('year' in i or 'month' in i)]

    present_indicators = Test.timingIndicators['Current']

    all_timing = past_indicators + present_indicators

    
    


    

    

    def createaffirmative(self):

        question = MultichoiceQuestion()
        question.topics.append(self.topic)
        
        subjectGroup = random.choice(self.subList)

        subject = random.choice(subjectGroup[1])

        timing = random.choice(self.all_timing)

        state = random.choice(self.variable_states)


                
        if subjectGroup[0] == 'FirstSingular' and timing in self.present_indicators:

            question.correct_option = 'am'

            
            question.wrong_option1 = 'was'
            question.wrong_option2 = 'were'
            question.wrong_option3 = 'is'
            question.wrong_option4 = 'are'

        elif subjectGroup[0] == 'FirstSingular' and timing in self.past_indicators:

            question.correct_option = 'was'

            
            question.wrong_option1 = 'am'
            question.wrong_option2 = 'were'
            question.wrong_option3 = 'is'
            question.wrong_option4 = 'are'        
                           
        elif subjectGroup[0] == 'ThirdSingular' and timing in self.present_indicators:
            
            question.correct_option = 'is'

            
            question.wrong_option1 = 'am'
            question.wrong_option2 = 'were'
            question.wrong_option3 = 'was'
            question.wrong_option4 = 'are'        


        elif subjectGroup[0] == 'ThirdSingular' and timing in self.past_indicators:
            
            question.correct_option = 'was'

            
            question.wrong_option1 = 'am'
            question.wrong_option2 = 'were'
            question.wrong_option3 = 'is'
            question.wrong_option4 = 'are'        

        elif timing in self.present_indicators: # You, We, They, present tense
            
            question.correct_option = 'are'

            
            question.wrong_option1 = 'am'
            question.wrong_option2 = 'were'
            question.wrong_option3 = 'was'
            question.wrong_option4 = 'is'

        else: # You, We, They, past tense
            
            question.correct_option = 'were'

            
            question.wrong_option1 = 'am'
            question.wrong_option2 = 'are'
            question.wrong_option3 = 'was'
            question.wrong_option4 = 'is'

        question.question_string = f'{subject} ______ {state} {timing}.'


        return question



    def createaffirmativesubject(self):

        question = MultichoiceQuestion()
        question.topics.append(self.topic)

        timing = random.choice(self.timingGroup)

        verb = random.choice(self.verb_pool)

        verb_object = ''

        if verb in Test.verbs_with_objects:
            verb_object = f'{random.choice(Test.verbs_with_objects[verb])} '

        verb_forms = []
        with open('SourceFolder/inflections1.txt', 'r') as infile:

            for line in infile:
                if line.strip().split('\t', 1)[0] == verb:

                    for form in line.strip().split('\t'):
                        verb_forms.append(form)
                    
                    break
        current_verb_forms = [verb_forms[0], verb_forms[1]] # the relevant inflections for simple present tense

        verb = random.choice(current_verb_forms) # the inflection to be used in the current question

                
        if verb == current_verb_forms[0]: # the 'do' form

            

            question.correct_option = random.choice(random.choice(list(self.do_subjects.items()))[1])

            random.shuffle(self.does_subjects)
            question.wrong_option1 = self.does_subjects[0]
            question.wrong_option2 = self.does_subjects[1]
            question.wrong_option3 = self.does_subjects[2]
            question.wrong_option4 = self.does_subjects[3]
                           

        else:  # the 'does' form
            
            question.correct_option = random.choice(self.does_subjects)

            temp_list = list(self.do_subjects.items())
            random.shuffle(temp_list)

            question.wrong_option1 = temp_list[0][1][random.randrange(len(temp_list[0][1]))]

            question.wrong_option2 = temp_list[1][1][random.randrange(len(temp_list[1][1]))]

            question.wrong_option3 = temp_list[2][1][random.randrange(len(temp_list[2][1]))]

            question.wrong_option4 = temp_list[3][1][random.randrange(len(temp_list[3][1]))]

                           

        question.question_string = f'______ {verb} {verb_object}{timing}.'


        return question

    def test_timing_affirmative(self):

        question = MultichoiceQuestion()
        question.topics.append(self.topic)

        subjectGroup = random.choice(self.subList)

        subject = random.choice(subjectGroup[1])

        verb = random.choice(self.verb_pool)

        verb_object = ''

        if verb in Test.verbs_with_objects:
            verb_object = f'{random.choice(Test.verbs_with_objects[verb])} '

        verb_forms = []
        with open('SourceFolder/inflections1.txt', 'r') as infile:

            for line in infile:
                if line.strip().split('\t', 1)[0] == verb:

                    for form in line.strip().split('\t'):
                        verb_forms.append(form)
                    
                    break

        if subjectGroup[0] == 'ThirdSingular':

            verb = verb_forms[1] # this changes the inflection to the 'does' form

        question.correct_option = random.choice(self.timingGroup) # choose a recurrent timing variant

        question.wrong_option1 = random.choice(Test.timingIndicators['Past'])
        question.wrong_option2 = random.choice(Test.timingIndicators['Since'])
        question.wrong_option3 = random.choice(Test.timingIndicators['At past time'])
        question.wrong_option4 = random.choice(Test.timingIndicators['For past period'])
            
        question.question_string = f'{subject} {verb} {verb_object}______.'


        return question
            
                 

    def createtests(self, numfiles, numquestions):

        alltests = []

        for i in range(numfiles):

            alltests.append([])
            
            j = 1

            while True:
                alltests[i].append(self.createaffirmative())
                #alltests[i].append(self.createaffirmativesubject())

                #alltests[i].append(self.test_timing_affirmative())


                j = j + 2

                if j >= numquestions:
                    break

                

        return alltests

    
                
'''
Program to test appropriate use of tense and concord

'''


class DoesNotHappen(Test):

    topic = 'does not happen'

    subList = list(Test.subjectIndicators.items())

    subList.append(subList[2] * 3) # adds more 3rd person singular members, to ensure better representation in question pool
                
    timingGroup = Test.timingIndicators['Never']

    does_subjects = Test.subjectIndicators['ThirdSingular']

    do_subjects = {i:Test.subjectIndicators[i] for i in Test.subjectIndicators if i != 'ThirdSingular'}

    

    

    def createaffirmative(self):

        question = MultichoiceQuestion()
        question.topics.append(self.topic)
        
        subjectGroup = random.choice(self.subList)

        subject = random.choice(subjectGroup[1])

        timing = random.choice(self.timingGroup)

        verb = random.choice(self.verb_pool)

        verb_object = ''

        if verb in Test.verbs_with_objects:
            verb_object = f'{random.choice(Test.verbs_with_objects[verb])} '

        verb_forms = []
        with open('SourceFolder/inflections1.txt', 'r') as infile:

            for line in infile:
                if line.strip().split('\t', 1)[0] == verb:

                    for form in line.strip().split('\t'):
                        verb_forms.append(form)
                    
                    break

                
        if subjectGroup[0] == 'FirstSingular':

            question.correct_option = f'do not {verb_forms[0]}' # choose present simple - note could apply to other tenses correctly too

            
            question.wrong_option1 = f'am not {verb_forms[0]}' # I am not do
            question.wrong_option2 = f'are not {verb_forms[2]}' # I are not doing
            question.wrong_option3 = f'does not {verb_forms[0]}' # I does not do
            question.wrong_option4 = f'was not {verb_forms[0]}' # I was not do
                           
        elif subjectGroup[0] == 'ThirdSingular':
            
            question.correct_option = f'does not {verb_forms[0]}'

            
            question.wrong_option1 = f'are not {verb_forms[2]}' # He are not doing
            question.wrong_option2 = f'do not {verb_forms[0]}' # He do not do
            question.wrong_option3 = f'was not {verb_forms[1]}' # He was not does
            question.wrong_option4 = f'is not {verb_forms[0]}' # He is not do


        else:
            
            question.correct_option = f'do not {verb_forms[0]}' # choose present simple - note could apply to other tenses correctly too

            
            question.wrong_option1 = f'are not {verb_forms[0]}' # You are not do
            question.wrong_option2 = f'was not {verb_forms[2]}' # You was not doing
            question.wrong_option3 = f'does not {verb_forms[0]}' # You does not do
            question.wrong_option4 = f'was not {verb_forms[0]}' # You was not do

        question.question_string = f'{subject} ______ {verb_object}{timing}.'


        return question



    def createaffirmativesubject(self):

        question = MultichoiceQuestion()
        question.topics.append(self.topic)

        timing = random.choice(self.timingGroup)

        verb = random.choice(self.verb_pool)

        verb_object = ''

        if verb in Test.verbs_with_objects:
            verb_object = f'{random.choice(Test.verbs_with_objects[verb])} '

        verb_forms = ['do not', 'does not'] # the relevant inflections for the negative

        verb = f'{random.choice(verb_forms)} {verb}' # the inflection to be used in the current question

                
        if verb.startswith(verb_forms[0]): # the 'do not' form

            

            question.correct_option = random.choice(random.choice(list(self.do_subjects.items()))[1])

            random.shuffle(self.does_subjects)
            question.wrong_option1 = self.does_subjects[0]
            question.wrong_option2 = self.does_subjects[1]
            question.wrong_option3 = self.does_subjects[2]
            question.wrong_option4 = self.does_subjects[3]
                           

        else:  # the 'does not' form
            
            question.correct_option = random.choice(self.does_subjects)

            temp_list = list(self.do_subjects.items())
            random.shuffle(temp_list)

            question.wrong_option1 = temp_list[0][1][random.randrange(len(temp_list[0][1]))]

            question.wrong_option2 = temp_list[1][1][random.randrange(len(temp_list[1][1]))]

            question.wrong_option3 = temp_list[2][1][random.randrange(len(temp_list[2][1]))]

            question.wrong_option4 = temp_list[3][1][random.randrange(len(temp_list[3][1]))]

                           

        question.question_string = f'______ {verb} {verb_object}{timing}.'


        return question

    def test_timing_affirmative(self):

        question = MultichoiceQuestion()
        question.topics.append(self.topic)

        subjectGroup = random.choice(self.subList)

        subject = random.choice(subjectGroup[1])

        verb = random.choice(self.verb_pool)

        verb_object = ''

        if verb in Test.verbs_with_objects:
            verb_object = f'{random.choice(Test.verbs_with_objects[verb])} '

        verb_forms = []
        with open('SourceFolder/inflections1.txt', 'r') as infile:

            for line in infile:
                if line.strip().split('\t', 1)[0] == verb:

                    for form in line.strip().split('\t'):
                        verb_forms.append(form)
                    
                    break

        if subjectGroup[0] == 'ThirdSingular':

            verb = verb_forms[1] # this changes the inflection to the 'does' form

        question.correct_option = random.choice(self.timingGroup) # choose a recurrent timing variant

        question.wrong_option1 = random.choice(Test.timingIndicators['Past'])
        question.wrong_option2 = random.choice(Test.timingIndicators['Since'])
        question.wrong_option3 = random.choice(Test.timingIndicators['At past time'])
        question.wrong_option4 = random.choice(Test.timingIndicators['For past period'])
            
        question.question_string = f'{subject} {verb} {verb_object}______.'


        return question
            
                   

    def createtests(self, numfiles, numquestions):

        alltests = []

        for i in range(numfiles):

            alltests.append([])
            
            j = 1

            while True:
                alltests[i].append(self.createaffirmative())
                alltests[i].append(self.createaffirmativesubject())

                #alltests[i].append(self.test_timing_affirmative())


                j = j + 2

                if j >= numquestions:
                    break

                

        return alltests


'''
Program to test appropriate use of tense and concord

'''


class HadHappened(Test):
    topic = 'had happened'
   
    subList = list(Test.subjectIndicators.items())

    subList.append(subList[2] * 3) # adds more 3rd person singular members, to ensure better representation in question pool
                
    timingGroup = Test.timingIndicators['Before past event']

    def createaffirmative(self):

        question = MultichoiceQuestion()
        question.topics.append(self.topic)
        
        subjectGroup = random.choice(self.subList)

        subject = subjectGroup[1][0] if len(subjectGroup[1]) == 1 else random.choice(subjectGroup[1])

        timing = random.choice(self.timingGroup)

        verb = random.choice(self.verb_pool)

        verb_forms = []
        with open('SourceFolder/inflections1.txt', 'r') as infile:

            for line in infile:
                if line.strip().split('\t', 1)[0] == verb:

                    for form in line.strip().split('\t'):
                        verb_forms.append(form)
                    
                    break

                
        if subjectGroup[0] == 'FirstSingular':

            question.correct_option = f'had {verb_forms[4]}' # choose the past perfect

            
            question.wrong_option1 = f'have {verb_forms[4]}' # I have done
            question.wrong_option2 = f'will {verb_forms[0]}' # I will do
            question.wrong_option3 = f'am {verb_forms[2]}' # I am doing
            question.wrong_option4 = f'was {verb_forms[3]}' # I was did
                           
        elif subjectGroup[0] == 'ThirdSingular':
            
            question.correct_option = f'had {verb_forms[4]}' # choose the past perfect

            
            question.wrong_option1 = f'has {verb_forms[4]}' # He has done
            question.wrong_option2 = f'will {verb_forms[0]}' # He will do
            question.wrong_option3 = f'is {verb_forms[2]}' # He is doing 
            question.wrong_option4 = f'was {verb_forms[3]}' # He was did

        else:
            
            question.correct_option = f'had {verb_forms[4]}' # choose the past perfect

            
            question.wrong_option1 = f'have {verb_forms[4]}' # You have done
            question.wrong_option2 = f'will {verb_forms[0]}' # You will do
            question.wrong_option3 = f'are {verb_forms[2]}' # You are doing
            question.wrong_option4 = f'were {verb_forms[3]}' # You were did
  
        question.question_string = f'{subject} ______ {timing}.'


        return question



                    

    def createtests(self, numfiles, numquestions):

        alltests = []

        for i in range(numfiles):

            alltests.append([])
            
            for j in range(numquestions):
                alltests[i].append(self.createaffirmative())

        return alltests

         

'''
Program to test appropriate use of tense and concord

'''


class IsSomething(Test):
    topic = 'is something'

    subList = list(Test.subjectIndicators.items())

    subList.append(subList[2] * 3) # adds more 3rd person singular members, to ensure better representation in question pool
                
    past_indicators = [i for i in Test.timingIndicators['Past']
                       if not ('hour' in i or 'day' in i or 'week' in i or 'night' in i)]

    present_indicators = ['for now', 'at present', 'at this time', 'now']
    

    all_timing = past_indicators + present_indicators

    

    def createaffirmative(self):

        question = MultichoiceQuestion()
        question.topics.append(self.topic)
        
        subjectGroup = random.choice(self.subList)

        subject = random.choice(subjectGroup[1])

        timing = random.choice(self.all_timing)

        identity = random.choice(self.variable_identities)

        # check if identity starts with a vowel, to assign article

        article = ''

        firstletter = identity[0]
        if subjectGroup[0] in ['FirstSingular', 'SecondSingular', 'ThirdSingular']:
            if firstletter in 'aeiou':
                article = 'an '
            else:
                article = 'a '

        # temporary code to assign plurality

        else:

            identity = f'{identity}s'

               
        if subjectGroup[0] == 'FirstSingular' and timing in self.present_indicators:

            question.correct_option = 'am'

            
            question.wrong_option1 = 'was'
            question.wrong_option2 = 'were'
            question.wrong_option3 = 'is'
            question.wrong_option4 = 'are'

        elif subjectGroup[0] == 'FirstSingular' and timing in self.past_indicators:

            question.correct_option = 'was'

            
            question.wrong_option1 = 'am'
            question.wrong_option2 = 'were'
            question.wrong_option3 = 'is'
            question.wrong_option4 = 'are'        
                           
        elif subjectGroup[0] == 'ThirdSingular' and timing in self.present_indicators:
            
            question.correct_option = 'is'

            
            question.wrong_option1 = 'am'
            question.wrong_option2 = 'were'
            question.wrong_option3 = 'was'
            question.wrong_option4 = 'are'        


        elif subjectGroup[0] == 'ThirdSingular' and timing in self.past_indicators:
            
            question.correct_option = 'was'

            
            question.wrong_option1 = 'am'
            question.wrong_option2 = 'were'
            question.wrong_option3 = 'is'
            question.wrong_option4 = 'are'        

        elif timing in self.present_indicators: # You, We, They, present tense
            
            question.correct_option = 'are'

            
            question.wrong_option1 = 'am'
            question.wrong_option2 = 'were'
            question.wrong_option3 = 'was'
            question.wrong_option4 = 'is'

        else: # You, We, They, past tense
            
            question.correct_option = 'were'

            
            question.wrong_option1 = 'am'
            question.wrong_option2 = 'are'
            question.wrong_option3 = 'was'
            question.wrong_option4 = 'is'

        question.question_string = f'{subject} ______ {article}{identity} {timing}.'


        return question



    def createaffirmativesubject(self):

        question = MultichoiceQuestion()
        question.topics.append(self.topic)

        timing = random.choice(self.timingGroup)

        verb = random.choice(self.verb_pool)

        verb_object = ''

        if verb in Test.verbs_with_objects:
            verb_object = f'{random.choice(Test.verbs_with_objects[verb])} '

        verb_forms = []
        with open('SourceFolder/inflections1.txt', 'r') as infile:

            for line in infile:
                if line.strip().split('\t', 1)[0] == verb:

                    for form in line.strip().split('\t'):
                        verb_forms.append(form)
                    
                    break
        current_verb_forms = [verb_forms[0], verb_forms[1]] # the relevant inflections for simple present tense

        verb = random.choice(current_verb_forms) # the inflection to be used in the current question

                
        if verb == current_verb_forms[0]: # the 'do' form

            

            question.correct_option = random.choice(random.choice(list(self.do_subjects.items()))[1])

            random.shuffle(self.does_subjects)
            question.wrong_option1 = self.does_subjects[0]
            question.wrong_option2 = self.does_subjects[1]
            question.wrong_option3 = self.does_subjects[2]
            question.wrong_option4 = self.does_subjects[3]
                           

        else:  # the 'does' form
            
            question.correct_option = random.choice(self.does_subjects)

            temp_list = list(self.do_subjects.items())
            random.shuffle(temp_list)

            question.wrong_option1 = temp_list[0][1][random.randrange(len(temp_list[0][1]))]

            question.wrong_option2 = temp_list[1][1][random.randrange(len(temp_list[1][1]))]

            question.wrong_option3 = temp_list[2][1][random.randrange(len(temp_list[2][1]))]

            question.wrong_option4 = temp_list[3][1][random.randrange(len(temp_list[3][1]))]

                           

        question.question_string = f'______ {verb} {verb_object}{timing}.'


        return question

    def test_timing_affirmative(self):

        question = MultichoiceQuestion()
        question.topics.append(self.topic)

        subjectGroup = random.choice(self.subList)

        subject = random.choice(subjectGroup[1])

        verb = random.choice(self.verb_pool)

        verb_object = ''

        if verb in Test.verbs_with_objects:
            verb_object = f'{random.choice(Test.verbs_with_objects[verb])} '

        verb_forms = []
        with open('SourceFolder/inflections1.txt', 'r') as infile:

            for line in infile:
                if line.strip().split('\t', 1)[0] == verb:

                    for form in line.strip().split('\t'):
                        verb_forms.append(form)
                    
                    break

        if subjectGroup[0] == 'ThirdSingular':

            verb = verb_forms[1] # this changes the inflection to the 'does' form

        question.correct_option = random.choice(self.timingGroup) # choose a recurrent timing variant

        question.wrong_option1 = random.choice(Test.timingIndicators['Past'])
        question.wrong_option2 = random.choice(Test.timingIndicators['Since'])
        question.wrong_option3 = random.choice(Test.timingIndicators['At past time'])
        question.wrong_option4 = random.choice(Test.timingIndicators['For past period'])
            
        question.question_string = f'{subject} {verb} {verb_object}______.'


        return question
            
                 

    def createtests(self, numfiles, numquestions):

        alltests = []

        for i in range(numfiles):

            alltests.append([])
            
            j = 1

            while True:
                alltests[i].append(self.createaffirmative())
                #alltests[i].append(self.createaffirmativesubject())

                #alltests[i].append(self.test_timing_affirmative())


                j = j + 2

                if j >= numquestions:
                    break

                

        return alltests

'''
Program to test appropriate use of tense and concord

'''


class WasHappening(Test):
   
    topic = 'was happening'
    
    subList = list(Test.subjectIndicators.items())

    subList.append(subList[2] * 3) # adds more 3rd person singular members, to ensure better representation in question pool
                
    timingGroup = Test.timingIndicators['At past time']

    def createaffirmative(self):

        question = MultichoiceQuestion()
        question.topics.append(self.topic)
        
        subjectGroup = random.choice(self.subList)

        subject = subjectGroup[1][0] if len(subjectGroup[1]) == 1 else random.choice(subjectGroup[1])

        timing = random.choice(self.timingGroup)

        verb = random.choice(self.verb_pool)

        verb_forms = []
        with open('SourceFolder/inflections1.txt', 'r') as infile:

            for line in infile:
                if line.strip().split('\t', 1)[0] == verb:

                    for form in line.strip().split('\t'):
                        verb_forms.append(form)
                    
                    break

                
        if subjectGroup[0] == 'FirstSingular':

            question.correct_option = f'was {verb_forms[2]}' # choose the past continuous

            
            question.wrong_option1 = f'have {verb_forms[4]}' # I have done
            question.wrong_option2 = f'will {verb_forms[0]}' # I will do
            question.wrong_option3 = f'am {verb_forms[2]}' # I am doing
            question.wrong_option4 = f'was {verb_forms[3]}' # I was did
                           
        elif subjectGroup[0] == 'ThirdSingular':
            
            question.correct_option = f'was {verb_forms[2]}' # choose the past continuous

            
            question.wrong_option1 = f'has {verb_forms[4]}' # He has done
            question.wrong_option2 = f'will {verb_forms[0]}' # He will do
            question.wrong_option3 = f'is {verb_forms[2]}' # He is doing 
            question.wrong_option4 = f'was {verb_forms[3]}' # He was did

        else:
            
            question.correct_option = f'were {verb_forms[2]}' # choose the past continuous

            
            question.wrong_option1 = f'have {verb_forms[4]}' # You have done
            question.wrong_option2 = f'will {verb_forms[0]}' # You will do
            question.wrong_option3 = f'are {verb_forms[2]}' # You are doing
            question.wrong_option4 = f'were {verb_forms[3]}' # You were did
  
        question.question_string = f'{subject} ______ {timing}.'


        return question

                  

    def createtests(self, numfiles, numquestions):

        alltests = []

        for i in range(numfiles):

            alltests.append([])
            
            for j in range(numquestions):
                alltests[i].append(self.createaffirmative())

        return alltests


'''
Program to test appropriate use of tense and concord

'''


class WillBeHappening(Test):

    topic = 'will be happening'
   

    subList = list(Test.subjectIndicators.items())

    subList.append(subList[2] * 3) # adds more 3rd person singular members, to ensure better representation in question pool
                
    timingGroup = Test.timingIndicators['By future time']

    def createaffirmative(self):

        question = MultichoiceQuestion()
        question.topics.append(self.topic)
        
        subjectGroup = random.choice(self.subList)

        subject = subjectGroup[1][0] if len(subjectGroup[1]) == 1 else random.choice(subjectGroup[1])

        timing = random.choice(self.timingGroup)

        verb = random.choice(self.verb_pool)

        verb_forms = []
        with open('SourceFolder/inflections1.txt', 'r') as infile:

            for line in infile:
                if line.strip().split('\t', 1)[0] == verb:

                    for form in line.strip().split('\t'):
                        verb_forms.append(form)
                    
                    break

                
        if subjectGroup[0] == 'FirstSingular':

            question.correct_option = f'will be {verb_forms[2]}' # choose the future continuous

            
            question.wrong_option1 = f'have {verb_forms[4]}' # I have done
            question.wrong_option2 = f'will be {verb_forms[0]}' # I will be do
            question.wrong_option3 = f'was {verb_forms[2]}' # I was doing
            question.wrong_option4 = f'{verb_forms[3]}' # I did
                           
        elif subjectGroup[0] == 'ThirdSingular':
            
            question.correct_option = f'will be {verb_forms[2]}' # choose the future continuous

            
            question.wrong_option1 = f'has {verb_forms[4]}' # He has done
            question.wrong_option2 = f'will be {verb_forms[1]}' # He will be does
            question.wrong_option3 = f'was {verb_forms[2]}' # He was doing
            question.wrong_option4 = f'{verb_forms[3]}' # He did
        else:
            
            question.correct_option = f'will be {verb_forms[2]}' # choose the future continuous

            
            question.wrong_option1 = f'have {verb_forms[4]}' # You have done
            question.wrong_option2 = f'will be {verb_forms[0]}' # You will be do
            question.wrong_option3 = f'were {verb_forms[2]}' # You were doing
            question.wrong_option4 = f'{verb_forms[3]}' # You did
  
        question.question_string = f'{subject} ______ {timing}.'


        return question


    def createtests(self, numfiles, numquestions):

        alltests = []

        for i in range(numfiles):

            alltests.append([])
            
            for j in range(numquestions):
                alltests[i].append(self.createaffirmative())

        return alltests


# End of code of englishtest.py
class English():
    topics = ['happens', 'has happened', 'is something', 'is so', 'does happen', 'does not happen']
    questions = allquestions.english
    
class Mathematics():
    topics = []
    questions = []

class Business():
    topics = []
    questions = []

class Science():
##    topics = [
##            'General Basic Science',
##            'The Environment',
##            'Living Things',
##            'Chemicals and Materials',
##            'Energy and Mechanics',
##            'Outer Space and Radioactivity',
##            'Human Health and Development',
##            'General Physical and Health Education',
##            'Personal Fitness and Recreation',
##            'Sports and Games',
##            'Diseases and Personal Health',
##            'Drug use and abuse',
##            'Food and Nutrition',
##            'Personal and Sports Safety',
##            'Environmental Health',
##            'General Basic Technology',
##            'Workshop and Environmental Safety',
##            'Materials Technology',
##            'Building Technology',
##            'Electrical and Electronics Technology',
##            'Woodwork ',
##            'Metalwork',
##            'Drawing and Construction',
##            'Machines and Tools',
##            'General Information Technology',
##            'Computer Hardware',
##            'Software Applications',
##            'Networks and the Internet',
##            'Computer Ethics and Security',
##            'Operating Systems and Computer Logic',]




        questions2 = [
            {'question_string' : 'Human solid and liquid wastes from homes is known as_________________', 
'options' : ['effluent', 'garbage', 'refuse', 'sewage', 'sullage', ],
'correct_option' : 'sullage',
'topics' : ['The Environment',]},
{'question_string' : 'A masked trait is said to be _______________________________________', 
'options' : ['allelic', 'dominant', 'genotypic', 'phenotypic', 'recessive', ],
'correct_option' : 'recessive',
'topics' : ['Living Things',]},
{'question_string' : 'The following are reason for skill acquisition except for _______________________________', 
'options' : ['fun making', 'managing emergencies', 'self employment', 'survival strategy', 'taking risk', ],
'correct_option' : 'taking risk',
'topics' : ['General Basic Science',]},
{'question_string' : 'The incubation period in birds is between_______________________', 
'options' : ['fertilization and hatching of eggs', 'fertilization and laying of eggs', 'hatching of the first egg and the last egg', 'laying and hatching of eggs', 'laying of the first egg and hatching', ],
'correct_option' : 'laying and hatching of eggs',
'topics' : ['Living Things',]},
{'question_string' : 'Which of the following is an example of waterborne disease?', 
'options' : ['Cold', 'Measles', 'Pneumonia', 'Tuberculosis', 'Typhoid', ],
'correct_option' : 'Typhoid',
'topics' : ['Human Health and Development',]},
{'question_string' : 'A product of tobacco is _______________________________', 
'options' : ['cigarette', 'cocaine', 'heroin', 'marijuana', 'morphine', ],
'correct_option' : 'cigarette',
'topics' : ['Human Health and Development',]},
{'question_string' : 'The process by which food substances are broken down into simple and soluble form is called________________________________', 
'options' : ['defecation', 'digestion', 'excretion', 'mastication', 'regurgitation', ],
'correct_option' : 'digestion',
'topics' : ['Human Health and Development','Living Things',]},
{'question_string' : 'The diagram illustrates', 
'options' : ['diffused reflection', 'laws of refraction', 'refraction of light', 'regular reflection', 'scattered reflection', ],
'correct_option' : 'refraction of light',
'topics' : ['Energy and Mechanics',]},
{'question_string' : 'The part labelled I is the___________________', 
'options' : ['incident ray', 'reflected ray', 'reflecting medium', 'refracted ray', 'refracting medium', ],
'correct_option' : 'refracted ray',
'topics' : ['Energy and Mechanics',]},
{'question_string' : 'The distribution of materials within an organisms is known as___________________________', 
'options' : ['circulation', 'digestion', 'excretion', 'reproduction', 'respiration', ],
'correct_option' : 'circulation',
'topics' : ['Living Things',]},
{'question_string' : 'Which of the following is a flowering plant?', 
'options' : ['Conifer', 'Fern', 'Ixora', 'Liverwort', 'Moss', ],
'correct_option' : 'Ixora',
'topics' : ['Living Things',]},
{'question_string' : 'The conversion of water vapour to liquid is known as_________________________', 
'options' : ['condensation', 'deposition', 'evaporation', 'sublimation', 'vaporization', ],
'correct_option' : 'condensation',
'topics' : ['Chemicals and Materials','Energy and Mechanics',]},
{'question_string' : 'A microphone converts sound energy into________________________ energy', 
'options' : ['electrical', 'heat', 'magnetic', 'mechanical', 'light', ],
'correct_option' : 'electrical',
'topics' : ['Energy and Mechanics',]},
{'question_string' : 'Which of the following  is the chemical formula of water?', 
'options' : ['HO', 'H2O2', 'H2O', 'H3O', 'H3O2', ],
'correct_option' : 'H2O',
'topics' : ['Chemicals and Materials',]},
{'question_string' : 'Which of the following vitamins is also referred to as the “ Sunshine vitamin”?', 
'options' : ['A', 'B', 'D', 'E', 'K', ],
'correct_option' : 'D',
'topics' : ['Human Health and Development',]},
{'question_string' : 'In the solar system, the fourth planet from the sun is __________________________', 
'options' : ['earth', 'mars', 'mercury', 'neptune', 'vensus', ],
'correct_option' : 'mars',
'topics' : ['Outer Space and Radioactivity',]},
{'question_string' : 'Which of the following is a renewable source of energy?', 
'options' : ['Coal', 'Diesel', 'Petrol', 'Gasoline', 'Wood', ],
'correct_option' : 'Wood',
'topics' : ['Energy and Mechanics',]},
{'question_string' : 'Metals expand when___________________energy is applied to them', 
'options' : ['chemical', 'heat', 'kinetic', 'light', 'sound', ],
'correct_option' : 'heat',
'topics' : ['Energy and Mechanics',]},
{'question_string' : 'Matter are classified into____________________ states', 
'options' : ['two', 'three', 'four', 'five', 'six', ],
'correct_option' : 'three',
'topics' : ['Chemicals and Materials',]},
{'question_string' : 'The following are methods of controlling soil erosion except', 
'options' : ['bush burning', 'mulching', 'planting of cover crops', 'planting of trees', 'terracting', ],
'correct_option' : 'bush burning',
'topics' : ['The Environment',]},
{'question_string' : 'The method of growing food crops and trees on the same piece of land is ___________________', 
'options' : ['afforestation', 'agroforestry', 'crop rotation', 'horiculture', 'mixed cropping', ],
'correct_option' : 'agroforestry',
'topics' : ['Living Things',]},
{'question_string' : 'When two forces act on a body and it remains at rest, it means the forces acting on it are', 
'options' : ['equal and opposite', 'inactive', 'in constant motion', 'unbalanced', ' weak and active', ],
'correct_option' : 'equal and opposite',
'topics' : ['Energy and Mechanics',]},
{'question_string' : 'The method of heat transfer demonstrated in the diagram below is ', 
'options' : ['conduction', 'convection', 'evaporation', 'radiation', 'vaporization', ],
'correct_option' : 'convection',
'topics' : ['Energy and Mechanics',]},
{'question_string' : '', 
'options' : ['26', '54', '55', '74', '200', ],
'correct_option' : '200',
'topics' : ['Energy and Mechanics',]},
{'question_string' : 'The energy possessed by a stationary ball is____________________ energy', 
'options' : ['chemical', 'electrical', 'kinetic', 'magnetic', 'potential', ],
'correct_option' : 'potential',
'topics' : ['Energy and Mechanics',]},
{'question_string' : 'Which of the following is not a radioactive element?', 
'options' : ['Magnesium', 'Plutonium', 'Radius', 'Thorium', 'Uranium', ],
'correct_option' : 'Magnesium',
'topics' : ['Outer Space and Radioactivity',]},
{'question_string' : 'The method of separation of mixture demonstrated in the diagram below is', 
'options' : ['chromatography', 'crystallization', 'destructive distillation', 'fractional distillation', 'sedimentation', ],
'correct_option' : 'fractional distillation',
'topics' : ['Chemicals and Materials',]},
{'question_string' : 'When a bar magnet is suspended freely and it comes to rest, its ends point in the ________________ direction', 
'options' : ['EastWest', 'NorthSouth', 'NorthWest', 'SouthEast', 'SouthWest', ],
'correct_option' : 'NorthSouth',
'topics' : ['Energy and Mechanics',]},
{'question_string' : 'A radio set of 60w is used for 12hours per day 30 days. Calculate the quantity of energy consumed in kWh. ', 
'options' : ['21.60', '24.00', '35.00', '42.00', '102.00', ],
'correct_option' : '21.60',
'topics' : ['Energy and Mechanics',]},
{'question_string' : '', 
'options' : ['', '', '', '', '', ],
'correct_option' : '',
'topics' : ['Energy and Mechanics',]},
{'question_string' : 'The following are objectives of Physical Education except', 
'options' : ['development of international friendly matches', 'development of skill', 'Exposure of athletes to intellectual environment', 'provision of life career', 'provision of opportunity for physical development', ],
'correct_option' : 'development of international friendly matches',
'topics' : ['General Physical and Health Education',]},
{'question_string' : 'Which of the following activities can be recommended for an elderly person?', 
'options' : ['Camping', 'Cycling', 'Running', 'Swimming', 'Walking', ],
'correct_option' : 'Walking',
'topics' : ['Personal Fitness and Recreation',]},
{'question_string' : 'Who is the father of modern Olympic games?', 
'options' : ['Captain Clia', 'Frederick Ludwing John', 'James Naismith', 'Johann Basedow', 'Pierre de Coubertin', ],
'correct_option' : 'Pierre de Coubertin',
'topics' : ['General Physical and Health Education',]},
{'question_string' : 'Insufficient warm up activities may lead to____________________________', 
'options' : ['anawmia', 'convulsion', 'nausea', 'scurvy', 'strain', ],
'correct_option' : 'strain',
'topics' : ['Personal and Sports Safety',]},
{'question_string' : 'The ability of a group of muscles to sustain contraction over a period of time is __________________', 
'options' : ['agility', 'balance', 'endurance', 'flexibility', 'strength', ],
'correct_option' : 'endurance',
'topics' : ['Personal Fitness and Recreation',]},
{'question_string' : 'The physical fitness component required in sprint is ______________________', 
'options' : ['accuracy', 'balance', 'coordination', 'flexibility', 'speed', ],
'correct_option' : 'speed',
'topics' : ['General Physical and Health Education',]},
{'question_string' : 'An example of a tumbling exercise is ____________________', 
'options' : ['crab walk', 'duck fight', 'forward roll', 'frog jump', 'sit up', ],
'correct_option' : 'forward roll',
'topics' : ['Personal Fitness and Recreation',]},
{'question_string' : 'The expressive movement of the body to conform with rhythm of sound is ____________________', 
'options' : ['dancing', 'galloping', 'skipping', 'sporting', 'swinging', ],
'correct_option' : 'dancing',
'topics' : ['Personal Fitness and Recreation',]},
{'question_string' : 'Which of the following is a partnership activity?', 
'options' : ['Duck fight', 'Elbow balance', 'Frog jump', 'Press up', 'Push up', ],
'correct_option' : 'Duck fight',
'topics' : ['General Physical and Health Education',]},
{'question_string' : 'An example of an indoor activity is ________________', 
'options' : ['camping', 'cricket', 'hiking', 'scrabble', 'surfing', ],
'correct_option' : 'scrabble',
'topics' : ['Personal Fitness and Recreation',]},
{'question_string' : 'An injury that occurs as a result of over stretching of the ligament of the joint is __________________', 
'options' : ['abrasion', 'dislocation', 'fracture', 'sprain', 'strain', ],
'correct_option' : 'sprain',
'topics' : ['Personal and Sports Safety',]},
{'question_string' : 'Which of the following is a style in swimming ?', 
'options' : ['Breast stroke', 'Eastern cut off', 'Forward roll', 'Rowing', 'Spiking', ],
'correct_option' : 'Breast stroke',
'topics' : ['Sports and Games',]},
{'question_string' : 'A place where two or more bones meet in the body is a___________________________', 
'options' : ['joint', 'ligament', 'limbs', 'tendon', 'trunk', ],
'correct_option' : 'joint',
'topics' : ['Personal Fitness and Recreation',]},
{'question_string' : 'Which of the following is a stunt activity?', 
'options' : ['Astride vault', 'Backward roll', 'Hand stand', 'Neck spring', 'Thief vault', ],
'correct_option' : 'Hand stand',
'topics' : ['Sports and Games',]},
{'question_string' : 'Which of the following is a box activity in gymnastics?', 
'options' : ['Elbow balance', 'Forward roll', 'Handstand', 'Headstand', 'Through vault', ],
'correct_option' : 'Handstand',
'topics' : ['Sports and Games',]},
{'question_string' : 'Spiking is a fundamental skill in ______________________________', 
'options' : ['basketball', 'football', 'handball', 'hockey', 'volleyball', ],
'correct_option' : 'volleyball',
'topics' : ['Sports and Games',]},
{'question_string' : 'In a game of tennis, when the ball land outside the service area it is a/an__________________service', 
'options' : ['bad', 'double', 'faulty', 'offensive', 'good', ],
'correct_option' : 'faulty',
'topics' : ['Sports and Games',]},
{'question_string' : 'For a service to be valid in the game of tennis, the ball must touch the opponents', 
'options' : ['back court', 'base line', 'centre line', 'service area', 'side area', ],
'correct_option' : 'service area',
'topics' : ['Sports and Games',]},
{'question_string' : 'Which of the following is a skill in the game of football?', 
'options' : ['Dribbling', 'Flick', 'Grip', 'Scoop', 'Hitting', ],
'correct_option' : 'Dribbling',
'topics' : ['Sports and Games',]},
{'question_string' : 'How many players make a team in a handball game of football?', 
'options' : ['3', '5', '7', '9', '11', ],
'correct_option' : '7',
'topics' : ['Sports and Games',]},
{'question_string' : 'Which of the following is an equipment in swimming', 
'options' : ['Baton', 'Floats', 'Gloves', 'Pool', 'Racket', ],
'correct_option' : 'Floats',
'topics' : ['Sports and Games',]},
{'question_string' : 'The bones at a joint are held together by_______________________', 
'options' : ['cartilage', 'fibre', 'ligament', 'muscle', 'tendon', ],
'correct_option' : 'ligament',
'topics' : ['Personal Fitness and Recreation',]},
{'question_string' : 'The ability of the body to maintain its equilibrium is_______________________', 
'options' : ['agility', 'balance', 'endurance', 'flexibility', 'strength', ],
'correct_option' : 'balance',
'topics' : ['Diseases and Personal Health',]},
{'question_string' : 'The physical fitness component that allows free movement at the joint is ________________', 
'options' : ['agility', 'balance', 'flexibility', 'power', 'speed', ],
'correct_option' : 'flexibility',
'topics' : ['Personal Fitness and Recreation',]},
{'question_string' : 'Which of the following is not a rule in discus throw?', 
'options' : ['Each competitor is awarded the best of his trial', 'Measurement is taken from outside the sector', 'The competitors are allowed 3 or 5 trials', 'The discus is thrown from the sector', 'The order of trial is decided by drawing of lots', ],
'correct_option' : 'The discus is thrown from the sector',
'topics' : ['Sports and Games',]},
{'question_string' : 'The postural deformity leading to bending of lumbar spine beyond normal level is_____________', 
'options' : ['flat foot', 'knock knee', 'kyphosis', 'lordosis', 'scoliosis', ],
'correct_option' : 'lordosis',
'topics' : ['Personal Fitness and Recreation',]},
{'question_string' : 'Repairs of worn out tissues and building of white blood cells is the function of', 
'options' : ['carbohydrate', 'fats and oil', 'mineral salt', 'protein', 'water', ],
'correct_option' : 'protein',
'topics' : ['Food and Nutrition',]},
{'question_string' : 'How many hurdles does an athlete run over in a 110m race?', 
'options' : ['10', '11', '12', '13', '14', ],
'correct_option' : '10',
'topics' : ['Sports and Games',]},
{'question_string' : 'The following are responsibilities of government in school physical education programme except', 
'options' : ['encouraging schools to release students for sports', 'providing financial aid to school physical education programme', 'provision of sport facilities and equipment', 'punishing principals whose school participates in sports', 'training of physical education teacher', ],
'correct_option' : 'punishing principals whose school participates in sports',
'topics' : ['General Physical and Health Education',]},
{'question_string' : 'Which of the following personnel can be recommended as a school games master?', 
'options' : ['Examination officer', 'Head teacher', '', 'House master', 'Vice principal academics', ],
'correct_option' : '',
'topics' : ['General Physical and Health Education',]},
                
]

        questions = [
{'question_string' : 'which of the following is not a source of light?', 
'options' : ['sun', 'fire fly', 'moon', 'star', ],
'correct_option' : 'moon',
'topics' : ['Energy and Mechanics',]},
{'question_string' : 'which of these functions like our limb?', 
'options' : ['lever', 'pulley', 'screw', 'wedges', ],
'correct_option' : 'lever',
'topics' : ['Energy and Mechanics',]},
{'question_string' : 'refraction of light occurs when rays of light......', 
'options' : ['fall on a rough surface', 'travel on a straiht line', 'move from a medium to another', 'strike a polished material', ],
'correct_option' : 'move from a medium to another',
'topics' : ['Outer Space and Radioactivity',]},
{'question_string' : 'enviroment harzard does NOT result to erosion is.....', 
'options' : ['burning', 'flooding', 'deforestation', 'pollution', ],
'correct_option' : 'pollution',
'topics' : ['The Environment',]},
{'question_string' : 'the energy conversion in a boiling ring is....to....', 
'options' : ['light,heat', 'electrical,heat', 'chemical,light', 'chemical,electrical', ],
'correct_option' : 'electrical,heat',
'topics' : ['Energy and Mechanics',]},
{'question_string' : 'the two magnet poles which repel are', 
'options' : ['south,south', 'north,south', 'east,west', 'west,west', ],
'correct_option' : 'south,south',
'topics' : ['Energy and Mechanics',]},
{'question_string' : 'dary product does not include', 
'options' : ['cheese', 'egg', 'milk', 'yoghurt', ],
'correct_option' : 'egg',
'topics' : ['Living Things',]},
{'question_string' : 'which of the following is a third class lever ? ', 
'options' : ['nutcracker', 'wheelbarrow', 'sugartong', 'hammer', ],
'correct_option' : 'sugartong',
'topics' : ['Energy and Mechanics',]},
{'question_string' : 'it is best to properly dispose our sewage to', 
'options' : ['keep files away', 'make our surr neat and tidy', 'prevent unpleasant smell', 'prevent spread of disease', ],
'correct_option' : 'prevent spread of disease',
'topics' : ['Human Health and Development',]},
{'question_string' : 'a legal body which enforce forestry regulation is ', 
'options' : ['FEPA', 'NAFCON', 'NESREA', 'FAO', ],
'correct_option' : 'FEPA',
'topics' : ['General Basic Science',]},
{'question_string' : 'which of the following food item helps to replace worn out cells and tissues', 
'options' : ['fish', 'butter', 'rice', 'maize', ],
'correct_option' : 'fish',
'topics' : ['Human Health and Development',]},
{'question_string' : 'The diagram above shows the magnetic.....', 
'options' : ['Attraction', 'Field', 'Repulsion', 'Law', ],
'correct_option' : 'Attraction',
'topics' : ['Chemicals and Materials',]},
{'question_string' : 'fruits are nutritional to the body and should be taking', 
'options' : ['after', 'during', 'within', 'before', ],
'correct_option' : 'after',
'topics' : ['Human Health and Development',]},
{'question_string' : 'self esteem is ', 
'options' : ['feeling of self worth', 'active listening', 'open mindless', 'feelin shy', ],
'correct_option' : 'feeling of self worth',
'topics' : ['General Basic Science',]},
{'question_string' : 'if  it takes 6N to lift a block with a pulley.what is the mecanical advantage of using the pulley if it takes 18N for you to lift the block?', 
'options' : ['1', '2', '3', '12', ],
'correct_option' : '3',
'topics' : ['Energy and Mechanics',]},
{'question_string' : 'an offspring resembles his parents because he/she....them', 
'options' : ['loves', 'inherits them', 'lives with', 'wishes to resemble', ],
'correct_option' : 'inherits them',
'topics' : ['General Basic Science',]},
{'question_string' : 'the puberty changes occur at the......stage in life.', 
'options' : ['childhood', 'adulthood', 'widowhood', 'adolesent', ],
'correct_option' : 'adolesent',
'topics' : ['Human Health and Development',]},
{'question_string' : 'the fraction of crude oil used in terring road is......', 
'options' : ['bitumen', 'paraffin', 'grease', 'kerosine', ],
'correct_option' : 'bitumen',
'topics' : ['Chemicals and Materials',]},
{'question_string' : 'an object that is a conductor of heat and electricity is a ______', 
'options' : ['Non metal', 'plastic', 'metal', 'glass', ],
'correct_option' : 'metal',
'topics' : ['Metalwork',]},
{'question_string' : 'which of the following proces is a highly developed technology used for preserving grains ?', 
'options' : ['sack', 'gourd', 'drums', 'silos', ],
'correct_option' : 'silos',
'topics' : ['General Basic Technology',]},
{'question_string' : 'the type of plastic which can melt and be remolded is known as....', 
'options' : ['thermolplastic', 'politheneplastic', 'thermosetplastic', 'thermolpile plastic', ],
'correct_option' : 'thermolplastic',
'topics' : ['Metalwork',]},
{'question_string' : 'which of these metals is used to produce roofing sheets?', 
'options' : ['iron', 'steel', 'zinc', 'copper', ],
'correct_option' : 'zinc',
'topics' : ['Metalwork',]},
{'question_string' : 'a hardwood can be identified by its.....', 
'options' : ['needle like leaves', 'broads leave', 'tappered stem', 'evergreen leaves', ],
'correct_option' : 'broads leave',
'topics' : ['Woodwork ',]},
{'question_string' : 'potters wheel is used when producing a product made of......', 
'options' : ['robber', 'plastic', 'metal', 'ceramics', ],
'correct_option' : 'ceramics',
'topics' : ['Human Health and Development',]},
{'question_string' : 'preventive mentainance includes the following EXCEPT', 
'options' : ['lubrication', 'inspection', 'repair', 'cleaning', ],
'correct_option' : 'repair',
'topics' : ['Environmental Health',]},
{'question_string' : 'Continuous thick line in technical drawing is used for....', 
'options' : ['outline', 'hidden details', 'construction', 'centre line', ],
'correct_option' : 'outline',
'topics' : ['Drawing and Construction',]},
{'question_string' : 'A regular polygon with seven sides is called', 
'options' : ['hexagon', 'heptagon', 'pentagon', 'decagon', ],
'correct_option' : 'heptagon',
'topics' : ['Drawing and Construction',]},
{'question_string' : 'Type of line above is used to...', 
'options' : ['Cutting plane', 'hidden detail', 'dimension', 'centre line', ],
'correct_option' : 'dimension',
'topics' : ['Drawing and Construction',]},
{'question_string' : 'The angle marked x in the construction shown is....', 
'options' : ['15o', '30o', '60o', '75o', ],
'correct_option' : '60o',
'topics' : ['Drawing and Construction',]},
{'question_string' : 'Friction is the force which....', 
'options' : ['oppose motion', 'causes movement', 'generates energy', 'increase motion', ],
'correct_option' : 'oppose motion',
'topics' : ['Energy and Mechanics',]},
{'question_string' : 'Gear drives are used to transmit....', 
'options' : ['force', 'energy', 'Work', 'power', ],
'correct_option' : 'power',
'topics' : ['Energy and Mechanics',]},
{'question_string' : 'Which of the following is NOT a woodwork machine?', 
'options' : ['Milling machine', 'Band machine', 'Circular saw', 'Thicknessing machine', ],
'correct_option' : 'Milling machine',
'topics' : ['Woodwork ',]},
{'question_string' : 'The tool used for cutting sheet metal is called....', 
'options' : ['pincers', 'pliers', 'snip', 'panelsaw', ],
'correct_option' : 'snip',
'topics' : ['Metalwork',]},
{'question_string' : 'Which of these saws is used for cutting compex shapes in woodwork?', 
'options' : ['Tenon saw', 'Dovetail saw', 'Coping saw', 'Fret saw', ],
'correct_option' : 'Fret saw',
'topics' : ['Woodwork ',]},
{'question_string' : 'Which of the following is NOT a metalwork marking out tool?', 
'options' : ['Scriber', 'inside calliper', 'Dot punch', 'Divider', ],
'correct_option' : 'inside calliper',
'topics' : ['Metalwork',]},
{'question_string' : 'The purpose of well in woodwork bench is to...', 
'options' : ['store tools during working', 'hold the bench hook', 'receive wood shaving', 'accommodate', ],
'correct_option' : 'store tools during working',
'topics' : ['Woodwork ',]},
{'question_string' : 'The section of the workshop marked “EMERGENCY EXIT” is....', 
'options' : ['for escape only', 'to provide easy movement', 'to provide entrance for the workers', 'for safety of materials', ],
'correct_option' : 'for escape only',
'topics' : ['Workshop and Environmental Safety',]},
{'question_string' : 'The best form of accident prevention in the workshop is to...', 
'options' : ['work well', 'give first aid', 'avoid the use of machine', 'obey safety rules', ],
'correct_option' : 'obey safety rules',
'topics' : ['Workshop and Environmental Safety',]},
{'question_string' : 'Which of the following symbols represents electrical resistor', 
'options' : [],
'correct_option' : '',
'topics' : ['Electrical and Electronics Technology',]},
{'question_string' : 'A generator is a device which converts......', 
'options' : ['eletrical energy into mechanical energy', 'eletrical energy into light energy', 'mechanical energy into electrical energy', 'mechanical energy into light energy', ],
'correct_option' : 'mechanical energy into electrical energy',
'topics' : ['Energy and Mechanics',]},
{'question_string' : 'site preparation includes the following EXCEPT...', 
'options' : ['cutting of grass', 'moulding of blocks', 'uprooting of trees', 'removal of top soil', ],
'correct_option' : 'moulding of blocks',
'topics' : ['Building Technology',]},
{'question_string' : 'The part which surposes and transmits the load of the building to the subsoil is...', 
'options' : ['roof', 'wall', 'lintel', 'foundation', ],
'correct_option' : 'foundation',
'topics' : ['Building Technology',]},
{'question_string' : 'Which of the following appliances does NOT convert electrical energy into heat energy?', 
'options' : ['Electric fan', 'Eletric iron', 'Eletric kettle', 'Electric cooker', ],
'correct_option' : 'Electric fan',
'topics' : ['Energy and Mechanics','Electrical and Electronics Technology',]},
{'question_string' : 'Physical education is an integral part of the education which helps to develops the body and mind through physical', 
'options' : ['behaviour', 'fitness', 'activities ', 'body', ],
'correct_option' : 'activities ',
'topics' : ['General Physical and Health Education',]},
{'question_string' : 'The following must be ensured during heavy bleeding EXCEPT', 
'options' : ['victim must not be crowded', 'bandaging the affected area', 'stop bleeding with dirty cloth', 'elevating the limbs', ],
'correct_option' : 'stop bleeding with dirty cloth',
'topics' : ['Personal and Sports Safety',]},
{'question_string' : 'The stage of period  at which the reproductive organs begin to mature is...', 
'options' : ['infancy', 'adolescent', 'puberty', 'chilhood', ],
'correct_option' : 'puberty',
'topics' : ['Human Health and Development',]},
{'question_string' : 'The activity done during leisure hour is....', 
'options' : ['recreation', 'sports', 'games', 'gymnastic', ],
'correct_option' : 'recreation',
'topics' : ['Personal Fitness and Recreation',]},
{'question_string' : 'An ordered movement that runs through all the body is known as...', 
'options' : ['dance', 'rhythm', 'jogging', 'singing', ],
'correct_option' : 'dance',
'topics' : ['Personal Fitness and Recreation',]},
{'question_string' : 'The process by which menstrual cycle stopped in woman is called...', 
'options' : ['ovulation', 'period', 'menopause', 'bleeding', ],
'correct_option' : 'menopause',
'topics' : ['Human Health and Development',]},
{'question_string' : 'Cross.... is an equipment in pole vault', 
'options' : ['arm', 'leg', 'hand', 'bar', ],
'correct_option' : 'bar',
'topics' : ['Living Things',]},
{'question_string' : 'Pentathlon in athletics is an event carried out by', 
'options' : ['men', 'woman', 'girls', 'children', ],
'correct_option' : 'woman',
'topics' : ['Sports and Games',]},
{'question_string' : 'A combined event that is done by woman and comprises of 7 games is known as...', 
'options' : ['decathlon', 'hectagon', 'pentathlon', 'heptathlon', ],
'correct_option' : 'heptathlon',
'topics' : ['General Physical and Health Education',]},
{'question_string' : 'Hockey is a game played by two tearms of ....players', 
'options' : ['9', '10', '11', '12', ],
'correct_option' : '11',
'topics' : ['Sports and Games',]},
{'question_string' : 'Meal that contains various classes of food in the right proportion is....', 
'options' : ['Vitamin', 'Calories', 'Balance diet', 'Adequate salt', ],
'correct_option' : 'Balance diet',
'topics' : ['Food and Nutrition',]},
{'question_string' : 'Forward roll and backward roll are exercises in....', 
'options' : ['Acthletics', 'Gymnastics', 'Soccer', 'Karate', ],
'correct_option' : 'Gymnastics',
'topics' : ['Sports and Games',]},
{'question_string' : 'The following items are regarded as missiles EXCEPT', 
'options' : ['Hammer', 'Shot put', 'Javelin', 'Pole vault', ],
'correct_option' : 'Pole vault',
'topics' : ['Sports and Games',]},
{'question_string' : 'The most essential skills in the game of handball are', 
'options' : ['Catching and heading', 'Throwing and catching', 'Shooting and scoring', 'Kicking andshooting', ],
'correct_option' : 'Throwing and catching',
'topics' : ['Sports and Games',]},
{'question_string' : 'The first recorded olympic festival was held in.... B.C', 
'options' : ['766', '776', '786', '796', ],
'correct_option' : '776',
'topics' : ['General Physical and Health Education',]},
{'question_string' : 'Activities that are performed on a raised object are called', 
'options' : ['Vaults', 'Agilities', 'Somersaults', 'Weightilifing', ],
'correct_option' : 'Vaults',
'topics' : ['Sports and Games',]},
{'question_string' : 'Gymnast is a performer of.... activities', 
'options' : ['Gymchronist', 'Gymnastic', 'Acrobatics', 'Aquatic', ],
'correct_option' : 'Gymnastic',
'topics' : ['Sports and Games',]},
{'question_string' : 'Factors responsible for poor posture include the following EXCEpt', 
'options' : ['Accident', 'Diet', 'Fatigue', 'illiness', ],
'correct_option' : 'Diet',
'topics' : ['Food and Nutrition',]},
{'question_string' : 'ln accident Greece, Olympic festival was organized in homour of a supreme god called....', 
'options' : ['Pythian', 'Claus', 'Zeus', 'Appolo', ],
'correct_option' : 'Zeus',
'topics' : ['General Physical and Health Education',]},
{'question_string' : 'The race that requies full speed from the start to finish is ...race.', 
'options' : ['Sprint', 'Speed', 'Short', 'Long', ],
'correct_option' : 'Sprint',
'topics' : ['Sports and Games',]},
{'question_string' : 'The forth leg runner in a relay race is called....', 
'options' : ['Forth', 'Fast', 'Anchor', 'Fast', ],
'correct_option' : 'Anchor',
'topics' : ['Sports and Games',]},
{'question_string' : 'The class of food that serves as a major source of energy during muscular contraction is called....', 
'options' : ['Protein', 'Mineral salts', 'Carbohydrates', 'Water', ],
'correct_option' : 'Carbohydrates',
'topics' : ['Food and Nutrition','Human Health and Development',]},
{'question_string' : 'The bony and cartilaginous frame work of the body is known as', 
'options' : ['Skeleton', 'Muscles', 'Bones', 'Cartilage', ],
'correct_option' : 'Skeleton',
'topics' : ['Living Things',]},
{'question_string' : 'Taekwondo is a...sport', 
'options' : ['Japanese', 'Korean', 'Togolese', 'Cartilage', ],
'correct_option' : 'Korean',
'topics' : ['Sports and Games',]},
{'question_string' : 'The ability to float in water with confidence is called...', 
'options' : ['Buoyancy', 'Propulsion', 'Confidency', 'Breathing', ],
'correct_option' : 'Buoyancy',
'topics' : ['Personal Fitness and Recreation',]},
{'question_string' : 'Which of the following is an Electronic Machine?', 
'options' : ['Sim card', 'Compart disk', 'Computer', 'Flash drive', ],
'correct_option' : 'Computer',
'topics' : ['General Information Technology',]},
{'question_string' : 'The age when tools were made from steel and metals is the.....', 
'options' : ['Stone age', 'iron age', 'Middle age', 'industrial age', ],
'correct_option' : 'iron age',
'topics' : ['Metalwork',]},
{'question_string' : 'The blinking symbol on the computer screen is called the', 
'options' : ['Logo', 'Mouse', 'Cursor', 'prompt', ],
'correct_option' : 'Cursor',
'topics' : ['Computer Hardware',]},
{'question_string' : 'The ability to use the computer for different purposes is called....', 
'options' : ['Diligence', 'Versatility', 'Accurac', 'Prompt', ],
'correct_option' : 'Versatility',
'topics' : ['Computer Ethics and Security',]},
{'question_string' : 'Which of the following is NOT a way of classifying computer?', 
'options' : ['Classication by age', 'Classification by size', 'Classification by range', 'Classification by size', ],
'correct_option' : 'Classication by age',
'topics' : ['General Information Technology',]},
{'question_string' : 'Which of the following is NOT an example of external storage device?', 
'options' : ['Compress disk  ', 'Flash drive', 'Compact disk', 'Memory card', ],
'correct_option' : 'Compress disk  ',
'topics' : ['Computer Hardware',]},
{'question_string' : 'All of the following are examples of input devices Except....', 
'options' : ['Scanner', 'Mouse', 'Printer', 'Keyboard', ],
'correct_option' : 'Printer',
'topics' : ['Computer Hardware',]},
{'question_string' : 'Which of the following is NOT true about the Arithmetic and Logic Unit?', 
'options' : ['Can perform all types of an arithemetic operation', 'Canperform all logic reasoing', 'Can perform addition, subtractions multiplication', 'Can store data and instructions', ],
'correct_option' : 'Can store data and instructions',
'topics' : ['Computer Hardware',]},
{'question_string' : 'Which of the following is Not a function of operating system?', 
'options' : ['Booting the computer', 'Providing user interface', 'Printing processed work', 'File management', ],
'correct_option' : 'Printing processed work',
'topics' : ['Operating Systems and Computer Logic',]},
{'question_string' : 'The following are methods of tranmitting information over a long distance in the olden daysEXCEPT...', 
'options' : ['Whistiling', 'Whispering', 'Firelighting', 'Drumming', ],
'correct_option' : 'Drumming',
'topics' : ['Computer Hardware',]},
{'question_string' : 'The use of a rug in a computer laboratory helps to..', 
'options' : ['Suppress heat', 'Suppress dust', 'Prevent dust', 'lncrease ventilation', ],
'correct_option' : 'Prevent dust',
'topics' : ['General Information Technology',]},
{'question_string' : 'Which of the following is NOT a feature of graphic package?', 
'options' : ['Menu bar', 'Outlook', 'Colour box', 'Printable area', ],
'correct_option' : 'Outlook',
'topics' : ['Software Applications',]},
{'question_string' : 'The person that retrieves, stores and queries database is called...', 
'options' : ['Database administration', 'Database manager', 'Database user', 'Database oprator', ],
'correct_option' : 'Database administration',
'topics' : ['Software Applications',]},
{'question_string' : 'The following are benefits of ICT EXCEPT....', 
'options' : ['Spreading information', 'Makes the work faster', 'lncreases productivity', 'increases loss of job', ],
'correct_option' : 'increases loss of job',
'topics' : ['General Information Technology',]},
{'question_string' : 'The vertical lines represented by letters are....', 
'options' : ['Rows', 'Column', 'Worksheets', 'Formula', ],
'correct_option' : 'Column',
'topics' : ['Computer Hardware',]},
{'question_string' : 'Which of the following is the advantage of playing computer games', 
'options' : ['Addiction', 'Expensive', 'Waste time', 'Relaxes the brain', ],
'correct_option' : 'Expensive',
'topics' : ['General Information Technology',]},
{'question_string' : 'The intersection of a row and a column is called...', 
'options' : ['Range', 'Cell', 'Sheet', 'Row', ],
'correct_option' : 'Cell',
'topics' : ['Computer Hardware',]},
{'question_string' : 'Which of the following will copy a part or a whole document in Microsoft word?', 
'options' : ['CTRL+S', 'CTRL+C', 'SHIFT+C', 'CTRL+X', ],
'correct_option' : 'CTRL+C',
'topics' : ['Software Applications',]},
{'question_string' : 'The following are functions of digital literacy EXCEPT ability to...', 
'options' : ['Create and organize', 'Understand', 'Evaluate', 'Email,browse and phinching', ],
'correct_option' : 'Email,browse and phinching',
'topics' : ['Networks and the Internet',]},
{'question_string' : 'The following are examples of graphic package EXCEPT', 
'options' : ['Paint', 'Coreldraw', 'Adobe photoscope', 'Notepad', ],
'correct_option' : 'Notepad',
'topics' : ['Software Applications',]},
{'question_string' : 'Which of the following sets is needed to connect to the internet?', 
'options' : ['Monitor, Keyboard, Mouse and Modem', 'Telephone line, PDA,Modern and Computer', 'Telephone line, Modern,Computer and ISP', 'Modem, Computer,PDA and ISP', ],
'correct_option' : 'Telephone line, Modern,Computer and ISP',
'topics' : ['Computer Hardware',]},
{'question_string' : 'The technology that provides access to information through telecommunication is....', 
'options' : ['Satelite', 'lnternet', 'Tele conferece', 'lnformation', ],
'correct_option' : 'lnformation',
'topics' : ['General Information Technology',]},
{'question_string' : 'The new economy has been described as....', 
'options' : ['Digital economy', 'Citizen economy', 'Knowledge economy', 'Skill economy', ],
'correct_option' : 'Digital economy',
'topics' : ['General Information Technology',]}
]


    


class BasicTechnology(Science):
    topics = [
        'General Basic Technology',
            'Workshop and Environmental Safety',
            'Materials Technology',
            'Building Technology',
            'Electrical and Electronics Technology',
            'Woodwork ',
            'Metalwork',
            'Drawing and Construction',
            'Machines and Tools',
        ]
##    questions = []
class BasicScience(Science):
    topics = [
        'General Basic Science',
            'The Environment',
            'Living Things',
            'Chemicals and Materials',
            'Energy and Mechanics',
            'Outer Space and Radioactivity',
            'Human Health and Development',]
##    questions = []
class PhysicalHealthEducation(Science):
    topics = [
        'General Physical and Health Education',
            'Personal Fitness and Recreation',
            'Sports and Games',
            'Diseases and Personal Health',
            'Drug use and abuse',
            'Food and Nutrition',
            'Personal and Sports Safety',
            'Environmental Health',]
##    questions = []
class InformationTechnology(Science):
    topics = [
        'General Information Technology',
            'Computer Hardware',
            'Software Applications',
            'Networks and the Internet',
            'Computer Ethics and Security',
            'Operating Systems and Computer Logic',]
##    questions = []




class EnglishLessonApp(tk.Frame):
    """ Entry class into the application"""

    def __init__(self, parent):

        tk.Frame.__init__(self)
        self.parent = parent


        
        # Dictionary of subject strings and corresponding objects
        
##        self.subjects_dict = {
##                              
##                              'Basic Science' : BasicScience(),
##                              'Basic Technology' : BasicTechnology(),
##                              'Physical and Health Education' : PhysicalHealthEducation(),
##                              'Information Technology' : InformationTechnology(),                              
##                              'English Language': English()
##                              }
        self.subjects_dict = {
                                                         
                              'English Language': English()
                              }
        # Current user
        self.user_firstname = ''
        self.user_lastname = ''
        self.logged_in = False

        # Current subject
        self.current_subject = None

        # Current subject string
        self.current_subject_string = ''
        

        # Current user selection for lesson topic
        self.current_topic = ''

        # Number of test questions requested
        self.num_test_questions = 0
        

        # Default number of questions in practice exercise
        self.NUM_PRACTICE_QUESTIONS = 5

        # Dictionary of questions, options, and answers for exam (both practice and test)
        self.quiz_dictionary = {'questions_list':[], 'answers_list':[], 'options_list':[]}

        # Dictionary of missed questions, options, and answers 
        self.missed_questions_dictionary = {'questions_list':[], 'answers_list':[], 'options_list':[]}

        
        # Dictionary of user-selected topic strings : number of questions    
        self.chosen_topics_dict = {}


        # Collection of indices of wrongly answered questions
        self.wrong_question_numbers = []

        #  Collection of indices of correctly answered questions
        self.correct_question_numbers = []

        # Percent score on current test
        self.current_score = 0

                # Set learning mode vs testing mode
        self.learning_mode = True

        # This step is to enable frame switching
        self._frame = None


        # Call up the home window

        self.show_frame(LoginHome)
        


    def show_frame(self, frame_class):
        '''Hide current frame and replace with new one'''
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.pack_forget()
        self._frame = new_frame
        self._frame.pack(fill='both', expand=True)
        
        if self.logged_in:
        
            
            root.title(self.user_firstname + ' ' + self.user_lastname[0] + ' ' + '@MSSG CLASSROOM')
    
        
    def set_topic(self, topic_str):
        '''
        Sets current topic based on user selection
        '''
        self.current_topic = topic_str
        
    def set_subject(self, subject_str):
        '''
        Sets current subject based on user selection
        '''
        self.current_subject = self.subjects_dict[subject_str]
        self.current_subject_str = subject_str

    def start_lesson_exercises(self, topic, numquestions):
        """Starts lesson-based exercises """
        # Exit if no ready topics or questions (subject not ready)
        if len(self.current_subject.topics) == 0 or len(self.current_subject.questions) == 0:

            messagebox.showerror('Error',
                                 'This test is not yet ready.\n \
Your teacher will let you know when it is ready.')
            self.show_frame(SubjectChooser)
            return
        questions_list = self.current_subject.questions

        # Shuffle questions
        random.shuffle(questions_list)


        counter = 0
        
        for question in questions_list:
            # If the target topic is in the list of topics associated with the question
            if  topic in question['topics']:
            
                self.quiz_dictionary['questions_list'].append(question['question_string'])

                random.shuffle(question['options'])

                answer_index = question['options'].index(question['correct_option']) + 1

                self.quiz_dictionary['options_list'].append(question['options'])
                self.quiz_dictionary['answers_list'].append(answer_index)
                counter += 1
                if counter == numquestions:
                    break
            

        # Open the quiz page
        self.show_frame(Quiz)

    def enable_learning_mode(self):
        self.learning_mode = True

    def enable_test_mode(self):
        self.learning_mode = False
    
    def goto_test(self):
        """ Opens the landing page for a test where user selects topics and number of questions"""
        
        self.show_frame(QuizHome)

   
    def start_test(self, topics, numquestions):
        """ Triggers the start of a test """
        
       # Allocate number of questions for each topic
       
        numquestions_per_topic = int(numquestions/len(topics))
            
        # Account for leftover questions from the integer division above
        undistributed_questions = numquestions % len(topics)

        # Populate chosen topics dictionary,
        # allocating the average number of questions per topic to each topic

        for topic in topics:
            self.chosen_topics_dict[topic] = numquestions_per_topic

            
        # Handling cases of uneven distribution (leftover questions)
        if undistributed_questions > 0: 

            # Add 1 more question to other topics as needed in order to
            # round total number of questions up to expected value

            key_list = list(self.chosen_topics_dict.keys())

            for i in range(undistributed_questions):
            
                self.chosen_topics_dict[key_list[i]] += 1


        # Populate quiz dictionary of topics and questions for the test
        self.quiz_dictionary = self.create_quiz_dict(self.chosen_topics_dict)
        
        # Bring up the quiz window
        self.show_frame(Quiz)

    
    def create_quiz_dict(self, topics_dict):
        """ Builds a dictionary of quiz topics and questions.

            Accepts a dictionary of topics/number of questions per topic as input
        """

        # Instantiate and populate dictionary of questions, answers, and options
        quiz_dictionary = {'questions_list':[], 'answers_list':[], 'options_list':[]}

        # Pull collection of questions for current subject
        questions_list = self.current_subject.questions

        # Shuffle questions
        random.shuffle(questions_list)

        # Loop over each topic in the dictionary

        for topic in topics_dict.keys():
            
            counter = 0
            
            for question in questions_list:
                # If the target topic is in the list of topics associated with the question
                if  topic in question['topics']:

                    # Ensure the question is not already included via another topic
                    if question['question_string'] not in quiz_dictionary['questions_list']:
                
                        quiz_dictionary['questions_list'].append(question['question_string'])

                        random.shuffle(question['options'])

                        answer_index = question['options'].index(question['correct_option']) + 1

                        quiz_dictionary['options_list'].append(question['options'])
                        quiz_dictionary['answers_list'].append(answer_index)
                        counter = counter + 1
                        if counter == topics_dict[topic]:
                            break


        return quiz_dictionary

    def evaluate_answer(self, question_number, answer_string):
        """ Evaluates answer and updates tally of correct  and incorrect responses.
            Returns True if the answer was correct, otherwise False        
        """


        # Compare answer string with correct answer for the question
        # Depending on the answer, add to correct or incorrect answers list
        if answer_string == self.quiz_dictionary['answers_list'][question_number]:
            self.correct_question_numbers.append(question_number)
            return True
        else:
            self.wrong_question_numbers.append(question_number)
            return False


    def compute_results(self):
        """ Compute final results and return string for display """

        total = len(self.quiz_dictionary['questions_list'])
        correct = len(self.correct_question_numbers)
        wrong = len(self.wrong_question_numbers)
        self.current_score = int(correct / total * 100)

        result_string = ('You scored ' + str(self.current_score) + '%.\n'
                         'Out of ' + str(total) + ' questions:\n' +  
                         str(correct) + ' correct\n' + str(wrong) + ' wrong.')

        return result_string

    def finalize_test(self):
        self.record_session(self.num_test_questions, self.current_score)
        """ Reset collections, and redirect to start a new test or other options for the user """
         # Clear question entries in the quiz dictionary
        self.quiz_dictionary = {'questions_list':[], 'answers_list':[], 'options_list':[]}

        # Clear entries in missed questions dictionary
        self.missed_questions_dictionary = {'questions_list':[], 'answers_list':[], 'options_list':[]}

        # Clear the list of chosen topics for the completed test
        self.chosen_topics_dict.clear()

        # Clear list of indices of wrongly answered questions
        self.wrong_question_numbers = []

        #  Clear list  of indices of correctly answered questions
        self.correct_question_numbers = []

        # Return to home screen
        self.show_frame(SubjectChooser)
        
    def record_session(self, numquestions, percent_score):
        folder = './Records'
        if not os.path.exists(folder):
            os.makedirs(folder)

        filepath = folder + '/' + self.user_firstname + self.user_lastname + '.txt'
        today = date.today()
        datestr = today.strftime('%x')
        with open(filepath, 'a') as outfile:
            # Learning mode, no score recorded
            if self.learning_mode:
                outfile.write(datestr + ', ' + self.current_subject_str + ', ' + 
                              str(numquestions) + 'questions, Learning\n')

            else: # Test mode, score recorded
                outfile.write(datestr + ', ' + self.current_subject_str + ', ' +
                              str(numquestions) + 'questions, ' + str(percent_score) + '%\n')
                
        
            
  
    def open_video(self, filename):
        """ Opens a lesson video file from OS program """
        # Exit if video not found
        if not os.path.exists(filename):
            messagebox.showerror('Error',
                                 'This video is not yet ready.\n \
Your teacher will let you know when it is ready.')
            return
        if sys.platform == "win32":
            os.startfile(filename)
        else:
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, filename])

class LoginHome(tk.Frame):
    """User login page"""

    def __init__(self, controller):
        tk.Frame.__init__(self, bg='light blue')
        self.controller = controller
        label = tk.Label(self,
                         text="Please enter your first name and last name",
                         font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        
        # Entry fields for first and last names
        firstname_frame = tk.Frame(self, bg='#6FAFE7')
        firstname_frame.pack()

        tk.Label(firstname_frame, text='First name',
                 bg='#6FAFE7').pack(side='left', padx=5)

        self.firstname_entry = tk.Entry(firstname_frame, bd=3)
        self.firstname_entry.pack(side='right')

        lastname_frame = tk.Frame(self, bg='#6FAFE7')
        lastname_frame.pack()

        tk.Label(lastname_frame, text='Last name',
                 bg='#6FAFE7').pack(side='left', padx=5)

        self.lastname_entry = tk.Entry(lastname_frame, bd=3)
        self.lastname_entry.pack(side='right')

        # login button

        login_btn = tk.Button(self, text='Go to classroom',
                              command=self.login_btn,
                              bg='#6FAFE7', width=20)
        login_btn.pack(pady=5)

        # FUTURE IMPLEMENTATION -REMEMBER ME AND FORGOT PASSWORD
        # Remember me and forgot password
##bottom_frame = Frame(root, bg="#6FAFE7")
##bottom_frame.pack()
##
##var = IntVar()
##
##remember_me = Checkbutton(bottom_frame, text="Remember me", bg="#6FAFE7", command=toggled, variable=var)
##remember_me.pack(side='left', padx=19)
##
### The forgot password Label is just a placeholder, has no function currently
##forgot_pswrd = Label(bottom_frame, text="Forgot password?", bg="#6FAFE7")
##forgot_pswrd.pack(side="right", padx=19)


    # Login button
    def login_btn(self):

        # Ensure both fields are filled
        entered_fname = self.firstname_entry.get()
        entered_lname = self.lastname_entry.get()

        if not entered_fname.isalpha():
            messagebox.showerror('Error', 'You must enter a valid first name')

        elif not entered_lname.isalpha():
            messagebox.showerror('Error', 'You must enter a valid last name')
        else:
            self.controller.user_firstname = entered_fname
            self.controller.user_lastname = entered_lname
            self.controller.logged_in = True
            self.controller.show_frame(SubjectChooser)
            
        
class SubjectChooser(tk.Frame):
    """Displays listing of subjects to choose from"""

    def __init__(self, controller):
        tk.Frame.__init__(self, bg='light green')
        label = tk.Label(self,
                         text='Welcome, ' + controller.user_firstname + '. Please choose a subject',
                         font=LARGE_FONT)
        label.pack(pady=10, padx=10)
       
        # Placeholder for all topics, probably a listbox etc later

        subjects_button_frame = tk.Frame(self)

       # Populate the subject buttons
        for subject in controller.subjects_dict.keys():
            
            subject_button = tk.Button(subjects_button_frame, text=subject,
                                    command= lambda subject = subject : [controller.set_subject(subject),
                                                      controller.show_frame(SubjectHome)])
            
            subject_button.pack(side='top', fill='x')

        subjects_button_frame.pack()



class SubjectHome(tk.Frame):
    """User home page"""

    def __init__(self, controller):
        tk.Frame.__init__(self, bg='light blue')
        self.controller = controller
        label = tk.Label(self, text="What do you want to do today?",
                         font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button_do_lesson = tk.Button(self, text="Watch a video lesson",
                                    command= lambda:controller.show_frame(TopicsHome))

        button_do_lesson.pack(pady=10, padx=10)

        button_take_test = tk.Button(self, text="Take a test",
                                    command= lambda: controller.goto_test())
        button_take_test.pack(pady=10, padx=10)


class TopicsHome(tk.Frame):
    """Displays listing of lesson topics to choose from"""

    def __init__(self, controller):
        tk.Frame.__init__(self, bg='light blue')
        label = tk.Label(self, text="Choose a topic", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
       
        # Placeholder for all topics, probably a listbox etc later

        topicsbutton_frame = tk.Frame(self)

       # Populate the topic buttons
        for topic in controller.current_subject.topics:
            
            topicbutton = tk.Button(topicsbutton_frame, text=topic,
                                    command= lambda topic = topic: [controller.set_topic(topic),
                                                      controller.show_frame(LessonHome)])
            topicbutton.pack(side='top', fill='x')

        topicsbutton_frame.pack()

                                   
class LessonHome(tk.Frame):
    """Home for a lesson topic, pointing to lesson video or practice quiz"""
    
    def __init__(self, controller):

        tk.Frame.__init__(self, bg='light blue')

        #  Topic label
        label = tk.Label(self, text=controller.current_topic, font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        # Button to play video
        
        # TODO: change this to call videos independent of OS
        button_watchvideo = tk.Button(self, text="Watch Lesson Video",
                                    command= lambda: controller.open_video
                                      (controller.current_topic + '.mp4'))

        button_watchvideo.pack()

        button_doquestions = tk.Button(self, text="Do Lesson Questions",
                                command= lambda: controller.start_lesson_exercises(
                                    controller.current_topic, controller.NUM_PRACTICE_QUESTIONS))
        button_doquestions.pack()
  

# TODO: Implement this class later to have self-contained video frame
# not relying on calling OS video play feature
class LessonVideo(tk.Frame):
    def __init__(self, controller):
         tk.Frame.__init__(self, bg='light blue')



class QuizHome(tk.Frame):
    """ Landing page for a test, where user chooses topics and number of questions """


    def __init__(self, controller):
        tk.Frame.__init__(self)
        self.controller = controller      

        # Entry field for number of questions desired

        self.numquestions_field = tk.Entry(self)

        # List of checkboxes

        self.cb_list = []
        
        self.display_title()
        
        self.display_numquestions_field() 

        self.checkboxes()
        
        self.make_start_button()

        # Value for mode selection button, default to 1 for Learning mode

        self.selected_mode = tk.IntVar(value=1)
        self.select_mode_radiobuttons()


    def display_numquestions_field(self):
        """ Shows field for number of questions """

        entry_label = tk.Label(self, text='Enter number of questions wanted (maximum of 20)')
        
        self.numquestions_field.insert(0, '2')
        entry_label.pack()
        self.numquestions_field.pack() 


    def make_start_button(self):
        """ Creates start button """

        start_button = tk.Button(self, text='Start Test', command= self.configure_test,
                              width=10, bg='green', fg='white', font=('ariel',16,'bold'))

        start_button.pack(side=tk.BOTTOM, pady=(10,50))
        
    def display_title(self):
        """ Displays title """
        title = tk.Label(self, text='PRACTICE EXAM',width=30,
                      fg='black', font=('ariel', 20, 'bold'))

        title.pack(pady=20)
        



    def checkboxes(self):
        """ Checkboxes for topics """

        frame = tk.LabelFrame(self, text='Select the topics you want', padx=20, pady=20)
        frame.pack(pady=20, padx=10)

        # Populate checkboxes with topics
        for topic in self.controller.current_subject.topics:

            # Variable to keep track of state of checkbox
            state = tk.IntVar()
            cb = tk.Checkbutton(frame, text=topic, variable=state, width=200, anchor='w')
            cb.checked = state
            self.cb_list.append(cb)
            cb.pack()


    # Radio buttons to select mode
    def select_mode_radiobuttons(self):
        rb_learning = tk.Radiobutton(
            self, text='Learning Mode', command=self.select_mode, variable=self.selected_mode, value=1
            )
        rb_learning.pack(anchor='w')
        rb_test = tk.Radiobutton(
            self, text='Test Mode', command=self.select_mode, variable=self.selected_mode, value=2
            )
        rb_test.pack(anchor='w')

    # User selects learning versus test mode
    def select_mode(self):
        if self.selected_mode.get() == 1:
            self.controller.learning_mode = True
        else:
            self.controller.learning_mode = False
            
    def configure_test(self):
        # Exit if no ready topics or questions (subject not ready)
        if (len(self.controller.current_subject.topics) == 0 or
            len(self.controller.current_subject.questions) == 0):

            messagebox.showerror('Error',
                                 'This test is not yet ready.\n \
Your teacher will let you know when it is ready.')
            self.controller.show_frame(SubjectChooser)
            return

        # Get the selected topic checkboxes
        selected_topics = []
        for item in self.cb_list:
            if item.checked.get():

                # Get the quiz topic object from the topic string
                selected_topics.append(item.cget('text'))

        # Initialize total number of questions
        
        
        numquestions = 0
        
        # Get input string for number of questions

        numquestions_str = self.numquestions_field.get()
        
        # Validation of user entries        
        # If user did not select any topic

        if len(selected_topics) == 0:
            messagebox.showerror('Error', 'You must select a topic')

        # If number of questions is not a valid number
        elif  not numquestions_str.isnumeric():
            messagebox.showerror('Error', 'You must enter a valid number')

        else:
            # Get the selected number of questions
            numquestions = int(self.numquestions_field.get())
            self.controller.num_test_questions = numquestions

        # If there are more topics than questions, omit the most recent topics
        if numquestions < len(selected_topics):
            numextratopics = len(selected_topics)- numquestions
            for i in range(numextratopics):
                selected_topics.pop()

        # Send parameters to begin test

        self.controller.start_test(selected_topics, numquestions)



class Quiz(tk.Frame):
    """ Class for display of test window, questions"""

    def __init__(self, controller):
        tk.Frame.__init__(self,  bg='light blue')
        self.controller = controller
        
        self.questions_list = controller.quiz_dictionary['questions_list']
        self.options_list = controller.quiz_dictionary['options_list']
        self.answers_list = controller.quiz_dictionary['answers_list']

        self.current_question_num = 0

        self.display_question()

        self.selected_option= tk.IntVar()

        # Create radio button group for options display

        self.option_buttons=self.radio_buttons()

        # Populate option buttons with text of answer options

        self.display_options()

        self.next_button = tk.Button(self, text='Next', command=self.next_btn,
                             width=15, bg='green', fg='white', font=('ariel',14,'bold'))


        self.submit_button = tk.Button(self, text='Submit Answer',
                                    state=tk.DISABLED, command=self.show_feedback,
                               width=15, bg='light green', fg='black', font=('ariel', 14, 'bold'))

        self.submit_button.place(x=600, y=380)

        self.finish_button = tk.Button(self, text='Finish', command=self.finish_btn,
                             width=15, bg='green', fg='white', font=('ariel',14,'bold'))

        self.review_missed_button = tk.Button(self, text='Review questions you missed', command=self.review_missed_btn,
                             width=25, bg='blue', fg='white', font=('ariel',12,'bold'))




        # To show whether the answer is correct or wrong
        self.feedback_label = tk.Label(self, pady=10, font=("ariel", 15, "bold"), justify=tk.LEFT)
        self.feedback_label.place(x=700, y=250)

        self.data_size=len(self.questions_list)
        

    def display_result(self):

        if self.controller.learning_mode:
            messagebox.showinfo('Finished', 'Thank you for finishing the questions!')
        else:         
            messagebox.showinfo('Result', self.controller.compute_results())
        
    def show_feedback(self):

        answer_str = self.options_list[self.current_question_num][self.answers_list[self.current_question_num] - 1]


        
        if self.controller.evaluate_answer(self.current_question_num, self.selected_option.get()):
        
            self.feedback_label["fg"] = "green"
            self.feedback_label["text"] = 'Correct answer! \u2705'
        else:
            self.feedback_label['fg'] = 'red'
            self.feedback_label['text'] = ('\u274E Not correct \n'
                                         'Correct answer is: ' + answer_str)
            # Add missed question to collection of missed questions
            self.controller.missed_questions_dictionary['questions_list'].append(self.questions_list[self.current_question_num])
            self.controller.missed_questions_dictionary['answers_list'].append(self.answers_list[self.current_question_num])
            self.controller.missed_questions_dictionary['options_list'].append(self.options_list[self.current_question_num])

        self.feedback_label.place(x=500, y=250)
        self.submit_button.place_forget()

        # If it is the last question, show Finish button
        # otherwise show Next button

        if self.current_question_num==self.data_size - 1:
            # Recycle missed questions if in learning mode
            if self.controller.learning_mode:
            # if no more missed questions
                if len(self.controller.missed_questions_dictionary['questions_list']) == 0:
                    self.finish_button.place(x=600, y=380)
                else:
                    self.review_missed_button.place(x=600, y=380)
                    

            else: # in testing mode
                self.finish_button.place(x=600, y=380)
        else:
            self.next_button.place(x=600, y=380)

    def enable_submit(self):
        self.submit_button['state'] = tk.NORMAL

    def next_btn(self):

        self.feedback_label.place_forget()
        self.submit_button['state'] = tk.DISABLED
        

        self.current_question_num += 1
       
        self.display_question()
        self.display_options()

        self.next_button.place_forget()
        self.submit_button.place(x=600, y=380)

    def finish_btn(self):

        
        self.display_result()
        
        self.controller.finalize_test()
        
    def review_missed_btn(self):
        # reassign quiz collection to missed questions
        self.controller.quiz_dictionary = self.controller.missed_questions_dictionary
        # Clear missed questions collection
        self.controller.missed_questions_dictionary = {'questions_list':[], 'answers_list':[], 'options_list':[]}
        self.destroy()
        self.controller.show_frame(Quiz)
        

    def display_options(self):
        val=0

        self.selected_option.set(0)

        for option in self.options_list[self.current_question_num]:
            self.option_buttons[val]['text'] = option
            val+=1

    def display_question(self):


        instructions = tk.Label(self, text='Choose the best option to complete the sentence below:',
                             font=('ariel', 14, 'normal'), anchor='w')
        question_num = tk.Label(self, text='Question ' + str(self.current_question_num + 1),
                             font=('ariel', 16, 'bold'), anchor='w')

##        question_text = tk.Label(self, text=self.questions_list[self.current_question_num], width=80,
##                     font=('ariel', 12, 'normal'), anchor='w')

        question_text = tk.Text(self, font=('ariel', 12, 'normal'), height = 4, width = 80)
        
        question_text.insert(tk.END, self.questions_list[self.current_question_num])

        instructions.place(x=70, y=10)
        #instructions.pack()
        

        question_num.place(x=400, y=40)
        #question_num.pack()

        question_text.place(x=70, y=100)
       # question_text.pack()


    def radio_buttons(self):

        radio_list = []

        y_pos = 200    

        while len(radio_list) < 5:

            radio_btn = tk.Radiobutton(self,
                                    command=self.enable_submit,
                                    text='',variable=self.selected_option,
                                    value=len(radio_list) + 1, font=('ariel', 12))

            radio_list.append(radio_btn)

            radio_btn.place(x=100, y=y_pos)

            y_pos += 40

        return radio_list


if __name__ == '__main__':
    
    root = tk.Tk()
    root.title('MSSG CLASSROOM')
    root.geometry('900x600')
    app = EnglishLessonApp(root)
    
    
    app.mainloop()



        
