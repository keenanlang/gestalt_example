#! /APSshare/anaconda3/x86_64/bin/python

from pprint import pprint

from gestalt import *

styles = Stylesheet.parse("layout.yml")

a_display = Gestalt.Display()

a_display.addChild( Gestalt.Widget("caLabel", layout=styles["clear_coloring"])
	.setProperties( geometry="935x25", text="$(P) Common Plugins")
	.position(0, 6) )

a_display.addChild( styles["UIHeader"].position(0, 40), macros={ 'text': "Plugin Type" })

y_val = 71

for row in Spreadsheet.rows("data.csv"):	
	a_display.addChild(styles["UIRow"].position(0, y_val), macros=row)
	
	y_val += 25
	
	
a_display.setProperty("geometry", Type.Rect(935, y_val))
	
a_display.writeQt("commonPlugins.ui")
