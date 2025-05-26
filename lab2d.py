#!/usr/bin/env python3
import sys

# Check if exactly 2 arguments are provided
if len(sys.argv) != 3:
    print("Usage: " + sys.argv[0] + " name age")
    sys.exit()

# If correct, assign arguments
name = sys.argv[1]
age = sys.argv[2]

# Display the message
print("Hi " + name + ", you are " + age + " years old.")

