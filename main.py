#!/usr/bin/env python3

from numpy import log as ln
import subprocess as sub
from colorama import init, Fore, Style

menu = f"""{Fore.BLUE}∆v{Fore.RESET} = {Fore.YELLOW}Ve{Fore.RESET} * ln({Fore.MAGENTA}mi{Fore.RESET} / {Fore.CYAN}mf{Fore.RESET})

∆v:     the change in velocity of the rocket (m/s)
Ve:     the exhaust velocity (m/s)
mi:     the initial mass of the rocket (kg)
mf:     the final mass of the rocket (kg)

This formula assumes a constant exhaust velocity.
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
            print("Ve*ln(mi/mf)")
            self.Ve = int(input("Ve (m/s): "))
            clear()
            print(menu)
            print(f"{self.Ve}*ln(mi/mf)")
            self.mi = int(input("mi (kg): "))
            clear()
            print(menu)
            print(f"{self.Ve}*ln({self.mi}/mf)")
            self.mf = int(input("mf (kg): "))
            clear()
            print(menu)
            print(f"{self.Ve}*ln({self.mi}/{self.mf})")
        except ValueError:
            print("Need an integer!")

    def resolve_deltav(self):
        self.deltaV = self.Ve*ln(self.mi/self.mf)
        print(f"∆v: {self.deltaV:.2f} m/s")

"""
try:
    num = int(input("ln: "))
except ValueError:
    print(f"Need an Int not {type(num)}")
"""

main = Main()
main.run()
