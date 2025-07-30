# filepath: mtg_card_cli_tool/mtg_card_cli_tool/src/main.py

import argparse
import os
import json
from src import color_utils

class Cube():
    def __init__(self):
        self.cards = {}

    def add_deck(self, deck):
        for card, count in deck.cards.items():
            if card in self.cards:
                if deck.name in self.cards[card]:
                    self.cards[card][deck.name]["number"] += count
                else:
                    self.cards[card][deck.name] = {
                    "number": count,
                    "colour": deck.colour
                    }
            else:
                self.cards[card] = {deck.name: {
                    "number": count,
                    "colour": deck.colour
                    }}

    def print_card_summary(self, card_name):
        print(f"    {card_name}")
        for deck_name, info in self.cards[card_name].items():
            print(color_utils.color_text(f"        {deck_name}: {info['number']}", color=info['colour'].lower()))

    def print_summary(self):
        for card in sorted(self.cards.keys()):
            self.print_card_summary(card)

class Deck():
    def __init__(self, name):
        self.name = name
        self.cards = {}
        self.colour = 'white'  # Default color

    def add_card(self, card_name, count):
        if card_name in self.cards:
            self.cards[card_name] += count
        else:
            self.cards[card_name] = count

    def get_summary(self):
        return {card: count for card, count in self.cards.items()}

def read_card_data(file_path, deck_name):
    deck = Deck(deck_name)
    with open(file_path, 'r') as file:
        for line in file:

            if line.upper().startswith(('COLOUR', 'COLOR')):
                deck.colour = line.split('=')[1].split("#")[0].strip().upper()
                continue

            important_info = line.split('(')[0].strip()
            number = int(important_info.split(' ')[0])
            card_name = ' '.join(important_info.split(' ')[1:])
            if card_name:
                deck.add_card(card_name, number)

    return deck

def main():
    parser = argparse.ArgumentParser(description="MTG Card CLI Tool")
    parser.add_argument('--save', type=str, help='Name of the cube being saved')
    parser.add_argument('--compare', type=str, help='Name of the cube being compared against')
    parser.add_argument('--append', type=str, help='Name of the cube being appended to')

    args = parser.parse_args()

    # Load comparison cube if requested
    compare_cube = Cube()
    if args.compare:
        with open(f"storage/{args.compare}.json", 'r') as f:
            compare_cube.cards = json.load(f)

    # Load original cube if appending
    input_cube = Cube()
    if args.append:
        with open(f"storage/{args.append}.json", 'r') as f:
            input_cube.cards = json.load(f)

    # Process the card list from the provided file
    files = os.listdir("input/")
    for file in files:
        if file.endswith('.txt'):
            print(f"Processing file: {file}")
            file_path = os.path.join("input/", file)
            deck = read_card_data(file_path, file.split('.')[0].replace(" ", "_"))
            input_cube.add_deck(deck)

    if not args.compare:
        # Display the card summary
        input_cube.print_summary()
        total_cards = sum(sum(deck_info['number'] for deck_info in deck.values()) for deck in input_cube.cards.values())
        print(f"\nTotal Cards:{total_cards}")
        cube_count = 0
        for card in input_cube.cards.values():
            max_count = max(info['number'] for info in card.values())
            cube_count += max_count
        print(f"Total Cards in Cube:{cube_count}")
        print(f"Improvement: {cube_count / total_cards * 100:.2f}%")

    # Save the summary if requested
    if args.save:
        with open(f"storage/{args.save}.json", 'w') as f:
            summary = input_cube.cards
            json.dump(summary, f, indent=4)

    if args.compare:
        print("Comparison with existing cube:")
        print("================================\n")
        print(f"Cards Exist in Existing Cube:")
        print("--------------------------------")
        for card_name in set(compare_cube.cards.keys()).intersection(input_cube.cards.keys()):
            input_cube.print_card_summary(card_name)

        print(f"\nUnique to New Cube:")
        print("--------------------------------")
        for card_name in set(input_cube.cards.keys()).difference(compare_cube.cards.keys()):
            input_cube.print_card_summary(card_name)


if __name__ == "__main__":
    main()