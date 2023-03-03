#! /usr/bin/python3

from pprint import pprint

from gestalt import *

a_display = Gestalt.QtDisplay()

styles = Stylesheet.parse("layout.yml")

data = Spreadsheet.rows("data.csv")

for key, item in styles.items():
	if type(item) is Gestalt.Node:
		if item.classname == "Form":
			a_display.setProperties(item.attrs)
		else:
			a_display.append(item.generateQt({}))

#a_display.addChild( styles["UILabel"])
#a_display.addChild( styles["UIHeader"])

#y_val = styles["UIHeader"]["geometry"]["y"] + 30

#for row in Spreadsheet.rows("data.csv"):
	
#	if row["Used"] == "x":
#		a_display.addChild(styles["UIRow"].position(0, y_val), macros=row)
	
#		y_val += styles["UIRow"]["geometry"]["height"]
	
	
a_display.setProperty("geometry", Type.Rect(935, 60))

a_display.writeQt("commonPlugins.ui")
