def getStopWordList(fileName):
    stopWords = []
    fp = open(fileName, 'r')
    line = fp.readline()
    while line:
        if line[0] == '#':
            line = fp.readline()
            continue
        word = line.strip()
        stopWords.append(word)
        line = fp.readline()
    fp.close()
    print('get stop words done')
    print(stopWords)
    return stopWords

def removeStopWords(text, stopWords):
    result = ''
    for w in text.split(' '):
        if w not in stopWords:
            result = result + w + ' '
    print('remove stop words done')
    return result

def processText(text_file, stopWords):
    # skip label score line, step size should be 2
    fo = open(text_file, 'r')
    lines = fo.readlines()
    results = []
    for line in lines:
        line = line.lower()
        line = removeStopWords(line, stopWords)
        print(line)
        words = line.split()
        new_line = ''
        for w in words:
            # ignore if it is a stop word
            if w in stopWords:
                None
            # strip punctuation
            else:
                w = w.replace('''"''', ''' ''')
                w = w.replace('.', '')
                w = w.replace(',', '')
                w = w.replace('(', '')
                w = w.replace(')', '')
                new_line = new_line + w + ' '
        results.append(new_line)
    print('process', text_file, 'done')
    print(results)
    fo.close()
    return results

stopWords = getStopWordList('stopword_list.txt')
train_text = processText('train.txt', stopWords)
test_text = processText('test.txt', stopWords)
valid_text = processText('valid.txt', stopWords)

