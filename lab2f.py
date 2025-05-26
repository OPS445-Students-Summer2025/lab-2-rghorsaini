#!/usr/bin/env python3
# Author: Ranjan Ghorsaini
# Author ID: 144843224
# Date Created: 2025/05/26

import sys

# If no argument is provided, exit with error
if len(sys.argv) != 2:
    sys.exit(1)

# Geting the number from and converting to integer
timer = int(sys.argv[1])

# Count down until 0
while timer > 0:
    print(timer)
    timer = timer - 1

print("blast off!")

