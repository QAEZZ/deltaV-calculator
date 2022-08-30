#!/usr/bin/env python3

from numpy import log as ln
import math
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
            self.Ve = input(f"{Fore.YELLOW}Ve{Fore.RESET} (m/s): ")
            clear()
            print(menu)
            print(f"{Fore.YELLOW}{self.Ve}{Fore.RESET}*ln({Fore.MAGENTA}mi{Fore.RESET}/{Fore.CYAN}mf{Fore.RESET})")
            self.mi = input(f"{Fore.MAGENTA}mi{Fore.RESET} (kg): ")
            clear()
            print(menu)
            print(f"{Fore.YELLOW}{self.Ve}{Fore.RESET}*ln({Fore.MAGENTA}{self.mi}{Fore.RESET}/{Fore.CYAN}mf{Fore.RESET})")
            self.mf = input(f"{Fore.CYAN}mf{Fore.RESET} (kg): ")
            clear()
            print(menu)
            print(f"{Fore.YELLOW}{self.Ve}{Fore.RESET}*ln({Fore.MAGENTA}{self.mi}{Fore.RESET}/{Fore.CYAN}{self.mf}{Fore.RESET})")

            self.Ve = float(self.Ve)
            self.mi = float(self.mi)
            self.mf = float(self.mf)

        except ValueError:
            print("Need an integer or float!")
            exit()

    def resolve_deltav(self):
        self.deltaV = str(self.Ve*math.log(self.mi/self.mf))

        if "-" in self.deltaV or self.deltaV.startswith("0.0"):
            self.outcome = f"{Fore.BLUE}∆v{Fore.RESET}: {Fore.RED}{self.deltaV}{Fore.RESET} m/s"
        else:
            self.outcome = f"{Fore.BLUE}∆v{Fore.RESET}: {Fore.GREEN}{self.deltaV}{Fore.RESET} m/s"
        print(self.outcome)

"""
try:
    num = int(input("ln: "))
except ValueError:
    print(f"Need an Int not {type(num)}")
"""

main = Main()
main.run()
