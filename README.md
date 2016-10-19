#Pinout.xyz

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a>

Pinout.xyz is the successor to the popular Pi pinout website originally hosted on http://pi.gadgetoid.com/pinout

To support translation efforts, and allow people to build tools with the data in this repository, Pinout.xyz is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.

This license excludes the file pinout-graphic-horizontal.ai, which is provided under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a> to permit commercial use; specifically publication in books and magazines with appropriate attribution.

#About this project

This project aims to build a consistent workflow behind the Pinout.xyz front-end, gather useful information about the Raspberry Pi GPIO interface and add-on boards, and invite board manufacturers to produce their own "overlay" files which describe which pins their Pi add-ons use.

We hope that by making this project open and extensible I will invite not only contributions of board pinouts, but translations too.

#Contributing

If you have a board you'd like to contribute, raise an issue and we'll consider it!

If you've spotted an error, ommission or have a suggestion then you're welcome to do the same.

#Translating

The contents of this GitHub repository are used to build http://pinout.xyz and its translated subdomains.

Current known contributors are:

* de - @rdmueller and @KojoePi
* es - @ResonantWave and @IkerGarcia
* fr - @RogueM
* it - @LizardM4 
* pt - @Maslor
* tr - @Ardakilic

If you would like to provide support for a language not yet in the repository you should start by duplicating the `src/en` directory to the appropriate culture. For example if you want to create a German translation you would create the folder `src/de`.

There are no plans to support cultures (it would just get out of hand!), so you can't have `src/fr-CA` ( sorry! ).

Once you've made your translation, build and preview it with, for example:

```bash
make serve LANG=de
```

And then open: http://127.0.0.1:5000 in your browser.

Please do not attempt to translate the `/resources` folder, this is shared between sites on the server and should be generic.

Feel free to modify the template with links relevent to your country, and your Twitter handle but don't fiddle with the structure!

Submit your finished translation as a pull request and we'll get it live on its own pinout.xyz subdomain :)

#Roadmap & wishlist

* Redesign HTML generation and unify HTML templates into a single, translatable file
* Add functionality to compare two or more boards, to visualise pin compatibility
* Tool to convert WiringPi to GPIO to BCM and back
* Add as many boards as possible!
