import sqlite3
from tabulate import tabulate

# Function to look up La lga standings

def la_liga_standings():
    conn = sqlite3.connect('soccer_teams.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM teams''')
    team = c.fetchall()
    conn.close()
    return team


# Function to look up team information by name
def lookup_team(name):
    conn = sqlite3.connect('soccer_teams.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM teams WHERE name=?''', (name,))
    team = c.fetchone()
    conn.close()
    return team

# Main function to interact with the user
def main():
    done = False
    while not done :
        print("1. Look up team information")
        print("2. Standing La Liga info")
        print("3. Quit")
        
        choice = input("Enter your choice (1/2/3): ")
    
        
        if choice == '1':
            name = input("Enter team name to look up: ")
            team = lookup_team(name)
            if team:
                headers = ["Name", "MP", "W", "D", "L", "GF", "GA", "GD", "Pts"]
                data = [[team[1], team[2], team[3], team[4], team[5], team[6], team[7], team[8], team[9]]]
                print("\nTeam Information:")
                print(tabulate(data, headers=headers, tablefmt="grid"))
            else:
                print("Team not found.")

        elif choice == '2':
            teams = la_liga_standings()
            print("\nTeam Information:")
            headers = ["Name", "MP", "W", "D", "L", "GF", "GA", "GD", "Pts"]
            for team in teams:
                data = [[team[1], team[2], team[3], team[4], team[5], team[6], team[7], team[8], team[9]]]
                print(tabulate(data, headers=headers, tablefmt="grid"))

        
        elif choice == '3':
            print("Exiting program.")
            done = True
        
        else:
            print("Invalid choice. Please enter 1, or 2.")

if __name__ == "__main__":
    main()

