import csv
import random 

def load_teams(filepath):
    teams=[]
    with open(filepath,"r") as file:
        csv_reader=csv.reader(file)
        next(csv_reader,None)
        for row in csv_reader:
            team_data={ 
                "name": row[1],
                "power":int(row[2]),
                "group":row[0]               
            }
            teams.append(team_data)
    return teams

class TeamNode:
    def __init__(self,team_name,power):
        self.name=team_name
        self.power=power
        self.points=0
        self.goalsFor=0
        self.goalsAgainst=0
        self.wins=0
        self.draws=0
        self.losses=0
        self.next=None
        
'''     
   def GetMatchesForDay(self):
            matches=[]
            teams=[]
            current=self.head
            while current:
                teams.append(current.name)
                current=current.next
            for i in range(len(teams)):
                for j in range(i+1,len(teams)):
                    matches.append((teams[i],teams[j]))
            return matches '''
        
class GroupLinkedList:
    
    def __init__(self):
        self.head=None
        
    def insert(self,team_name,power):
        #print("test")
        new_node=TeamNode(team_name,power)
        if not self.head:
            #print("new test")
            self.head=new_node
        else:
            #print("testing")
            current=self.head
            while current.next:
                current=current.next
            current.next=new_node
    
    def sort(self):
        if not self.head or not self.head.next:
            return 
        nodes=[]
        current=self.head
        while current:
            nodes.append(current)
            current=current.next
        nodes.sort(key=lambda x:(-x.points,x.goalsFor-x.goalsAgainst,-x.power))
        self.head=nodes[0]
        current=self.head
        for node in nodes[1:]:
            current.next=nodes
            current=node
        current.next=None
        
    def display_rankings(self):
        current=self.head
        print(f"| {'Team':<14} | {'Points':<6} | {'Wins':<4} | {'Draws':<5} | {'Losses':<6} | {'GD':<4} | ")
        print("-"*60)
        while current:
            GD=current.goalsFor-current.goalsAgainst
            print(f"| {current.name:<14} | {current.points:<6} | {current.wins:<4} | {current.draws:<5} | {current.losses:<6} | {GD:<4} |")
            current=current.next

            
    def getTopTeams(self,n):
        teams=[]
        current=self.head
        while current:
            teams.append(current)
            current=current.next
        teams.sort(key=lambda x:(-x.points,x.goalsFor-x.goalsAgainst,-x.power))
        return teams[:n]
    
    def GetMatchesForDay(self):
        matches=[]
        teams=[]
        current=self.head
        while current:
            teams.append(current)
            current=current.next
        for i in range(len(teams)):
            for j in range(i+1,len(teams)):
                matches.append((teams[i],teams[j]))
        return matches  
    
'''           
    def __iter__(self):
        current=self.head
        while current:
            yield current
            current=current.next'''
        
'''        
class matchNode:
    
    def __init__(self,team1,team2,team1_goals,team2_goals,game_no):
        self.team1=team1
        self.team2=team2
        self.team1_goals=team1_goals
        self.team2_goals=team2_goals
        self.game_no=game_no
        self.next=None
        
class MatchedHistoryLinkedList:
    
    def __init__(self):
        self.head=None
        
    def addmatch(self,team1,team2,team1_goals,team2_goals,game_no):
        newMatch=matchNode(team1,team2,team1_goals,team2_goals,game_no)
        if not self.head:
            self.head=newMatch
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=newMatch
            
    def displayMatches(self):
        
        current=self.head
        print(f"| {'game':<6} | {'team1':<10} | {'team2':<10} | {'score':<7} |")
        print("-"*40)
        while current:
            print(f"| {current.game_no:<6} | {current.team1:<10} | {current.team2:<10} | {current.team1_goals}-{current.team2_goals:<7} |")
            current=current.next
            
class KnockoutNode:
    
    def __init__(self,team_name):
        self.team_name=team_name
        self.next=None
'''        
class KnockoutLinkedList:
    
    def __init__(self):
        self.head=None
        
    def addTeam(self,team_name):
        new_node=TeamNode(team_name,0)
        if not self.head:
            self.head=new_node
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=new_node
    
    def playMatch(self,team1,team2):
        team1_goals=random.randint(0,5)
        team2_goals=random.randint(0,5)
        while team1_goals==team2_goals:
            team1_goals=random.randint(0,5)
            team2_goals=random.randint(0,5)
        if team1_goals>team2_goals:
            winner=team1
        else:
            winner=team2
        return winner,team1_goals,team2_goals

    def size(self):
        count=0
        current=self.head
        while current:
            count+=1
            current=current.next
        return count
    
    def get_current_round_matches(self):
        matches=[]
        current=self.head
        while current and current.next:
            matches.append((current,current.next))
            current=current.next.next
        return matches
    
    def removeTeam(self,team_name):
        current=self.head
        previous=None
        while current:
            if current.name==team_name:
                if previous:
                    previous.next=current.next
                else:
                    self.head=current.next
                return 
            previous=current
            current=current.next
            
            
        
def groupMatchPlay(team1,team2):
    team1_goals=random.randint(0,team1.power)
    team2_goals=random.randint(0,team2.power)
    if team1_goals>team2_goals:
        team1.wins+=1
        team1.points+=3
        team2.losses+=1
    elif team1_goals<team2_goals:
        team2.wins+=1
        team2.points+=3
        team1.losses+=1
    else:
        team1.draws+=1
        team2.draws+=1
        team1.points+=1
        team2.points+=1
    team1.goalsFor+=team1_goals
    team1.goalsAgainst+=team2_goals
    team2.goalsFor+=team2_goals
    team2.goalsAgainst+=team1_goals
    return team1_goals,team2_goals

def SingleDayGroupMatches(groups):
    #print(groups,"hello")
    for group_name,group in groups.items():
        #print(type(group))
        matchesForDay=group.GetMatchesForDay()
        for match in matchesForDay:
            team1,team2=match
            groupMatchPlay(team1,team2)
            #group.updateAfterMatch(team1,team2)
            #matchHistory.addMatch(team1,team2)
            
def SingleDayKnockoutMatches(KnockoutList):
    matches=KnockoutList.get_current_round_matches()
    for team1,team2 in matches:
        winner,team1_goals,team2_goals=KnockoutList.playMatch(team1,team2)
        print(f"{team1.name} ({team1_goals}) vs {team2.name} ({team2_goals}) -> winner:{winner.name}")
        KnockoutList.removeTeam(team2.name)
        #team1,team2=match
        #winner=KnockoutMatchPlay(team1,team2)
        #KnockoutList.KnockoutUpdateAfterMatch(winner)
        
def UserCommands():
    while True:
        command=input("Enter S to display status or C to continue.").strip().upper()
        if command=="S":
            displayAllRankings()
        elif command=="C":
            break
        else:
            print("invalid command please enter S or C")
'''            
def displayGroupStageOutput(groups):
    for group in groups:
        print(f"group {group.name} rankings")
        group.displayrankings()

def displayKnockoutStageOutputs(KnockoutList):
    print("KnockoutStage bracket")
    KnockoutList.displaybracket()
    
def KnockoutMatchPlay(team1,team2,max_goals=5):
    while True:
        team1_goals=random.randint(0,max_goals)
        team2_goals=random.randint(0,max_goals)
        if team1_goals!=team2_goals:
            winner=team1 if team1_goals>team2_goals else team2
            return winner,(team1_goals,team2_goals)
        penality_team1=random.randint(0,5)
        penality_team2=random.randint(0,5)
        if penality_team1!=penality_team2:
            winner=team1 if penality_team1>penality_team2 else team2
            return winner,(team1_goals+penality_team1,team2_goals+penality_team2)
        
   
    def KnockoutUpdateAfterMatch(self,matchNode):
        if not self.head:
            return
        current=self.head
        previous=None
        while current:
            if current.team_name==matchNode:
                if previous:
                    previous.next=current.next
                else:
                    self.head=current.next
                return
            previous=current
            current=current.next 
'''
        
            

def main():
    teams_data=[]
    try:
        teams_data=load_teams("teams.csv")
    except FileNotFoundError:
        print("error teams.csv file not found")
        return
    groups={chr(65+i):GroupLinkedList() for i in range(8)}
    #print(groups)
    for team in teams_data:
        group_name=team["group"]
        groups[group_name].insert(team["name"],team["power"])
    print("intial group rankings")
    #print(groups,"hello")
    #print(groups.items,"hii")
    for group_name,group_list in groups.items():
        print(f"group {group_name}")
        group_list.display_rankings()
        print()
    print("running group stage matches")
    SingleDayGroupMatches(groups)
    #for group_name,group_list in groups.items():
        #SingleDayGroupMatches(group_list)
    print("updated group rankings after group stage")
    for group_name,group_list in groups.items():
        print(f"group {group_name}")
        group_list.display_rankings()
        print()
    print("preparing for Knock out rounds")
    KnockoutList=KnockoutLinkedList()
    for group_list in groups.values():
        top_teams=group_list.getTopTeams(2)
        for team in top_teams:
            #KnockoutList.insert(team["name"],team["power"])
            KnockoutList.addTeam(team.name)
    print("running knock out stage matches")
    while KnockoutList.size()>1:
        SingleDayKnockoutMatches(KnockoutList)
    print("fianl results")
    print(f"champion:{KnockoutList.head.name}")
    #print(f"runnerup:{KnockoutList.head.next.name}")
    while True:
        command=input("Enter S to display status or C to continue.").strip().upper()
        if command=="S":
            print("final group rankings")
            for group_name,group_list in groups.items():
                print(f"group {group_name}")
                group_list.display_rankings()
                print()
        elif command=="C":
            print("simulation compelete")
            break
        else:
            print("invalid command please enter S or C") 

if __name__=="__main__":
    main()

        
            
        
            
        
        
            
            
            
        
        
            
            
            
        
                    
                    
            
    
        
    
    
            
            
        
            
        
    
    

def initialize_teams():
    """
    Initialize 32 unique teams with names and return them in a list.
    
    Example: ["Team A", "Team B", ..., "Team Z"]
    """
  #   TODO: Create and return a list of team names.
  
def group_stage_matches(groups, linked_lists):
    """
    Conduct the group stage matches where teams within each group play against each other.
    
    Each match should assign points to the teams and update their rankings in the linked list.
    """
#     TODO: Implement match results with random outcomes.
#     For each match, update the linked list to reflect the new rankings.
   

def promote_teams(groups, linked_lists):
    """
    Identify the top two teams from each group to move on to the knockout stage.
    
    Remove teams ranked 3rd and 4th in each group from the linked list.
    """
  #   TODO: Implement logic to promote top teams and eliminate others.
   

def knockout_stage(teams, linked_list):
    """
    Conduct the knockout stage where teams are paired randomly.
    
    The losing team is removed from the linked list, and the winner moves on to the next round.
    """
   #  TODO: Implement single-elimination logic until one team remains.
    

def knockout_competition(teams):
# Function to simulate knockout matches and find the champion with a fixed bracket structure
    # Define bracket for Round of 16 based on group winners and runners-up
    
    # Round of 16
  
    # Quarterfinals
  
    # Semifinals
  
    # Final
  
    return champion

def main():
    """
    Run the World Cup simulation.
    
    This function should:
    1. Initialize the teams and groups.
    2. Conduct the group stage, updating rankings with each match.
    3. Promote teams and set up the knockout stage.
    4. Continue until a winner is determined.
    """
    #Initialize teams and linked list for rankings
   
    # TODO: Assign teams to groups and start group stage
    
    #TODO: Promote teams to knockout stage
    
    #Initialize new linked list for knockout stage
    
     #TODO: Run knockout stage and determine the winner
   
if __name__ == "__main__":
    main()
