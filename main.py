#!/usr/bin/env python3

from numpy import log as ln
import subprocess as sub
from colorama import init, Fore, Style

menu = f"""{Fore.BLUE}∆v{Fore.RESET} = {Fore.YELLOW}Ve{Fore.RESET} * ln({Fore.MAGENTA}mi{Fore.RESET} / {Fore.CYAN}mf{Fore.RESET})

{Fore.BLUE}∆v{Fore.RESET}:     the change in velocity of the rocket (m/s)
{Fore.YELLOW}Ve{Fore.RESET}:     the exhaust velocity (m/s)
{Fore.MAGENTA}mi{Fore.RESET}:     the initial mass of the rocket (kg)
{Fore.CYAN}mf{Fore.RESET}:     the final mass of the rocket (kg)

{Style.DIM}This formula assumes a constant exhaust velocity.{Style.RESET_ALL}
        """


def clear(shell=False):
    sub.call("clear", shell=shell)


class Main():
    def __init__(self):
        init(autoreset=True)
        clear()

    def run(self):
        self.get_values()
        self.resolve_deltav()

    def get_values(self):
        try:
            print(menu)
            print(f"{Fore.YELLOW}Ve{Fore.RESET}*ln({Fore.MAGENTA}mi{Fore.RESET}/{Fore.CYAN}mf{Fore.RESET})")
            self.Ve = int(input(f"{Fore.YELLOW}Ve{Fore.RESET} (m/s): "))
            clear()
            print(menu)
            print(f"{Fore.YELLOW}{self.Ve}{Fore.RESET}*ln({Fore.MAGENTA}mi{Fore.RESET}/{Fore.CYAN}mf{Fore.RESET})")
            self.mi = int(input(f"{Fore.MAGENTA}mi{Fore.RESET} (kg): "))
            clear()
            print(menu)
            print(f"{Fore.YELLOW}{self.Ve}{Fore.RESET}*ln({Fore.MAGENTA}{self.mi}{Fore.RESET}/{Fore.CYAN}mf{Fore.RESET})")
            self.mf = int(input(f"{Fore.CYAN}mf{Fore.RESET} (kg): "))
            clear()
            print(menu)
            print(f"{Fore.YELLOW}{self.Ve}{Fore.RESET}*ln({Fore.MAGENTA}{self.mi}{Fore.RESET}/{Fore.CYAN}{self.mf}{Fore.RESET})")
        except ValueError:
            print("Need an integer!")
            exit()

    def resolve_deltav(self):
        self.deltaV = self.Ve*ln(self.mi/self.mf)
        print(f"{Fore.BLUE}∆v{Fore.RESET}: {self.deltaV:.2f} m/s")

"""
try:
    num = int(input("ln: "))
except ValueError:
    print(f"Need an Int not {type(num)}")
"""

main = Main()
main.run()
