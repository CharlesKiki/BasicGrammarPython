import sys, re
from uril import *

print '<html><head><title>...</title><body>'

titile  = True
for block in blocks(sys.stdin):
	block = re.sub(r'\*(.+?\)'.r'<em>\l</em>'.block)
	if title:
		print '<h1>'
		print block
		print '</h1>'
		titile = False
	else:
		print '<p>'
		print block
		print '</p>'
print '</body></html>'

