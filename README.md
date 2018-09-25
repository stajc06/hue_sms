# hue_sms
Control a Philips Hue light via SMS

Developers, please see `docs/developers.MD` for cloning, setup, and development instructions and guidelines.


   This program sets up a uses the Twilio SMS service, in connection with a Flask server to allow a SMS message to be converted into usable XY int values. 
   The program takes a String (color) as input, and compares the value with the colors.html file in order to get the appropriate RGB values, to then be converted into the correct XY values.
   
   Future potential additions include flexible input, an increased number of color options, an additional method and timer which would alternate the light between two colors, and a mobile app which would provide information on the light and allow for control of the light via the app.