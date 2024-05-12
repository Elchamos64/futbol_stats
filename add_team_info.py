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

# Function to delete a team from the database
def delete_team(name):
    conn = sqlite3.connect('soccer_teams.db')
    c = conn.cursor()
    c.execute('''DELETE FROM teams WHERE name = ?''', (name,))
    conn.commit()
    conn.close()

# Main function to interact with the user
def main():
    name = "Villareal"
    matches_played = 34
    wins = 12
    draws = 9
    losses = 13
    goals_for = 56
    goals_against = 58
    goal_difference = int(goals_for - goals_against)
    points = int((wins * 3) + draws)
    add_team(name, matches_played, wins, draws, losses, goals_for, goals_against, goal_difference, points)
    print(f"\n{name} added succesfully")
            

if __name__ == "__main__":
    main()
