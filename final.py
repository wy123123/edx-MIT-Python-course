def insert(atMe, newFrob):
    """
    atMe: a Frob that is part of a doubly linked list
    newFrob:  a Frob with no links 
    This procedure appropriately inserts newFrob into the linked list that atMe is a part of.    
    """
    # Your Code Here
    #check if newFrob is alphabetically before atMe
    if checkPosition(atMe,newFrob)=='after' and checkPosition(atMe.getAfter(),newFrob)=='after':
        return insert(atMe.getAfter(),newFrob)
    elif checkPosition(atMe,newFrob)=='before' and checkPosition(atMe.getBefore(),newFrob)=='before':
        return insert(atMe.getBefore(),newFrob)
    elif checkPosition(atMe,newFrob)=='before' and (checkPosition(atMe.getBefore(),newFrob)=='after' or checkPosition(atMe.getBefore(),newFrob)=='end') :
    #elif checkPosition(atMe,newFrob)=='before' and checkPosition(atMe.getBefore(),newFrob)=='after':
        before_frob = atMe.getBefore()
        atMe.setBefore(newFrob)
        newFrob.setAfter(atMe)
        if before_frob:
            before_frob.setAfter(newFrob)
            newFrob.setBefore(before_frob)
    elif checkPosition(atMe,newFrob)=='after' and (checkPosition(atMe.getAfter(),newFrob)=='before' or checkPosition(atMe.getAfter(),newFrob)=='end'):
    #elif checkPosition(atMe,newFrob)=='after' and checkPosition(atMe.getAfter(),newFrob)=='before':
        after_frob = atMe.getAfter()
        atMe.setAfter(newFrob)
        newFrob.setBefore(atMe)
        if after_frob:
            after_frob.setBefore(newFrob)
            newFrob.setAfter(after_frob)
def checkPosition(atMe,newFrob):
    if atMe:
        a = [atMe.myName()]
        a.append(newFrob.myName())
        a.sort()
        if a[0]==atMe.myName():
            return 'after'
        else:
            return 'before'
    else:
        return 'end'
        
        
def findFront(start):
    """
    start: a Frob that is part of a doubly linked list
    returns: the Frob at the beginning of the linked list 
    """
    # Your Code Here
    if start.getBefore():
        return findFront(start.getBefore())
    else:
        return start
