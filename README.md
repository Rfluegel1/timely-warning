# timely-warning

B Project

Reid Fluegel (flueg047), Alex McKeever (mckee171)

https://csci-4131-final-timely-warning.herokuapp.com/

Bing Maps API

Our project was inspired by the University's emails entitled Timely Warning. Our web app allows the user to report a disturbance that happened which then may then be viewed by anyone. The submit page is interactive with the map giving the coordinates when clicked. The user must enter a name and the description is optional. The view page lists all the reports and pins where each report’s coordinates lie. 

View controller: Grabs the form data, the reports tuples, and renders the template. The javascript then takes care of displaying the bing map and capturing clicks on the map to change the value of the form latitude and longitude fields. On submit, insert route is executed inserting tuple into table and rendering success page.

Submit controller: Grabs the form data and renders the template. The javascript then takes care of displaying bing map and setting pins where reports dictate.

View view: The left contains table with all contents of reports table. The right contains Bing Map with pushpins corresponding to each report.

Submit view: The left contains the fields for a report (name, latitude, longitude, description). The right contains Bing Map which changes the value of the longitude and latitude values on the left when clicked.

Tables: The only table used for this project is the reports table which contains the id (int, PK), name (string), latitude (string), longitude (string), and description (string).

References and resources:
https://www.w3schools.com/ for fancy css
https://www.microsoft.com/en-us/maps/documentation for bing maps

