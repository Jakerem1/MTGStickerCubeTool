# MTG Card CLI Tool

## Overview
The MTG Card CLI Tool is a command-line interface application designed to process text files containing lists of Magic: The Gathering (MTG) cards. It allows users to manage decks, count card occurrences, and compare card lists, all while providing a colorful and user-friendly console output.

## Features
- Process text files containing MTG card lists.
- List all cards with their respective decks and counts.
- Compare current card lists with previously saved lists.
- Assign colors to each deck for enhanced console output.
- Save colored lists as text files.

## Installation
To get started with the MTG Card CLI Tool, clone the repository and install the required dependencies:

```bash
git clone <repository-url>
cd MTGStickerCubeTool
pip install -r requirements.txt
```

## Usage
To run the CLI tool, place the TXT file(s) containing the Moxfield Lists in the input/ folder and use the following command:

```bash
python main.py [options]
```

### Options
- `--append <file>`: Specify an existing cube file to update.
- `--save <file>`: Specify the cube name to save the processed cube.
- `--compare <file>`: Compare the current cube with a previously saved cube.
- `--help`: Show help information about the available commands and options.

## Example
To process a card list and save the output, you can run:

```bash
python src/main.py --save "Sticker Cube 1"
```

## License
This project is licensed under the MIT License. See the LICENSE file for more details.