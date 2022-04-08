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
                game_data_matrix[i][j] = row[left_index:right_index-1]
                i += 1
        right_index = index
        game_data_matrix[i][j] = row[left_index:right_index]
    return game_data_matrix
matrix_game_data = open_game_data_csv(game_data_row = 6, game_data_column = 6)
for i in range(1, 6):
    for j in range(6):
        print(matrix_game_data[i][j], end=" | ")
    print()

def open_user_data_csv(user_data_row, user_data_column):
    user_data_matrix = [["" for _ in range(user_data_column)] for _ in range(user_data_row)]
    user_data_csv = open("user.csv", "r")
    user_data = user_data_csv.readlines()
    i = 0
    for row in user_data:
        j = 0
        index = 0
        left_index = 0
        for char in row:
            if char == ";":
                right_index = index
                user_data_matrix[i][j] = row[left_index:right_index]
                j += 1
                left_index = index + 1
            index += 1
            if char == "\n":
                right_index = index
                user_data_matrix[i][j] = row[left_index:right_index-1]
                i += 1
        right_index = index
        user_data_matrix[i][j] = row[left_index:right_index]
    return user_data_matrix
# matrix_user_data = open_user_data_csv(user_data_row = 5, user_data_column = 3)
# for row in matrix_user_data:
#    print(*row)

# F02
def register():
    matrix_user_data = open_user_data_csv(5, 3)
    input_name = input("Masukan nama: ")
    input_username = input("Masukan username: ")
    input_password = input("Masukan password: ")

    isAvailable = True
    for i in range(5):
        if input_username == matrix_user_data[i][1]:
            isAvailable = False
            break
    
    if isAvailable:
        print("Username", input_username, 'telah berhasil register ke dalam "Binomo".')
    else:
        print("Username", input_username, 'sudah terpakai, silakan menggunakan username lain.')
# register()

# F03
def login():
    matrix_user_data = open_user_data_csv(5, 3)
    for row in matrix_user_data:
        print(*row)
    input_username = input("Masukan username: ")
    input_password = input("Masukan password: ")
    

    isRegistered = False
    for i in range(5):
        if input_username == matrix_user_data[i][1] and input_password == matrix_user_data[i][2]:
            isRegistered = True
            break
        print(isRegistered)
    if isRegistered:
        print("Halo " + str(matrix_user_data[i][0]) + '! Selamat datang di "Binomo".')
    else:
        print("Password atau username salah atau tidak ditemukan.")
# login()

# f04
# def tambah_game()
#     game_name = input("masukan nama game: ")
#     game_kategori = input