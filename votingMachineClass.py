# Purpose: Implement a VotingMachine class that can be used for a simple election.  
# Have methods to clear the machine state, to vote for a Democrat, to vote for a Republican, and to get the tallies for both parties.
# Have testVotingMachine file with at main() that will use this class VotingMachine and will print out the results.

class VotingMachine:
    _dem = 0
    _rep = 0
    _inLoop = True

    def clearState(self):
        self._dem = 0
        self._rep = 0

    def voteDemocrat(self):
        self._dem += 1

    def voteRepublican(self):
        self._rep += 1

    def tallies(self):
        self._inLoop = False 
        print("Total Democratic votes: ",self._dem)
        print("Total Republican votes: ",self._rep)     

    def wrongAnwser(self):
        print("Please enter the letters 'r' 'd' or 'c' or 't'.") 
