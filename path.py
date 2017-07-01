import sys
import os


print sys.path

# print __file__

base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(base_dir)

print os.path.abspath(__file__)

print os.path.dirname(os.path.abspath(__file__))

print sys.path
