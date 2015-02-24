#Pinout 2

Pinout 2 will be the successor to the popular Pi pinout website http://pi.gadgetoid.com/pinout

This project aims to build a consistent workflow behind the Pinout front-end, and invite board manufacturers
to produce their own "overlay" files which describe which pins their Pi add-ons use.

I hope that by making this project open and extensible I will invite not only contributions of board pinouts,
but translation efforts too.

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
