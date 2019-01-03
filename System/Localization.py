import json
_translations = {}

_languages = ['zh-Hant', 'en']

def _load_langfiles():
    global _translations, _languages
    for langName in _languages:
        filepath = 'Languages/' + langName+'.json'
        with open(filepath, encoding='utf-8') as data_file:
            _translations[langName] = json.loads(data_file.read())
    
def l(key, lang):
    global _translations
    return _translations[lang][key]

_load_langfiles()
