#!/usr/bin/env python

from subprocess import call
from os import system

import argparse

#Get command line options
parser = argparse.ArgumentParser(description='')

#Get options from command
parser.add_argument('--clean', action='store_true', help='Clean LOGs..')
parser.add_argument('--gui'  , action='store_true', help='GUI Simulation')

args = parser.parse_args()


def create_lib():
    system('vlib work')
    system('vmap work work')

def compile_files():
        system('vlog -work work -f barrier_inc.f +define+UVM_NO_DPI')

def simulate():
    if args.gui:
        system('vsim work.top -do "run -all;"')
    else:
        system('vsim work.top -c -do "run -all; exit;"')


def clean():
    system('rm -r modelsim.ini transcript vsim.wlf work')


def main():
    if args.clean:
        clean()
    else:
        create_lib()
        compile_files()
        simulate()


if __name__ == '__main__':
    main()

