#This program implements a deque then uses a function to
#show the functionality and operations of a deque 
class Deque:
    def __init__(self):
        self.container = []

    def isEmpty(self):
        return self.container == []

    def addFront(self, item):
        self.container.append(item)

    def addRear(self, item):
        self.container.insert(0, item)

    def removeFront(self):
        return self.container.pop()

    def removeRear(self):
        return self.container.pop(0)

    def size(self):
        return len(self.container)


#palindrome checker to verify that the inputted string is a palindrome
#function that takes a string and checks whether it is a palindrome using
#a deque
def palindrome(string):
    #add the string to the deque
    char_deque = Deque()
    for char in string:
        char_deque.addRear(char)

    still_equal = True
    while char_deque.size() > 1 and still_equal:
        first = char_deque.removeFront()
        last = char_deque.removeRear()
        if first != last:
            print('{}, is not a palindrome.' .format(string))
            still_equal = False

    return still_equal

print(palindrome('racecar'))
print(palindrome('tenet'))
print(palindrome('eggs'))