import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from pprint import pprint

import sqlite3
import base64

with sqlite3.connect('WordWise.kll.en.en.db') as f:
    lemmas = f.execute('SELECT id,lemma FROM lemmas').fetchall()
    senses = dict(f.execute('SELECT display_lemma_id,id FROM senses WHERE id>0').fetchall()[::-1])

display_lemma_ids = senses.keys()

csv = ['"id","word","full_def","short_def","example_sentence","hint_level"']

#https://github.com/tmilovanov/wisecreator/tree/master/senses
with open('2.txt', 'rb') as f:
    b = f.read().decode('utf-8').splitlines()

with open('3.txt', 'rb') as f:
    c = f.read().decode('utf-8').splitlines()

with open('4.txt', 'rb') as f:
    d = f.read().decode('utf-8').splitlines()

with open('5.txt', 'rb') as f:
    e = f.read().decode('utf-8').splitlines()

print('Please wait a moment.')

processed_word_count = 0

for id_, word in lemmas:
    if id_ in display_lemma_ids:
        
        processed_word_count += 1
        print('processed: ' + str(processed_word_count) + ' word')

        #amazon kindle wordwise sense id
        id = senses[id_]
        
        #wordwise hint level (5 is highest level only show when you choose show more hints in wordwise feature - mean more frequent used word in english)
        #https://github.com/tmilovanov/wisecreator/tree/master/senses
        if word in e:
            hint_level = '5'
        elif word in d:
            hint_level = '4'
        elif word in c:
            hint_level = '3'
        elif word in b:
            hint_level = '2'
        else:
            hint_level = '1'

        #get detail sense data
        with sqlite3.connect('WordWise.kll.en.en.db') as f:
            f.row_factory = sqlite3.Row
            cur = f.cursor()
            senses_data = cur.execute('SELECT display_lemma_id,id,full_def,short_def,example_sentence FROM senses WHERE id=' + str(id)).fetchone()

        #print(word)
        #pprint(senses_data['full_def'])
        
        full_def = senses_data['full_def']
        short_def = senses_data['short_def']
        example_sentence = senses_data['example_sentence']

        #build csv file with header: id, word, full_def, short_def, example_sentence, hint_level
        csv.append('{0},"{1}","{2}","{3}","{4}",{5}'.format(id, word.encode("utf-8", errors="ignore"), base64.b64decode(full_def).replace('"','`') if full_def is not None else '', base64.b64decode(short_def).replace('"','`') if short_def is not None else '', base64.b64decode(example_sentence).replace('"','`') if example_sentence is not None else '', hint_level))

with open('wordwise-dict.csv', 'wb') as f:
    f = f.write('\n'.join(csv).encode("utf-8", errors="ignore"))

print('Success!')
