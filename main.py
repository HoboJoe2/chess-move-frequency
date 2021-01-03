import os
import matplotlib.pyplot as plt
import time

dirpath = os.path.dirname(__file__)
pgn_filepath = os.path.join(dirpath, "pgn_file.pgn")
moves_filepath = os.path.join(dirpath, "moves.txt")
data_filepath = os.path.join(dirpath, "data.txt")
images_filepath = os.path.join(dirpath, "images")


def create_graphs(all_dicts):
    print("Creating images...")
    for key, value in all_dicts.items():

        moves = list(value.keys())
        scores = list(value.values())

        plt.figure(figsize=(20, 10))
        plt.title(key)
        plt.bar(moves[:20], scores[:20])
        plt.savefig(f"{images_filepath}/{key}")

    return


def create_data_file(all_dicts):
    print("Writing dictionary contents to data.txt...")
    with open(data_filepath, "w") as f:
        for dataset, dictionary in all_dicts.items():
            print(f"""
----- {dataset} -----
            """, file=f)

            for move, score in dictionary.items():
                print(f"{move} > {score}", file=f)
    return


def create_moves_file():
    with open(pgn_filepath, "r") as f:
        print("Reading moves from pgn file...")
        lines = f.readlines()

    with open(moves_filepath, "w") as f:
        print("Writing moves to moves.txt...")
        for line in lines:
            if "[" not in line.strip("\n") and line.strip("\n") != "":
                for move in line.strip("\n").split(" "):
                    invalid_move = False
                    for symbol in [".", "0-1", "1-0", "1/2-1/2", " "]:
                        # not actual moves
                        if symbol in move:
                            invalid_move = True
                    if invalid_move is False:
                        f.write(f"{move}\n")
    return


def create_move_dict(filepath):
    move_dict = {}

    with open(filepath, "r") as f:
        print("Reading lines of file...")
        lines = f.readlines()
        print("Creating main dictionary...")
        for move in lines:
            move = move.strip("\n")
            if move not in move_dict:
                move_dict[move] = 1
            else:
                move_dict[move] += 1

    move_dict_sorted = dict(sorted(move_dict.items(),
                                   key=lambda kv: kv[1], reverse=True))
    return move_dict_sorted


def _match_symbol_to_movetype(symbol, key, movetype,
                              data_dictionary, move_dictionary):
    if symbol in key:
        data_dictionary[f"{movetype}"][key] = move_dictionary[key]
    else:
        pass
    return


def create_other_dicts(move_dict):
    print("Creating other dictionaries...")
    peice_initials = ["R", "N", "B", "Q", "K", "-"]  # "-" is for castling

    other_dicts = {
                   "Peice Moves": {},
                   "Rook Moves": {},
                   "Knight Moves": {},
                   "Bishop Moves": {},
                   "Queen Moves": {},
                   "King Moves": {},
                   "Pawn Moves": {},
                   "Checks": {},
                   "Checkmates": {},
                   "Captures": {},
                   "Non-captures": {}
    }

    for key in move_dict:  # key will be a move string like Ke2 or bxa8=Q#
        peice_move = False
        capture = False

        for letter in peice_initials:
            if letter in key:
                other_dicts["Peice Moves"][key] = move_dict[key]
                peice_move = True

        if peice_move is False:
            other_dicts["Pawn Moves"][key] = move_dict[key]

        if "x" in key:
            other_dicts["Captures"][key] = move_dict[key]
            capture = True

        if capture is False:
            other_dicts["Non-captures"][key] = move_dict[key]

        _match_symbol_to_movetype("R", key, "Rook Moves",
                                  other_dicts, move_dict)
        _match_symbol_to_movetype("N", key, "Knight Moves",
                                  other_dicts, move_dict)
        _match_symbol_to_movetype("B", key, "Bishop Moves",
                                  other_dicts, move_dict)
        _match_symbol_to_movetype("Q", key, "Queen Moves",
                                  other_dicts, move_dict)
        _match_symbol_to_movetype("K", key, "King Moves",
                                  other_dicts, move_dict)
        _match_symbol_to_movetype("+", key, "Checks",
                                  other_dicts, move_dict)
        _match_symbol_to_movetype("#", key, "Checkmates",
                                  other_dicts, move_dict)

    return other_dicts


if __name__ == "__main__":

    create_moves_file()
    moves_dict = create_move_dict(moves_filepath)
    other_dicts = create_other_dicts(moves_dict)

    all_dicts = {}  # merge moves_dict and other_dicts
    all_dicts["All Moves"] = moves_dict
    for key, value in other_dicts.items():
        all_dicts[key] = value

    create_data_file(all_dicts)

    create_graphs(all_dicts)

    print("Done, thank you for using this program!")
    time.sleep(1000)
