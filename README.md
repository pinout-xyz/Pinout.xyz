#Pinout 2

Pinout 2 is the successor to the popular Pi pinout website http://pi.gadgetoid.com/pinout

To support translation efforts, and allow people to build tools with the data in this repository, Pinout 2 is
provided under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.

This project aims to build a consistent workflow behind the Pinout front-end, and invite board manufacturers
to produce their own "overlay" files which describe which pins their Pi add-ons use.

I hope that by making this project open and extensible I will invite not only contributions of board pinouts,
but translations too.

I'm also looking for feedback about the structure of the JSON files, what information needs to be contained in
them, how they can better support translation and any other suggestions you might have.

#Contributing

The contents of this GitHub repository are used to build http://pi.gadgetoid.com/pinout.

If you have a board you'd like to contribute, you should look at these folders:

* [overlay/](overlay/)
* [description/overlay/](description/overlay/)

#Roadmap

##Phase 1

Replace the current Pinout site with a generated version built from this repository, aim for 100% compatibility.

* Drop ancient and redundant boards such as ladder, Clockatoo
* Replace things like Arduino with more relevant and up-to-date alternatives ( Alex's PiDuino )
* Compliment Pibrella with Explorer HAT (Pro)

##Phase 2

Redesign UI to support browsing a wider variety of boards and viewing their pinouts, description, links to library
+  buy links etc.

* Replace top tabs with some sort of search functionality or easy categorised UI for finding boards
* Allow for slightly longer descriptions of Pin functions ( baloons? ), current width is very restrictive

##Phase 3

Introduce advanced functionality such as board compatibility checks and more detailed overlays on Pin alt functions.

* Does X board work with Y board
* What extra functions does this pin have
* Convert WiringPi to GPIO to BCM and back
