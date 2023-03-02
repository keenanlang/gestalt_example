#! /APSshare/anaconda3/x86_64/bin/python

from pprint import pprint

from gestalt import *

styles = Stylesheet.parse("layout.yml")

a_display = Gestalt.Display()

for key, item in styles.items():
	if type(item) is Gestalt.Widget and item.classname == "Form":
		a_display.setProperties(item.attrs)

a_display.addChild( styles["UILabel"])
a_display.addChild( styles["UIHeader"])

y_val = styles["UIHeader"]["geometry"]["y"] + 30

for row in Spreadsheet.rows("data.csv"):
	
	if row["Used"] == "x":
		a_display.addChild(styles["UIRow"].position(0, y_val), macros=row)
	
		y_val += styles["UIRow"]["geometry"]["height"]
	
	
a_display.setProperty("geometry", Type.Rect(935, y_val))
	
a_display.writeQt("commonPlugins.ui")
