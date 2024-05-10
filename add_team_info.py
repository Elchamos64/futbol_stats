import sqlite3

# Function to create the database table if it doesn't exist
def create_table():
    conn = sqlite3.connect('soccer_teams.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS teams
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                 name TEXT NOT NULL, 
                 matches_played INTEGER NOT NULL,
                 wins INTEGER NOT NULL,
                 draws INTEGER NOT NULL,
                 losses INTEGER NOT NULL,
                 goals_for INTEGER NOT NULL,
                 goals_against INTEGER NOT NULL,
                 goal_difference INTEGER NOT NULL,
                 points INTEGER NOT NULL)''')
    conn.commit()
    conn.close()

# Function to add a new team to the database
def add_team(name, matches_played, wins, draws, losses, goals_for, goals_against, goal_difference, points):
    conn = sqlite3.connect('soccer_teams.db')
    c = conn.cursor()
    c.execute('''INSERT INTO teams (name, matches_played, wins, draws, losses, goals_for, goals_against, goal_difference, points) 
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', (name, matches_played, wins, draws, losses, goals_for, goals_against, goal_difference, points))
    conn.commit()
    conn.close()

# Main function to interact with the user
def main():
    create_table()
    
    while True:
        print("\n1. Add a new team")
        print("2. Quit")
        
        choice = input("Enter your choice (1/2): ")
        
        if choice == '1':
            name = input("Enter team name: ")
            matches_played = input("Enter MP: ")
            wins = int(input("Enter W: "))
            draws = int(input("Enter D: "))
            losses = int(input("Enter L: "))
            goals_for = int(input("Enter GF: "))
            goals_against = int(input("Enter GA: "))
            goal_difference = int(goals_for - goals_against)
            points = int((wins * 3) + draws)
            add_team(name, matches_played, wins, draws, losses, goals_for, goals_against, goal_difference, points)
            print("Team added successfully!")
        
        elif choice == '2':
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
