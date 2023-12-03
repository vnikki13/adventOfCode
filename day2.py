import regex as re

def textToObject(text_file):
    games = []

    file = text_file.readlines()
    for line in file:
        game_id = re.search('\d+', line)
        results = re.findall('\d+ \w+', line)
        if game_id is not None and results is not None:
            values = []
            for result in results:
                value = re.search('\d+', result)
                color = re.search('[a-z]+', result)
                if value is not None and color is not None:
                    values.append({color.group(0): int(value.group(0))})
            games.append({int(game_id.group(0)): values})
    return games

def find_games_with_possible_colors(games):
    possible_colors = {
        'red': 12,
        'green': 13,
        'blue': 14
    }

    possible_games = []

    for game in games:
        game_id = list(game)[0]
        sets = game[game_id]
        print(f"\nnew game with id {game_id}")
        for set in sets:
            colors = list(set)
            for color in colors:
                if possible_colors[color] < set[color]:
                    print(f'Exited because {color} has a value of {set[color]}')
                    break
            else:
                continue
            break
        else:
            possible_games.append(game_id)
            continue
    
    print(sum(possible_games))

def find_games_with_fewest_possible_colors(games):
    min_possible_values = []

    for game in games:
        game_id = list(game)[0]
        sets = game[game_id]
        print(f"\nnew game with id {game_id}")

        min_blue = 0
        min_green = 0
        min_red = 0
        for set in sets:
            color = list(set)[0]
            value = set[color]
            if color == 'blue':
                if min_blue < value: min_blue = value
            elif color == 'green':
                if min_green < value: min_green = value
            elif color == 'red':
                if min_red < value: min_red = value
        min_possible_values.append(min_blue * min_green * min_red)
        print(sum(min_possible_values))

with open('input.txt') as text_file:
    games = textToObject(text_file)

    # Function for puzzle one
    find_games_with_possible_colors(games)

    # Function for puzzle two
    find_games_with_fewest_possible_colors(games)
