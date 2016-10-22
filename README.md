#Pinout.xyz

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a>

[Pinout.xyz](http://pinout.xyz/) is the successor to the popular Pi pinout website originally hosted on http://pi.gadgetoid.com/pinout

To support translation efforts, and allow people to build tools with the data in this repository, Pinout.xyz is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.

This license excludes the file pinout-graphic-horizontal.ai, which is provided under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a> to permit commercial use; specifically publication in books and magazines with appropriate attribution.

#About this project

This project aims to build a consistent workflow behind the Pinout.xyz front-end, gather useful information about the Raspberry Pi GPIO interface and add-on boards, and invite board manufacturers to produce their own "overlay" files which describe which pins their Pi add-ons use.

We hope that by making this project open and extensible we will invite not only contributions of board pinouts, but translations too.

#Contributing

If you have a board you'd like to contribute, raise an [issue](https://github.com/Gadgetoid/Pinout.xyz/issues) and we'll consider it!

If you've spotted an error, ommission or have a suggestion then you're welcome to do the same.

#Translating

The contents of this GitHub repository are used to build http://pinout.xyz and its translated subdomains.

Maintainers: [@Gadgetoid](https://github.com/Gadgetoid) and [@RogueM](https://github.com/RogueM)

GPIO Zero code examples by: [@bennuttall](https://github.com/bennuttall)

Notable contributions:

* [en](http://pinout.xyz/) - [@lurch](https://github.com/lurch) and [@abelectronicsuk](https://github.com/abelectronicsuk)
* [de](http://de.pinout.xyz/) - [@rdmueller](https://github.com/rdmueller) and [@KojoePi](https://github.com/KojoePi)
* [es](http://es.pinout.xyz/) - [@ResonantWave](https://github.com/ResonantWave) and [@IkerGarcia](https://github.com/IkerGarcia)
* [fr](http://fr.pinout.xyz/) - [@RogueM](https://github.com/RogueM) and [@smileyn64](https://github.com/smileyn64)
* [it](http://it.pinout.xyz/) - [@LizardM4](https://github.com/LizardM4)
* [tr](http://tr.pinout.xyz/) - [@Ardakilic](https://github.com/Ardakilic)

If you would like to provide support for a language not yet in the repository you should start by duplicating the `src/en` directory to the appropriate language-code. For example, if you want to create a German translation you would create the folder `src/de`.

There are no plans to support cultures (it would just get out of hand!), so you can't have `src/fr-CA` ( sorry! ).

Once you've made your translation, build and preview it with, for example:

```bash
make serve LANG=de
```

And then open: http://127.0.0.1:5000 in your browser.

*note: if you are facing issues on your preview (card not showing, text update not appearing ...), you can fix it by erasing you browser cache (image and cache file only)*

Please do not attempt to translate the `/resources` folder, this is shared between sites on the server and should be generic.

Feel free to modify the template with links relevant to your country, and / or your Twitter handle, but don't fiddle with the structure!

Submit your finished translation as a [pull request](https://github.com/Gadgetoid/Pinout.xyz/pulls) and we'll get it live on its own *&lt;languagecode&gt;*.pinout.xyz subdomain :)

#Roadmap &amp; wishlist

* Redesign HTML generation and unify HTML templates into a single, translatable file
* Add functionality to compare two or more boards, to visualise pin compatibility
* Tool to convert WiringPi to GPIO to BCM and back
* Add as many [boards](http://pinout.xyz/boards) as possible!
