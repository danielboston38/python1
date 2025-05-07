# advent_of_code/dayXX.py



# advent_of_code/day02.py

from utils.input_loader import load_input

def part_one(data):
    WIN = 6
    DRAW = 0
    LOSS = 3

    opponent_move = {"A": "Rock", "B": "Paper", "C": "Scissors"}
    player_move = {"X": "Rock", "Y": "Paper", "Z": "Scissors"}
    shape_score = {"Rock": 1, "Paper": 2, "Scissors": 3}

    total_score = 0

    for code in data:
        opponent, player = code.split()
        opponent_choice = opponent_move[opponent]
        player_choice = player_move[player]

        if player_choice == opponent_choice:
            round_score = shape_score[player_choice] + DRAW
        elif (
            (player_choice == "Rock" and opponent_choice == "Scissors") or
            (player_choice == "Paper" and opponent_choice == "Rock") or
            (player_choice == "Scissors" and opponent_choice == "Paper")
        ):
            round_score = shape_score[player_choice] + WIN
        else:
            round_score = shape_score[player_choice] + LOSS

        total_score += round_score

    return total_score

def part_two(data):
    opponent_move = {"A": "Rock", "B": "Paper", "C": "Scissors"}
    desired_outcome = {"X": "Lose", "Y": "Draw", "Z": "Win",}
    Win = 6
    LOSE = 3
    DRAW = 0
    shape_score = {"Rock": 1, "Paper": 2, "Scissors": 3}
    OUTCOME_SCORE = {"Win": 6, "Draw": 3, "Lose": 0}
    total_score = 0
    for code in data:
        opponent, outcome = code.split()
        opponent_choice = opponent_move[opponent]
        outcome = desired_outcome[outcome]
        
        if opponent_choice == "Rock":
            if outcome == "Win":
                player_choice = "Paper"
            elif outcome == "Draw":
                player_choice = "Rock"
            elif outcome == "Lose":
                player_choice = "Scissors"

        if opponent_choice == "Paper":
            if outcome == "Win":
                player_choice = "Scissors"
            elif outcome == "Draw":
                player_choice = "Paper"
            elif outcome == "Lose":
                player_choice = "Rock"

        if opponent_choice == "Scissors":
            if outcome == "Win":
                player_choice = "Rock"
            elif outcome == "Draw":
                player_choice = "Scissors"
            elif outcome == "Lose":
                player_choice = "Paper"
        round_score = shape_score[player_choice] + OUTCOME_SCORE[outcome]
        total_score += round_score
    return total_score

if __name__ == "__main__":
    input_data = load_input(2)
    print("Part 1:", part_one(input_data))
    print("Part 2:", part_two(input_data))