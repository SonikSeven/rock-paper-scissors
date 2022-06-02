from random import choice


def identification():
    player = input("Enter your name: ")
    rating = {player: 0}
    with open("rating.txt") as rating_file:
        for line in rating_file:
            name, score = line.split()
            rating[name] = int(score)
    print(f"Hello, {player}")
    return rating[player]


def set_options():
    options = tuple(input().split(","))
    print("Okay, let's start")
    return options if len(options) > 1 else ("rock", "paper", "scissors")


def main(rating, options):
    player = input()
    if player == "!exit":
        return print("Bye!")
    elif player == "!rating":
        print(f"Your rating: {rating}")
        return main(rating, options)
    elif player not in options:
        print("Invalid input")
        return main(rating, options)

    computer = choice(options)
    index = options.index(player)
    winning = options[index + 1:] + options[:index]
    winning = winning[:len(winning) // 2]
    if computer == player:
        print(f"There is a draw ({computer})")
        rating += 50
    elif computer not in winning:
        print(f"Well done. The computer chose {computer} and failed")
        rating += 100
    else:
        print(f"Sorry, but the computer chose {computer}")
    return main(rating, options)


main(identification(), set_options())
