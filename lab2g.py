#!/usr/bin/env python3
# Author: Ranjan Ghorsaini
# Author ID: 144843224
# Date Created: 2025/05/26

import sys

# If user gave a number, use it; otherwise use 3
if len(sys.argv) == 2:
    timer = int(sys.argv[1])
else:
    timer = 3

# Countdown loop
while timer > 0:
    print(timer)
    timer = timer - 1

print("blast off!")
