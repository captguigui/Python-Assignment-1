# inspired by https://exercism.io/tracks/javascript/exercises/etl/solutions/91f99a3cca9548cebe5975d7ebca6a85


old_point_structure = {
  1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
  2: ['D', 'G'],
  3: ['B', 'C', 'M', 'P'],
  4: ['F', 'H', 'V', 'W', 'Y'],
  5: ['K'],
  8: ['J', 'X'],
  10: ['Q', 'Z']
}

def old_scrabble_scorer(user_word):
    word = user_word.upper()
    letterPoints = ""

    for char in word:

        for point_value in old_point_structure:

            if char in old_point_structure[point_value]:
                letterPoints += 'Points for {char}: {point_value}\n'.format(char = char, point_value = point_value)

    return letterPoints

# your job is to finish writing these functions and variables that we've named
# don't change the names or your program won't work as expected.

def initial_prompt():
   print("Let's play some Scrabble!\n")

   user_input = input("Enter a word to score: ")

   return user_input

def simple_scorer(word):
    score = 0
    for char in word.lower():
        score += 1

    return score

def vowel_bonus_scorer(word):
    vowels = 'aeiou'
    score = 0
    for char in word.lower():
        if char in vowels:
            score += 3
        else:
            score += 1

    return score

def scrabble_scorer(word):
    score = 0
    for letter in word.lower():
        if letter in new_point_structure:
            score += new_point_structure[letter]

    return score

simple_scorer_dict = {
    'name' : 'Simple Score',
    'description' : 'Each letter is worth 1 point',
    'scoring_function' : simple_scorer
}

vowel_bonus_scorer_dict = {
    'name' : 'Bonus Vowels',
    'description' : 'Gives 3 points per vowel and 1 point per consonants',
    'scoring_function' : vowel_bonus_scorer
}

old_scrabble_scorer_dict = {
    'name' : 'Scrabble',
    'description' : 'The traditional scoring algorithm',
    'scoring_function' : old_scrabble_scorer
}

scoring_algorithms = (
    simple_scorer_dict,
    vowel_bonus_scorer_dict,
    old_scrabble_scorer_dict
    )

def scorer_prompt():
    for index, algorithm in enumerate(scoring_algorithms):
        print(f'{index} - {algorithm["name"]}: {algorithm["description"]}')
    user_select = int(input('Enter 0, 1, or 2: '))
    scoring_dict = scoring_algorithms[user_select]

    return scoring_dict

def transform(given_dict):
    new_dict = {}
    for (key, value) in given_dict.items():
        for letter in value:
            new_dict[letter.lower()] = key

    return new_dict

new_point_structure = transform(old_point_structure)    

def run_program():
    word = initial_prompt()
    scoring_dict = scorer_prompt()
    score = scoring_dict['scoring_function'](word)
    print(score)
