class Markov(object):

    """A simple trigram Markov model. The current state is a sequence of the
        two words seen most recently. Initially, the state is (None, None),
        since no words have been seen. Scanning the sentence "The man ate the
        pasta" would casue the model to go through the sequence of states:
        [(None, None), (None, 'the'), ('The','man'), ('man', 'ate'),
        ('ate', 'the')."""
    def __init__(self):
        self.model = {}
        self.state = (None, None)

    def add(self, word):
        if self.state in self.model:
            #We have an existing list of words for this state
            #just add this new one (word).
            self.model[self.state].append(word)
        else:
            #first occurrence of this state, create a new list
            self.model[self.state] = [word]
        # transition to the next state given next word
        self._transition(word)

    def reset(self):
        self.state = (None, None)

    def randomNext(self):
        #get list of next words for this state
        lst = self.model[self.state]
        #choose one at random
        choice = random.choice(lst)
        #transition to next state, given the word choice
        self._transition(choice)
        return choice

    def _transition(self, next):
        # help function to construct next state
        self.state = (self.state[1], next)