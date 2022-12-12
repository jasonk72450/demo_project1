DATA_IN = 'scores.txt'


def main():
    """
    Read a text file and store the data in a dictionary.
    :return: None
    """

    # create empty dictionary
    players = {}

    with open(DATA_IN, 'rt') as file_in:
        for line in file_in:
            tokens = line.split()
            name = tokens[0]
            score = float(tokens[1])
            players[name] = score
        print(players)
        for player, score in players.items():
            print(player, score)


if __name__ == '__main__':
    main()
