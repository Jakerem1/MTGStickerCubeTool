import colorama

colorama.init()

# Define a colormap from low to high
colours = {
    "BLACK": colorama.Fore.BLACK,
    "RED": colorama.Fore.RED,
    "GREEN": colorama.Fore.GREEN,
    "YELLOW": colorama.Fore.YELLOW,
    "BLUE": colorama.Fore.BLUE,
    "MAGENTA": colorama.Fore.MAGENTA,
    "CYAN": colorama.Fore.CYAN,
    "WHITE": colorama.Fore.WHITE,
    "LIGHTBLACK_EX": colorama.Fore.LIGHTBLACK_EX,
    "LIGHTRED_EX": colorama.Fore.LIGHTRED_EX,
    "LIGHTGREEN_EX": colorama.Fore.LIGHTGREEN_EX,
    "LIGHTYELLOW_EX": colorama.Fore.LIGHTYELLOW_EX,
    "LIGHTBLUE_EX": colorama.Fore.LIGHTBLUE_EX,
    "LIGHTMAGENTA_EX": colorama.Fore.LIGHTMAGENTA_EX,
    "LIGHTCYAN_EX": colorama.Fore.LIGHTCYAN_EX,
    "LIGHTWHITE_EX": colorama.Fore.LIGHTWHITE_EX,
    "RESET": "\033[0m"
}

def color_text(text, color: str):
    return f"{colours.get(color.upper(), colours['RESET'])}{text}{colours['RESET']}"
