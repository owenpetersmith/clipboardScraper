# Clipboard Phone Scraper for US or Canadian Phone Numbers
# Copy text onto clipboard prior to executing program
# Number of results is printed onto console
# Output is sent onto clipboard 

import re, pyperclip

emailRegex =  re.compile(r'''(
	[a-zA-Z0-9_.+]+    #name
	@    # @ symbol
	[a-zA-Z0-9_.+]+    # domain pt.1
	\.
	[a-zA-Z0-9]+ # domain pt.2
	)''',re.VERBOSE)

text = pyperclip.paste()

extractedEmails = emailRegex.findall(text)

if len(extractedEmails) == 0:
	print("No results found")
else:
	print(str(len(extractedEmails))+" result(s) found")
	pyperclip.copy('\n'.join(extractedEmails))