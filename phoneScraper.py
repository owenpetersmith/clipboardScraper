# Clipboard Phone Scraper for US or Canadian Phone Numbers
# Copy text onto clipboard prior to executing program
# Number of results is printed onto console
# Output is sent onto clipboard 

import re, pyperclip

phoneRegex =  re.compile(r'''(
	( ( \d\d\d )|( \(\d\d\d\) ) )? # Area Code
	(\s|-)
	\d\d\d
	(\s|-)
	\d\d\d\d
	(((ext(\.)?\s)|x) #extension label
	(\d{2,5}))? # extension number
	)''',re.VERBOSE)

text = pyperclip.paste()

extractedPhoneNumbers = phoneRegex.findall(text)

if len(extractedPhoneNumbers) == 0:
	print("No results found")
else:
	allPhoneNumbers = []
	for entry in extractedPhoneNumbers:
		allPhoneNumbers.append(entry[0])
	print(str(len(allPhoneNumbers))+" result(s) found")
	pyperclip.copy('\n'.join(allPhoneNumbers))
