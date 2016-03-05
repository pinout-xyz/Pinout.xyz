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

If you have a board you'd like to contribute, raise an issue and we'll consider it!

#Translating

The contents of this GitHub repository are used to build http://pinout.xyz and its translated subdomains.

Current known contributors are:

* de - @rdmueller and @KojoePi
* es - @ResonantWave
* fr - @RogueM
* it - @LizardM4 
* pt - @Maslor
* tr - @Ardakilic

If you would like to provide support for a language not yet in the repository you should start by duplicating the `src/en` directory to the
appropriate culture. For example if you want to create a German translation you would create the folder `src/de`.

There are no plans to support cultures, so you can't have `src/fr-CA` ( sorry! ).

Once you've made your translation, build and preview it with, for example:

```bash
make serve LANG=de
```

And then open: http://127.0.0.1:5000 in your browser.

Please do not attempt to translate the `/resources` folder, this is shared between sites on the server and should be generic.

Feel free to modify the template with links relevent to your country, and your Twitter handle but don't fiddle with the structure!

Submit your finished translation as a pull request and I'll get it live on pinout.xyz.

#Roadmap

* Redesign UI to support browsing a wider variety of boards and viewing their pinouts ( partially done with drop down )
* Replace top tabs with some sort of search functionality or easy categorised UI for finding boards
* Allow for slightly longer descriptions of Pin functions ( baloons? ), current width is very restrictive
* Does X board work with Y board
* What extra functions does this pin have ( mostly done with ALT functions tables, but needs descriptions )
* Tool to convert WiringPi to GPIO to BCM and back
