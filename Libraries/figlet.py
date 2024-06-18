import sys
from pyfiglet import Figlet

figlet = Figlet()
all_fonts = figlet.getFonts()


if len(sys.argv) == 1:
    phrase = input("Input: ")
    print(figlet.renderText(phrase))
elif ('-f' in sys.argv or '--font' in sys.argv) and sys.argv[2] in all_fonts:
    font_name = sys.argv[2] # nome da fonte
    phrase = input("Input: ")
    figlet.setFont(font=font_name)
    print(figlet.renderText(phrase))
elif '-f' not in sys.argv or '--font' not in sys.argv:
    sys.exit("Invalid usage")
