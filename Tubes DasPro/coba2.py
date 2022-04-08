def open_game_data_csv(game_data_row, game_data_column):
    game_data_matrix = [["" for _ in range(game_data_column)] for _ in range(game_data_row)]
    game_data_csv = open("game.csv", "r")
    game_data = game_data_csv.readlines()
    i = 0
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
            if char == "\n":
                right_index = index
                game_data_matrix[i][j] = row[left_index:right_index]
                i += 1
        right_index = index
        game_data_matrix[i][j] = row[left_index:right_index]
    return game_data_matrix

game_data_csv = open("game.csv", "r")
game_data = game_data_csv.readlines()

game_data_csv = open("game.csv", "w")
for row in game_data:
    print(row)
    game_data_csv.write(row)
game_data_csv.write("GAME069;Python Gemink;Coding;1991;69000;999")
game_data_csv.close()