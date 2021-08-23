@map @points
Feature: Points Map zoom in
	As ENTSOG user,
	I want to zoom in three times
	And ensure small point are on the map
	
	Background:
		Given ENTSOG map is displayed
		
	Scenario:
		When user clicks zoom in
		When user clicks zoom in
		When user clicks zoom in
		Then small point locator is available
