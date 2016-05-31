def get_team_names_from_conference_and_division(teams, conference, division):
    """Return a list of team names when given conference and division

    >>>get_team_names_from_conference_and_division(AFC,West)
    'Your teams are Denver Broncos, Kansas City Chiefs, Oakland Raiders, San Diego Chargers'

    >>>get_team_names_from_conference_and_division(NFC,East)
    'Your teams are Dallas Cowboys, New York Giants, Philadelphia Eagles, Washington Redskins'
    """
    try:
        return teams[conference][division]
    except KeyError:
        return None




def get_conference_and_division_from_team_name(teams, team_name):
    """Return the conference and division from defined team name

    >>>get_conference_and_division_from_team_name(Seattle Seahawks)
    'Your Conference and Division is NFC West'

    >>>get_conference_and_division_from_team_name(Houston Texans)
    'Your Conference and Division is AFC South'
    """
    for conference in teams.keys():
        for division in teams[conference].keys():
            try:
                if teams[conference][division].index(team_name) > -1:
                    return conference, division
            except ValueError:
                continue

    return None, None



def main(teams):
    input_user = input("Enter the name of the team, division, or Conference. ")
    if input_user in teams.keys():
        conference = input_user
        division = input("Please enter a division. ")
        get_team_names_from_conference_and_division(teams, conference, division)

    elif input_user in teams['AFC'].keys():
        division = input_user
        conference = input("Please enter a conference. ")
        get_team_names_from_conference_and_division(teams, conference, division)

        if teams is None:
            main(teams)
        else:
            list_of_teams = teams[conference][division]
            print('The Teams in your {conference) and {division] are:\n {teams}'.format(
                conference=conference,
                division=division,
                teams='\n '.join(list_of_teams)
            ))
    else:
        team_name = input_user
        conference, division = get_conference_and_division_from_team_name(teams, team_name)

        if conference is None:
            main(teams)
        elif division is None:
            main(teams)
        else:
            print('Your {team_name} is in {conference] and {division}.'.format(
                team_name=teamname,
                conference=conference,
                division=division
            ))








NFL = {
    'AFC': {
        'East': ['Buffalo Bills', 'Miami Dolphins', 'New England Patriots', 'New York Jets'],
        'North': ['Baltimore Ravens', 'Cincinnati Bengals', 'Cleveland Browns', 'Pittsburgh Steeler'],
        'South': ['Houston Texans', 'Indianapolis Colts', 'Jacksonville Jaguars', 'Tennessee Titans'],
        'West': ['Denver Broncos', 'Kansas City Chiefs', 'Oakland Raiders', 'San Diego Chargers']},
    'NFC': {
        'East': ['Dallas Cowboys', 'Miami Dolphins', 'New England Patriots', 'New York Jets'],
        'North': ['Chicago Bears', 'Detroit Lions', 'Green Bay Packers', 'Minnesota Vikings'],
        'South': ['Atlanta Falcons', 'Carolina Panthers', 'New Orleans Saints', 'Tampa Bay Buccaneers'],
        'West': ['Arizona Cardinals', 'Los Angeles Rams', 'San Francisco 49ers', 'Seattle Seahawks']}
            }

main(NFL)

# if __name__ == '__main__':
#     import doctest
#
#     doctest.testmod()
#     prompt_user()
