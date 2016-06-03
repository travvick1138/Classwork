#setup

NFL = {
    'AFC': {
        'East': ['Buffalo Bills', 'Miami Dolphins', 'New England Patriots', 'New York Jets'],
        'North': ['Baltimore Ravens', 'Cincinnati Bengals', 'Cleveland Browns', 'Pittsburgh Steeler'],
        'South': ['Houston Texans', 'Indianapolis Colts', 'Jacksonville Jaguars', 'Tennessee Titans'],
        'West': ['Denver Broncos', 'Kansas City Chiefs', 'Oakland Raiders', 'San Diego Chargers']},
    'NFC': {
        'East': ['Dallas Cowboys', 'New York Giants', 'Philadelphia Eagles', 'Washington Redskins'],
        'North': ['Chicago Bears', 'Detroit Lions', 'Green Bay Packers', 'Minnesota Vikings'],
        'South': ['Atlanta Falcons', 'Carolina Panthers', 'New Orleans Saints', 'Tampa Bay Buccaneers'],
        'West': ['Arizona Cardinals', 'Los Angeles Rams', 'San Francisco 49ers', 'Seattle Seahawks']}
}


def give_me_team_list(teams, conference, division):
    """Returns a list of teams in the selected Conference and division"""

    return teams[conference][division]


def give_me_a_conference_and_division_from_team(teams, team):
    """Returns the conference and division for a selected team """

    for conference in teams.keys():
        for division in teams[conference].keys():
            if team in teams[conference][division]:
                return conference, division



#input


def main(teams):

    user_input = input("Enter the name of either a conference (AFC or NFC), or a team(Seattle Seahawks): ")

    if user_input in teams.keys():
        conference = user_input
        division = input("Please provide a division (North, South, East, West)")
        teams = give_me_team_list(teams, conference, division)

        if teams is None:
            main(teams)
        else:
            print("Here is a list of teams from the {conference} {division}: {teams}.".format(
                conference=conference,
                division=division,
                teams=', '.join(teams)
            ))
    else:
        team = user_input
        conference, division = give_me_a_conference_and_division_from_team(teams, team)

        print("Your {team} is in the {conference} {division}".format(
            team=team,
            conference=conference,
            division=division
        ))




main(NFL)

#transform


#output



