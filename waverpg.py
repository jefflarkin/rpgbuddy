import re
from random import randint
def process_text(text):
  r = re.compile("(\[\[.*?\]\])")
  # Find all rolls in the given text
  for match in r.findall(text):
    # Strip out the brackets so we won't match this again later
    save = str(match)
    match = str(match).replace("[","").replace("]","")
    # Get the new roll string
    result = roll(match.strip())
    # Substitute roll code for result
    text = re.sub(re.escape(save),result,text,1)
  return text

def roll(text):
  r = re.compile("(\d+)[dD](\d+)[oO]?(\d*)\+?(\d*)")
  # match all roll codes in the string
  while 1:
    match = r.search(text)
    if match == None: break
    sum = 0
    rolls = []
    output = "["
    for i in range(int(match.group(1))):
      last = randint(1,int(match.group(2)))
      rolls.append(last)
      sum += last
      if i == (int(match.group(1))-1):
        output = "%s <strong style=\"color: red\">%d</strong>"%(output, last)
      else:
        output = "%s %d"%(output, last)
    while (match.group(3) != '') and (last >= int(match.group(3))):
      last = randint(1,int(match.group(2)))
      rolls.append(last)
      sum += last
      output = "%s %d"%(output, last)
    if match.group(4) != '':
      sum += int(match.group(4))
      output = "%s + %s"%(output, match.group(4))
    output = "%s ] = <strong>%s</strong>"%(output,sum)
    text = re.sub(re.escape(match.group(0)),output,text,1)

#  return r.sub(output,text)
  return text
