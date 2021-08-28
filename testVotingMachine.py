# Author: Kelsy watkins
# Purpose: Implement a VotingMachine class that can be used for a simple election.  
# Have methods to clear the machine state, to vote for a Democrat, to vote for a Republican, and to get the tallies for both parties.
# Have testVotingMachine file with at main() that will use this class VotingMachine and will print out the results.

from votingMachineClass import VotingMachine

def main():
    machine = VotingMachine()
    print("Vote 'r' for republican and 'd' for democrat, Press enter after each entry.\nPress 'c' to clear votes and start over. Press 't' to enter all votes and get tallies.")

    while machine._inLoop == True:
        userInput = input("Enter: ")
        userInput = userInput.lower()
        if userInput == 'd':
            machine.voteDemocrat()
        elif userInput == 'r':
            machine.voteRepublican()   
        elif userInput == 'c':
            machine.clearState()   
            print("Machine cleared, enter in new data: ") 
        elif userInput == 't':
            machine.tallies()
        else:
            machine.wrongAnwser()

main()
