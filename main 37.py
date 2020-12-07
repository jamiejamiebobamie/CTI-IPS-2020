def bigram_frequency_analyzer(text):
  words = text.replace("\n"," ").split(" ")
  words = [word for word in words if (word != " " and len(word) > 0)]
  # key is two words
  # value is an array of "third word" 's and their counts
  histo = {}
  for k in range(2,len(words)):
    i=k-2
    j=k-1
    key = words[i] + " " + words[j]
    value = words[k]
    if key not in histo:
      histo[key] = [[value,1]]
    else:
      values = histo[key]
      found = False
      for l, val in enumerate(values):
        next_word, count = val
        if next_word == value:
          histo[key][l][1]+=1
          found = True
          break
      if not found:
        histo[key].append([value,1])
  output_string = ""
  for key,values in histo.items():
    output_string += key + " : "
    for val in values:
      word, count = val
      output_string += word +" (" + str(count) + ") "
    output_string+="\n"
  return output_string

# text = """I do not like green eggs and ham,
# I do not like them, Sam-I-Am!
# I do not like them with a fox,
# I do not like them in a box.
# I do not like them here or there,
# I do not like them anywhere!
# I do not like them, Sam-I-Am,
# I do not like green eggs and ham!"""

text = "a b c d e f g h i j k l m n o p q r s t u v w x y z "

print(bigram_frequency_analyzer(text))