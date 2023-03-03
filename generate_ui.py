#! /usr/bin/python3

from pprint import pprint

from gestalt import *


Gestalt.generateQtFile(stylesheet="layout.yml", datafile="data.yml", outputfile="commonPlugins.ui")
