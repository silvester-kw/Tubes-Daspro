game_data_row = 4
game_data_column = 6
def open_game_data_csv(game_data_row, game_data_column):
    game_data_matrix = [["" for _ in range(game_data_column)] for _ in range(game_data_row)]
    game_data_csv = open("game.csv", "r")
    game_data = game_data_csv.readlines()
    for i in range(game_data_row):
        for row in game_data:
            j = 0
            index = 0
            left_index = 0
            for char in row:
                if char == ";":
                    right_index = index
                    game_data_matrix[i][j] = row[left_index:right_index]
                    j += 1
                    left_index = index + 1
                index += 1
    for row in game_data_matrix:
        print(*row)
    return game_data_matrix
open_game_data_csv(game_data_row, game_data_column)