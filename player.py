from players import players
# from player.py import players list in player.py
class Player:
    def __init__(self, player):
        # self, pass var
        self.name = player['name']
        self.age = player['age']
        self.position = player['position']
        self.team = player['team']
        #self.parm = var [players key because all of players.py is here its imported]

# print(players[0]['name'])
# print key name in 1st dictionary in players list in players.py


kevin = Player(players[0])
jason = Player(players[1])
kyrie = Player(players[3])
print(kevin.name)
# player1 is equal to class Player( first players list )or index 0 players list or players[0]


# Finally, given the example list of players at the top of this module 
# (the one with many players) write a for loop that will populate an empty 
# list with Player objects from the original list of dictionaries.

# ... (class definition and large list of players here)
new_team = []
# Write your for loop here to populate the new_team variable with Player objects.




# for var from class in players list in players.py
# for every object in players list print object
# for player in players:
#     print(player)



for player in players:
    print(Player(player))
    # player is a dictionary
    # turn every dictionary into an object
#       {'name': 'Kevin Durant', 'age': 34, 'position': 'small forward', 'team': 'Brooklyn Nets'}
#       {'name': 'Jason Tatum', 'age': 24, 'position': 'small forward', 'team': 'Boston Celtics'}
#       {'name': 'Kyrie Irving', 'age': 32, 'position': 'Point Guard', 'team': 'Brooklyn Nets'}
#       {'name': 'Damian Lillard', 'age': 33, 'position': 'Point Guard', 'team': 'Portland Trailblazers'}
#       {'name': 'Joel Embiid', 'age': 32, 'position': 'Power Foward', 'team': 'Philidelphia 76ers'}
#       {'name': 'DeMar DeRozan', 'age': 32, 'position': 'Shooting Guard', 'team': 'Chicago Bulls'}
    temp_player = Player(player)
    # makes those objects one big variable
    new_team.append(temp_player)
    # adds my objects to new_team list from line 28 via variable we just made
    print(new_team)
    # prints our new list with objects from players.py!

