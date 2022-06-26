from colorama import Fore, Back, Style
from tssuupa import Tßüpa

def main():
    print(Fore.GREEN + "Tekā, e kā de Tßüpa brekeßt." + Style.RESET_ALL)
    āmaken = tsā("Vetümāk āmaken?")
    bākß = tsā("Vetümāk bākß?")
    taskitā = tsā("Vetümāk tāskitā?")
    trek = tsā("Vetümāk trek?")
    Þānb = tsā("Vetümāk Þānb?")
    
    tssupa = Tßüpa()
    tssupa.tok(āmaken, bākß, taskitā, trek, Þānb=Þānb)

def tsā(teteksun: str):
    return int(input(Fore.BLUE + teteksun + " " + Style.RESET_ALL))


if __name__ == "__main__":
    main()