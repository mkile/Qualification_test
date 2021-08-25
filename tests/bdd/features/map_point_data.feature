@map @points
Feature: Points Map
	As ENTSOG user,
	I want to zoom in and see elements changing
	And filter map points by type
	
	Scenario: Locate small point locators on zoomed in map
		Given ENTSOG map is displayed
		When user clicks zoom in
		And user clicks zoom in
		And user clicks zoom in

	Scenario Outline: Filter points
		Given ENTSOG map is displayed
		When user opens filters panel
#		And user clicks points filter select
		And user sets infrastructure filter to <filter>
		Then <point_type> points are on the map
		Examples:
		| filter 			| point_type				  		|
		| Distribution		| div.map-marker-incoun_dis-small 	|
		| Transmission		| div.map-marker-cb_itp-small	  	|
		| Storage			| div.map-marker-cb_ugs-small	  	|
		| Final Consumers	| div.map-marker-incoun_fnc-small 	|
		| LNG Entry			| div.map-marker-incoun_lng-small 	|
		| Production		| div.map-marker-incoun_prd-small 	|
		| Trading			| div.map-marker-incoun_vtp-small 	|
