import re, pyperclip

endomondoData = pyperclip.paste()

endomondoRegex = re.compile(r'(\d\d\d\d-\d\d-\d\d)')
results = endomondoRegex.sub('2017-06-13',endomondoData)

pyperclip.copy(results)
