# Advent of Code Day 2
def is_game_possible(game_data, bag_capacity):
    for set_data in game_data:
        for color, number in set_data.items():
            if number > bag_capacity[color]:
                return False
    return True

def analyze_games(input_text):
    games = input_text.strip().split('\n')
    bag_capacity = {'red': 12, 'green': 13, 'blue': 14}
    possible_games_sum = 0

    for game in games:
        if ': ' not in game:
            continue  

        game_id, sets = game.split(': ')
        game_id = int(game_id.split(' ')[1])
        set_data = [s.split(', ') for s in sets.split('; ')]
        set_data = [{color: int(num) for num, color in (item.split(' ') for item in set)} for set in set_data]

        if is_game_possible(set_data, bag_capacity):
            possible_games_sum += game_id

    return possible_games_sum

possible_games_sum = analyze_games(input_text)
print(f"Sum of IDs of possible games: {possible_games_sum}")

###### PART B ######
def calculate_power_of_minimum_sets(games):
    def parse_sets(sets):
        return [{color: int(num) for num, color in (item.split(' ') for item in set.split(', '))} for set in sets]

    def calculate_minimum_set(game_sets):
        min_set = {'red': 0, 'green': 0, 'blue': 0}
        for set in game_sets:
            for color, number in set.items():
                min_set[color] = max(min_set[color], number)
        return min_set

    def power_of_set(set):
        return set['red'] * set['green'] * set['blue']

    total_power = 0

    for game in games.strip().split('\n'):
        if ': ' not in game:
            continue 

        _, sets = game.split(': ')
        game_sets = parse_sets(sets.split('; '))
        min_set = calculate_minimum_set(game_sets)
        total_power += power_of_set(min_set)

    return total_power
  total_power = calculate_power_of_minimum_sets(input_text)
