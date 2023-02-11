# To run script, just use "python3 key_generator.py"
# Generated files will appear in same dir wher this script located

import json
import random
import string

"""
def get_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))
"""

#Key count - change this one
total = 29000

# Inside 'result_en' change value for key translation
result_en = {'key_' + str(i): 'How bad you want to fill your product with keys? Answer - yes' for i in range (total)}
result_translations = {'key_' + str(i): 'key ' + str(i) for i in range (total)}


f1 = open('en.json', 'w')
f2 = open('de.json', 'w')
f3 = open('es.json', 'w')
f1.write(json.dumps(result_en, sort_keys=False, indent=4))
f2.write(json.dumps(result_translations, sort_keys=False, indent=4))
f3.write(json.dumps(result_translations, sort_keys=False, indent=4))
f1.close()
f2.close()
f3.close()