def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    ### TODO.
    DICT = {}
    for i in range(26):
        if i + shift >25:
            DICT[string.ascii_uppercase[i]]=string.ascii_uppercase[(i + shift)%25-1]
        else:
            DICT[string.ascii_uppercase[i]]=string.ascii_uppercase[(i + shift)]
        
    for i in range(26):
        if i + shift >25:
            DICT[string.ascii_lowercase[i]]=string.ascii_lowercase[(i + shift)%25-1]
        else:
            DICT[string.ascii_lowercase[i]]=string.ascii_lowercase[(i + shift)]

    return DICT # Remove this comment when you code the function


def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    ### TODO
    encode = ""
    for i in text:
        try:
            encode+=(coder[i])
        except:
            encode+=i
    return encode
    
    
def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    ### TODO.
    ### HINT: This is a wrapper function.
    return applyCoder(text,buildCoder(shift))
    
    
def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    ### TODO
    s = text.split(" ")
    best = 0
    c_shift = 0
    for shift in range(0,26):
        score = 0
        for word in s:
            if isWord(wordList, applyShift(word, shift)):
                score +=1
        if score > best:
            best = score
            c_shift = shift
    return c_shift


def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Once you decrypt the message, be sure to include as a comment
    your decryption of the story.

    returns: string - story in plain text
    """
    ### TODO
    story = getStoryString()
    shift = findBestShift(loadWords(),story)
    return applyShift(story,shift)
