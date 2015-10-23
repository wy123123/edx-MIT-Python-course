# Enter your code for NewsStory in this box
class NewsStory(object):
    
    def __init__(self,guid,title,subject,summary,link):
        self.Guid = guid
        self.title = title
        self.subject = subject
        self.summary = summary
        self.link = link
        
    def getGuid(self):
        return self.Guid
        
    def getTitle(self):
        return self.title
        
    def getSubject(self):
        return self.subject
        
    def getSummary(self):
        return self.summary
        
    def getLink(self):
        return self.link
        
        
        
# Enter your code for WordTrigger, TitleTrigger, 
# SubjectTrigger, and SummaryTrigger in this box
class WordTrigger(Trigger):
    def __init__(self, word):
        self.word = word.lower()

    def isWordIn(self, text):
        text = self.replacePunc(text)
        return self.word in text.lower().split()

    def replacePunc(self, text):
        for p in string.punctuation:
            text = text.replace(p, ' ')

        return text
                
            
class TitleTrigger(WordTrigger):
    def evaluate(self, story):
        return self.isWordIn(story.getTitle())

class SubjectTrigger(WordTrigger):
    def evaluate(self, story):
        return self.isWordIn(story.getSubject())

class SummaryTrigger(WordTrigger):
    def evaluate(self, story):
        return self.isWordIn(story.getSummary())
        
        
# Enter your code for WordTrigger, TitleTrigger,
# NotTrigger, AndTrigger, and OrTrigger in this box
class AndTrigger(Trigger):
    def __init__(self,trigger1,trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2
    def evaluate(self,story):
        return self.trigger1.evaluate(story) and self.trigger2.evaluate(story)
        
class OrTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2

    def evaluate(self, story):
        return self.trigger1.evaluate(story) or self.trigger2.evaluate(story)

class NotTrigger(Trigger):
    def __init__(self,trigger):
        self.result = trigger
    
    def evaluate(self, story):
        return not self.result.evaluate(story)


class WordTrigger(Trigger):
    def __init__(self, word):
        self.word = word.lower()

    def isWordIn(self, text):
        text = self.replacePunc(text)
        return self.word in text.lower().split()

    def replacePunc(self, text):
        for p in string.punctuation:
            text = text.replace(p, ' ')

        return text
                
            
class TitleTrigger(WordTrigger):
    def evaluate(self, story):
        return self.isWordIn(story.getTitle())


class PhraseTrigger(Trigger):
    def __init__(self, st):
        self.st = st
        
    def evaluate(self,story):
        return self.st in story.getSubject() or \
            self.st in story.getTitle() or \
            self.st in story.getSummary()
def filterStories(stories, triggerlist):
    k = []
    for story in stories:
        for tr in triggerlist:
            if tr.evaluate(story):
                k.append(story)
                break
    return list(k)
    
    
def makeTrigger(triggerMap, triggerType, params, name):
    """
    Takes in a map of names to trigger instance, the type of trigger to make,
    and the list of parameters to the constructor, and adds a new trigger
    to the trigger map dictionary.
    triggerMap: dictionary with names as keys (strings) and triggers as values
    triggerType: string indicating the type of trigger to make (ex: "TITLE")
    params: list of strings with the inputs to the trigger constructor 
    (ex: ["world"])
    name: a string representing the name of the new trigger (ex: "t1")
    Modifies triggerMap, adding a new key-value pair for this trigger.
    Returns a new instance of a trigger (ex: TitleTrigger, AndTrigger).
    """
    trigger = None

    if triggerType == "TITLE":
        trigger = TitleTrigger(params[0])
    elif triggerType == "SUBJECT":
        trigger = SubjectTrigger(params[0])
    elif triggerType == "SUMMARY":
        trigger = SummaryTrigger(params[0])
    elif triggerType == "NOT":
        trigger = NotTrigger(triggerMap[params[0]])
    elif triggerType == "AND":
        trigger = AndTrigger(triggerMap[params[0]], triggerMap[params[1]])
    elif triggerType == "OR":
        trigger = OrTrigger(triggerMap[params[0]], triggerMap[params[1]])
    elif triggerType == "PHRASE":
        trigger = PhraseTrigger(" ".join(params))

    triggerMap[name] = trigger
    return trigger
