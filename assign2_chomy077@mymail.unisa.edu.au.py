#
# File: assign2_chomy077@mymail.unisa.edu.au.py
# Author: Mridul Chopra
# Email Id: chomy077@mymail.unisa.edu.au
# Description: Assignment 2 – A python script which reads and rights itno a file. and plays a game of blackjacks(dice version)
# This is my own work as defined by the University's
# Academic Misconduct policy.Description: Blackjack game assign2
#

import blackjack



# Function read_file() - reads the file and stores the value in a list
def read_file(filename):
    # player_list: List to store player information
    player_list = []
    index = 0
    
    infile = open(filename, "r")

    # Read first line of file.
    line = infile.readline()

    # While not end of file reached i.e. empty string not returned from readline method.
    while line != '':

        # Read name
        name = line.strip('\n')

        # Read in next line
        line = infile.readline()
        
        # Split line into games played, no won, no lost, etc
        info_list = line.split()
        games_played = int(info_list[0])
        no_won = int(info_list[1])
        no_lost = int(info_list[2])
        no_drawn = int(info_list[3])
        chips = int(info_list[4])
        total_score = int(info_list[5])
        
        # Create new player list with player info
        new_player = [name, games_played, no_won, no_lost, no_drawn, chips, total_score]
        
        # Add new player to player_list list
        player_list.append(new_player)
        
        # Read next line of file.
        line = infile.readline()
    
    return player_list


# Function display_players() - Display a list of players
def display_players(player_list): 
    print("===========================================================")
    print("-                    Player Summary                       -")
    print("===========================================================")
    print("-                                P  W  L  D  Chips Score  -")
    print("-----------------------------------------------------------")
    for lst in player_list:
        name = lst[0]  # name: Player's name
        games_played = lst[1] # games_played: Number of games played by the player
        no_won = lst[2]  # no_won: Number of games won by the player
        no_lost = lst[3] # no_lost: Number of games lost by the player
        no_drawn = lst[4]  # no_drawn: Number of games drawn by the player
        chips = lst[5] # chips: Number of chips the player has
        total_score = lst[6] # total_score: Total score of the player
        print("-",format(name, "<29"),format(games_played, "^3"),format(no_won, "^1"),format(no_lost, "^3"),format(no_drawn, "^2"),format(chips, "^6"),format(total_score, "^5"),"-")
        print("-----------------------------------------------------------")
    
    print("===========================================================")


# Function write_to_file() - writes the player list to the file
def write_to_file(filename,player_list):
    
    outfile = open(filename,"w") 

    # for loop to run in player list and gather each info list as lst
    for lst in player_list:
        #writes the name and a \n to change the line
        outfile.write(lst[0]+"\n")
        #second loop running in range 1 to 6 so that i can get 1ndex of each 
        for i in range(1,6):
            outfile.write(str(lst[i])+" ")
        outfile.write("\n")
    outfile.close()


# Function find_players() - finds a player by name and returns its index value in the player list and if player not find returns -1 as index
def find_players(player_list,name):
    found = -1 # total_score: Total score of the player if cant it would be -1
    for i in range(len(player_list)):
        if player_list[i][0] == name:
            found = i
    return found


# Function buy_player_chips() - allows a player to buy chips and if player not found responds with a error message
def buy_player_chips(player_list, name):
    player_pos = find_players(player_list,name)  #player_pos: stores the index value of the player, find_player() function- returns index of player and -1 if player not found
    if player_pos == -1:
        print("\n")
        print(name,"not Found in player list")
    else:
        print("\n")
        print(name,"is currently at", player_list[player_pos][5], "chips")
        print("\n")
        usr = int(input("How many chips would you like to buy? ")) #usr: stores
        while usr>100 or usr<1:
            print("You may only buy 1-100 chips at a time!")
            print("\n")
            usr = int(input("How many chips would you like to buy? "))
        player_list[player_pos][5] += usr
        print("\n")
        print("Successfully updated ",name,"'s chip balance to ",player_list[player_pos][5],sep='')


# Function display_highest_chip_holder() - displays the player with the highest chips in the player list
def display_highest_chip_holder(player_list):
    max_chip = 0 # max_chip stores maximum chip balance of players
    games_played=0 # games_played stores number of games played by the player with the highest chips
    if len(player_list)!=0:
        for lst in player_list:
            if lst[5]>max_chip:
                max_chip = lst[5]
                games_played = lst[1]
                Name = lst[0] # Name stores the name of the player with the highest chips
            elif lst[5] == max_chip:
                if lst [1] < games_played:
                    max_chip = lst[5]
                    Name = lst[0]

        if max_chip == 0:
            print("Error!!, Player with a highest chip balance cannot be Found")
        else:
            print("Highest Chip Holder =>",Name,"with",max_chip,"chips")
    else:
        print("Eroor!!, No players Found!")


# Function add_player() - adds a new player to the player list
def add_player(player_list, name):
    player_pos = find_players(player_list,name)  # player_pos stores Index of the player in the player list
    if player_list[player_pos][0] == name:
        print("\n")
        print(name,"already exosts in player list.")
    else:
        games_played = 0 
        no_won = 0
        no_lost = 0
        no_drawn = 0
        chips = 100
        total_score = 0 
        new_player = [name, games_played, no_won, no_lost, no_drawn, chips, total_score]
        player_list.append(new_player)
        print("\n")
        print("Succesfully added",name,"to player list.")
    return player_list


# Function remove_player() - removes a player from the player list
def remove_player(player_list, name):
    player_pos=find_players(player_list,name)
    templst = []
    if player_pos == -1:
        print("\n")
        print(name,"not found in player list")
        for lst in player_list:
            templst.append(lst)
    else:
        if  player_list[player_pos][0] == name:
            for index in range(len(player_list)): 
                if player_list[index][0] != name:
                    templst.append(player_list[index])
            print("\n")
            print("Succesfully Removed",name,"From player list.")
    return templst        
        
# Function play_blackjack_games() - playsa game of blackjack(dice version) for a player
def play_blackjack_games(player_list, player_pos):  
    player_pos=find_players(player_list,name)
    if player_pos == -1:
        print("\n")
        print(name,"not found in player list")
    else:  
        usr = "y"  # usr stores user's choice for playing again or not
        while usr.upper() == "Y":
            player_list[player_pos][1] +=1
            chips = player_list[player_pos][5] 
            game_result,chips= blackjack.play_one_game(chips)
            player_list[player_pos][5] = chips
            if game_result ==3:
                player_list[player_pos][2]+=1  
                player_list[player_pos][6]+=game_result  
            elif game_result ==1:
                player_list[player_pos][4]+=1  
                player_list[player_pos][6]+=game_result
            else:
                player_list[player_pos][3]+=1
            
            usr = input("Play again?[y/n]: ")


# Function sort_by_chips() - sorts players by their chip balance and returns a copy list
def sort_by_chips (player_list):
    copy_list=[]  # copy_list stores copy of the player list for sorting
    for lst in player_list: # using for lopp to copy the list from player list to copy list
        copy_list.append(lst)
    for index in range(len(copy_list)):
        for index2 in range(len(copy_list)-1):
            if copy_list[index2][5]<copy_list[index2+1][5]:
                temp = copy_list[index2]
                copy_list[index2] = copy_list[index2+1]
                copy_list[index2+1] = temp
            elif copy_list[index2][5]==copy_list[index2+1][5]:
                print(copy_list[index2],"before swap")
                if copy_list[index2][1] > copy_list[index2+1][1]:
                    temp = copy_list[index2]
                    copy_list[index2] = copy_list[index2+1]
                    copy_list[index2+1] = temp
                    print(copy_list[index2],"apfter swap")


    return copy_list


###list to store player information
player_list = []

# Read player information from file and store in player_list
player_list = read_file("players.txt")


# Display Details
print(format("File","<10"),": assign2_chomy077@mymail.unisa.edu.au.py")
print(format("Author","<10"),": Mridul Chopra")
print(format("Stud ID","<10"),": 110430082")
print(format("Email Id","<10"),": chomy077@mymail.unisa.edu.au")
print("This is my own work as defined by the")
print("University's Academic Misconduct policy.")
print("\n")



### Interactive Mode

#Prompt user for initial choice
print("Please enter choice")
usr = input("[list, buy, search, high, add, remove, play, chips, quit]: ")
#Loop until user chooses to quit
while usr.upper() !="QUIT":
    print("\n")

    #If user chooses to list players
    if usr.upper() == "LIST":
        display_players(player_list)

     #If user chooses to buy chips
    elif usr.upper() == "BUY":
        #Prompt for player's name
        name = input("Please enter name: ")

         #Buy chips for the specified player
        buy_player_chips(player_list,name)
    
    #If user chooses to search for a player   
    elif usr.upper() == "SEARCH":
        # Prompt for player's nam
        name = input("Please enter name: ")
        
         #Find the player's position in the list
        player_pos = find_players(player_list,name) #findplayer() returns index of player and -1 if player not found
        if player_pos == -1:
            #Find the player's position in the list
            print("\n")
            print(name,"is not found in player list")
        else:
            #If player found, print their stats
            print("\n")
            print(name,"stats:")
            print("\n")
            print(" P  W  L  D  Score")
            games_played = player_list[player_pos][1]
            no_won = player_list[player_pos][2]
            no_lost = player_list[player_pos][3]
            no_drawn = player_list[player_pos][4]
            chips = player_list[player_pos][5]
            total_score = player_list[player_pos][6]
            print(format(games_played, "^3"),format(no_won, "^1"),format(no_lost, "^3"),format(no_drawn, "^2"),format(total_score, "^5"))
            print("\n")
            print("Chips: ",chips)
    #If user chooses to display the highest chip holder
    elif usr.upper()  == "HIGH":
        display_highest_chip_holder(player_list)

    #If user chooses to add a playe
    elif usr.upper() == "ADD":
        #Prompt for player's name
        name = name = input("Please enter name: ")
        #Add the player to the list
        add_player(player_list,name)
    
    #If user chooses to remove a player
    elif usr.upper() == "REMOVE":
        #Prompt for player's name
        name = input("Please enter name: ")

        #Remove the player from the list
        player_list=remove_player(player_list,name)
    #If user chooses to play a blackjack game
    elif usr.upper()=="PLAY":
        #Prompt for player's name
        name = name = input("Please enter name: ")
        #Find the player's position in the list
        player_pos=find_players(player_list,name)
        #Play blackjack game for the specified player
        play_blackjack_games(player_list,player_pos)

    #If user chooses to display players sorted by chips
    elif usr.upper()=="CHIPS":
         #Display players sorted by chip balance
        display_players(sort_by_chips(player_list))
    #If user enters an invalid command
    else:
        print("Not a valid command - please try again")
    
    
    print("\n")

    #Prompt user for the next choice
    print("Please enter choice")
    usr = input("[list, buy, search, high, add, remove, play, chips, quit]: ")


write_to_file("new players.txt",player_list) #Writing player list back to file using write_to_file() function

#End of program message
print("\n\n-- Program terminating --\n")
