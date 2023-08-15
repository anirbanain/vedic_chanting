import string

def remove_punctuation(sentence):
    # Remove punctuation from the sentence
    sentence_no_punct = sentence.translate(str.maketrans('', '', string.punctuation))
    
    # Create a list of words
    word_list = sentence_no_punct.split()
    
    return word_list

def jata_patha(mantra):
  size = len(mantra)
  mantra.append('')
  print("\033[1m",'jaṭā-pāṭha',"\033[0m")
  for ii in range(size):
    print(mantra[ii],mantra[ii+1],mantra[ii+1],mantra[ii],mantra[ii],mantra[ii+1],' ~ ')

def mala_patha(mantra):
  size = len(mantra)
  mantra.append('')
  print("\033[1m",'mālā-pāṭha',"\033[0m")  
  for ii in range(size):
    print(mantra[ii],mantra[ii+1],' ~ ',mantra[ii+1],mantra[ii],' ~ ',mantra[ii],mantra[ii+1],' ~ ')

def sikha_patha(mantra):
  size = len(mantra)
  mantra.append('')
  mantra.append('')
  print("\033[1m",'śikhā-pāṭha',"\033[0m")  
  for ii in range(size):
    print(mantra[ii],mantra[ii+1],' ~ ',mantra[ii+1],mantra[ii],' ~ ',mantra[ii],mantra[ii+1],mantra[ii+2],' ~ ')

def rekha_patha(mantra):
  #mantra.insert(0,'')
  size = len(mantra)
  mantra.append('')
  mantra.append('')
  print("\033[1m",'rekhā-pāṭha',"\033[0m")  
  for ii in range(size):
    end = min(2*ii,size)
    first = [mantra[ii]]
    for jj in range(ii-1,end):
      first.append(mantra[jj+2])
    first = list(filter(lambda item: item != "", first))
    print(' '.join(first),' ~ ',end = '')
    first.reverse()
    print(' '.join(first),' ~ ',mantra[ii],mantra[ii+1],' ~ ')

def dhvaja_patha(mantra):
  size = len(mantra)
  mantra.append('')
  mantra.insert(0,'')
  print("\033[1m",'dhvaja-pāṭha',"\033[0m")  
  for ii in range(1,size+1):
    print(mantra[ii],mantra[ii+1],' ~ ',mantra[size-ii],mantra[size-ii+1],' ~ ')

def ghana_patha(mantra):
  size = len(mantra)
  mantra.append('')
  mantra.append('')
  mantra.append('')
  print("\033[1m",'ghana-pāṭha',"\033[0m")  
  for ii in range(size):
    print(mantra[ii],mantra[ii+1],mantra[ii+1],mantra[ii],mantra[ii],mantra[ii+1],mantra[ii+2],mantra[ii+2],mantra[ii+1],mantra[ii],mantra[ii],mantra[ii+1],mantra[ii+2],' ~ ')

def danda_path(mantra):
  size = len(mantra)
  mantra.append('')
  mantra.append('')
  mantra.append('')
  print("\033[1m",'daṇḍa-pāṭha',"\033[0m")  
  for ii in range(size):
     print(mantra[ii],mantra[ii+1],' ~ ',mantra[ii+1],mantra[ii],' ~ ',mantra[ii],mantra[ii+1],' ~ ',mantra[ii+1],mantra[ii+2],' ~ ',mantra[ii+2],mantra[ii+1],mantra[ii],' ~ '\
           ,mantra[ii],mantra[ii+1],' ~ ',mantra[ii+1],mantra[ii+2],' ~ ',mantra[ii+2],mantra[ii+3],' ~ ',mantra[ii+3],mantra[ii+2],mantra[ii+1],mantra[ii],' ~ ',mantra[ii],mantra[ii+1],' ~ ')

def ratha_patha(mantra):
  size = len(mantra)
  mantra.append('')
  mantra.append('')
  mantra.append('')

# Example sentence
input_sentence = "tyaṃ su meṣaṃ mahayā svarvidaṃ śataṃ yasya subhvaḥ sākamīrate"
words_without_punct = remove_punctuation(input_sentence)

print(input_sentence)
jata_patha(words_without_punct)
