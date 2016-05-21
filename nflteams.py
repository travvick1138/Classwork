def get_team_names_from_conference_and_division(conference, division):
    """Return a list of team names when given conference and division

    >>>get_team_names_from_conference_and_division(AFC,West)
    'Your teams are Denver Broncos, Kansas City Chiefs, Oakland Raiders, San Diego Chargers'

    >>>get_team_names_from_conference_and_division(NFC,East)
    'Your teams are Dallas Cowboys, New York Giants, Philadelphia Eagles, Washington Redskins'
    """
    list_of_teams = NFL[conference][division]
    print(', '.join(list_of_teams))


def get_conference_and_division_from_team_name(teams):
    """Return the conference and division from defined team name

    >>>get_conference_and_division_from_team_name(Seattle Seahawks)
    'Your Conference and Division is NFC West'

    >>>get_conference_and_division_from_team_name(Houston Texans)
    'Your Conference and Division is AFC South'
    """



def main(teams):
    input_user = input("Enter the name of the team, division, or Conference. ")
    if input_user in teams.keys():
        division = input("Please enter a division. ")
        get_team_names_from_conference_and_division(input_user, division)






NFL = {
    'AFC': {
        'EAST': ['Buffalo Bills', 'Miami Dolphins', 'New England Patriots', 'New York Jets'],
        'NORTH': ['Baltimore Ravens', 'Cincinnati Bengals', 'Cleveland Browns', 'Pittsburgh Steeler'],
        'SOUTH': ['Houston Texans', 'Indianapolis Colts', 'Jacksonville Jaguars', 'Tennessee Titans'],
        'WEST': ['Denver Broncos', 'Kansas City Chiefs', 'Oakland Raiders', 'San Diego Chargers']},
    'NFC': {
        'EAST': ['Dallas Cowboys', 'Miami Dolphins', 'New England Patriots', 'New York Jets'],
        'NORTH': ['Baltimore Ravens', 'Cincinnati Bengals', 'Cleveland Browns', 'Pittsburgh Steeler'],
        'SOUTH': ['Houston Texans', 'Indianapolis Colts', 'Jacksonville Jaguars', 'Tennessee Titans'],
        'WEST': ['Denver Broncos', 'Kansas City Chiefs', 'Oakland Raiders', 'San Diego Chargers']}
            }

main(NFL)

# if __name__ == '__main__':
#     import doctest
#
#     doctest.testmod()
#     prompt_user()
