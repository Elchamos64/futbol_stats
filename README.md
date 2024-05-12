# Overview

I wrote a pryhton program that uses SQLite3 to create and manage databases about futbol(soccer). The code is very simple. It allows user to input information about a team in the spanish league (la liga) and displays the information back to the user to see the standings of the teams in the league and stats like: Points, position, Goals scored and more.

I love watching futbol and I wanted to be able to see the stats of my favorite team more easily and in an easy to read format. That's why I created this app.

[Video walkthrough](https://youtu.be/OWhXth0sLQI)

# Relational Database

For this program I used `SQL`. I used `sqlite3` module to write the code using `Python`.

The table is stucture by team. Each team has a team name, matches played, goals scored, goals againts, goal diference and points.

# Development Environment

I used `python` to help me write the code structure with the functions and the variables. `Sqilte3` to help me build the database and the structure of the table. The `tabulate` module to help me display the data as a grid, so that it's easier to read.

I used VScode as my code editor, python as my programing language and the folowig modules:
- Sqlite3
- Tabulate

# Useful Websites

Below a list of websites that I used to learned how to use these tool. I also used some AI to help me with the syntax of the code. 

- [Sqlite](https://www.sqlitetutorial.net/)
- [sqlite3-python](https://docs.python.org/3/library/sqlite3.html)
- [Tabulate how-to](https://pypi.org/project/tabulate/)

# Future Work

The downside if this app is that it requires user input to keep the information up to date. Here is a list of future improvements required for the app to be more efficient and more useful:

- Use an API to fetch the data and keep it up to date.
- More team stats, like players, titles and more.
- Line up feature. It should display the line up of the team while the game is live.
- Other leagues, expand the app so it support more countries and more leagues.
