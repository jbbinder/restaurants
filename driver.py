
"""
Driver file
"""
import os
import sys
sys.path.append(os.getcwd())
from .ingest import IngestSystem

strt = IngestSystem('http://www.allmenus.com/dc/washington/-/?sort=popular')



#if __name__ == '__main__':
