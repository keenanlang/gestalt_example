#! /APSshare/anaconda3/x86_64/bin/python

from pprint import pprint

from gestalt import *

styles = Stylesheet.parse("layout.yml")

a_display = Gestalt.Display()

a_display.addChild( Gestalt.Widget("caLabel", layout=styles["clear_coloring"])
	.setProperties( geometry="935x25", text="$(P) Common Plugins")
	.position(0, 6) )

a_display.addChild( Gestalt.Widget("caLabel", layout=styles["clear_label"])
	.setProperties(geometry="110x20", text="Plugin Name")
	.position(10, 40) )

a_display.addChild( Gestalt.Widget("caLabel", layout=styles["clear_label"])
	.setProperties(geometry="110x20", text="Plugin Type")
	.position(150, 40) )

a_display.addChild( Gestalt.Widget("caLabel", layout=styles["clear_label"])
	.setProperties(geometry="40x20", text="Port")
	.position(300, 40) )

a_display.addChild( Gestalt.Widget("caLabel", layout=styles["clear_label"])
	.setProperties(geometry="60x20", text="Enable")
	.position(407, 40) )

a_display.addChild( Gestalt.Widget("caLabel", layout=styles["clear_label"])
	.setProperties(geometry="80x20", text="Blocking")
	.position(525, 40) )

a_display.addChild( Gestalt.Widget("caLabel", layout=styles["clear_label"])
	.setProperties(geometry="70x20", text="Dropped")
	.position(615, 40) )

a_display.addChild( Gestalt.Widget("caLabel", layout=styles["clear_label"])
	.setProperties(geometry="40x20", text="Free")
	.position(730, 40) )

a_display.addChild( Gestalt.Widget("caLabel", layout=styles["clear_label"])
	.setProperties(geometry="40x20", text="Rate")
	.position(800, 40) )

y_val = 71

for row in Data.rows("data.xlsx"):
	
	#Plugin Name
	a_display.addChild( Gestalt.Widget("caLineEdit", layout=styles["clear_lineedit"])
			.setProperty("channel", "$(P)" + row["Instance"] + ":PortName_RBV")
			.setProperty("geometry", "110x18")
			.position(10, y_val) )
	
	#Plugin Type
	a_display.addChild( Gestalt.Widget("caLineEdit", layout=styles["clear_lineedit"])
			.setProperty("channel", "$(P)" + row["Instance"] + ":PluginType_RBV")
			.setProperty("geometry", "160x18")
			.position(125, y_val) )
	
	#NDArray Port
	a_display.addChild( Gestalt.Widget("caTextEntry", layout=styles["blue_entry"])
			.setProperty("channel", "$(P)" + row["Instance"] + ":NDArrayPort")
			.position(290, y_val - 1) )
	
	#Enabled
	a_display.addChild( Gestalt.Widget("caMenu", layout=styles["blue_menu"])
			.setProperty("channel", "$(P)" + row["Instance"] + ":EnableCallbacks")
			.position(355, y_val - 1) )
	
	#Enabled Readback
	a_display.addChild( Gestalt.Widget("caLineEdit", layout=styles["gray_coloring"])
			.setProperty("channel", "$(P)" + row["Instance"] + ":EnableCallbacks_RBV")
			.position(440, y_val) )
	
	#Callback Blocking
	a_display.addChild( Gestalt.Widget("caMenu", layout=styles["blue_menu"])
			.setProperty("channel", "$(P)" + row["Instance"] + ":BlockingCallbacks")
			.position(525, y_val - 1) )
	
	#Dropped Arrays
	a_display.addChild( Gestalt.Widget("caLineEdit", layout=styles["clear_lineedit"])
			.setProperty("channel", "$(P)" + row["Instance"] + ":DroppedArrays_RBV")
			.position(610, y_val) )
	
	#Queue Free
	a_display.addChild( Gestalt.Widget("caLineEdit", layout=styles["gray_coloring"])
			.setProperty("channel", "$(P)" + row["Instance"] + ":QueueFree")
			.position(695, y_val) )
	
	#Rate
	a_display.addChild( Gestalt.Widget("caLineEdit", layout=styles["clear_lineedit"])
			.setProperty("channel", "$(P)" + row["Instance"] + ":ArrayRate_RBV")
			.position(780, y_val) )

	
	#Related Displays
	a_display.addChild( Gestalt.Widget("caRelatedDisplay", layout=styles["rel_displays"])
			.setProperties(labels=row["Instance"], files=row["related files"], args=row["args"])
			.position(865, y_val - 1) )
	
	
	y_val += 25
	
	
a_display.setProperty("geometry", Type.Rect(935, y_val))
	
a_display.writeQt("commonPlugins.ui")
