def count_words(text):
  punctuation = set("!@#$%^&*()}{][><.,?/_")
  # had some issues with cleaning commas from my corpus
  punctuation.add(",")
  text = text.split("\n")
  text = "".join([c for c in text if c not in punctuation]).lower().split(" ")
  histo = {}
  
  for word in text:
    new_word = ""
    for char in word:
      if char != ",":
        new_word+=char
    if new_word not in histo:
      histo[new_word] = 1
    else:
      histo[new_word] += 1
      
  result = []
  
  for word, count in histo.items():
    print(word+" "+str(count))
    result.append(word+" "+str(count))
  
  return result
  

example = "I do not like green eggs and ham, I do not like them, Sam-I-Am"
print(count_words(example))