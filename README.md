# Pinout.xyz

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a>

[Pinout.xyz](http://pinout.xyz/) is the successor to the popular Pi pinout website originally hosted on [http://pi.gadgetoid.com/pinout](http://pi.gadgetoid.com/pinout).

To support translation efforts, and allow people to build documentation and tools with the data in this repository, Pinout.xyz is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/).

The license was previously explicitly non-commercial, to understand why it has been changed please see: https://github.com/pinout-xyz/Pinout.xyz/issues/481

This license includes the 'pinout-graphic-horizontal' files located in the `graphics` directory and the 'pi-orientation' graphic located in `resources`, which are provided to permit commercial use; specifically publication in books and magazines with appropriate attribution.

The flags in `resources/flags` are from [flag-icons](https://github.com/lipis/flag-icons) and are MIT licensed, see `resources/flags/LICENSE`. The Spanish flag is the civil version, with the coat of arms removed to keep the file small. To add a flag for a new language, take the 4x3 SVG for the country you want from that project.

The license excludes all board photography which has been supplied by manufacturers or customers via PR without any explicit license grant, or supplied under the implicit permission of my (@Gadgetoid) employment at Pimoroni. Re-use of product photography is normally assumed to be implicitly permitted for resale or promotional purposes, but I cannot pass a nebulous, implicit license on for re-use. YMMV.

If you copy and re-use this website henceforth, I would prefer full attribution in the page footer, for example:

Based on <a href="https://pinout.xyz">Pinout.xyz</a> created by <a href="https://fosstodon.org/@gadgetoid">@gadgetoid.</a>
Maintained by @yourname, contribute at https://github.com/yourname/yourfork

If you're a commercial venture, or closely associated, I would also appreciate, but do not require, that you review Pinout's funding options and maybe chuck me a bone!

# About this project

The contents of this GitHub repository are used to build https://pinout.xyz and its translations, which are published as subdirectories such as https://pinout.xyz/de/.

This project aims to build a consistent workflow behind the Pinout.xyz front-end, gather useful information about the Raspberry Pi GPIO interface and add-on boards, and invite board manufacturers to produce their own "overlay" files which describe which pins their Pi add-ons use.

We hope that by making this project open and extensible we will invite not only contributions of board pinouts, but translations too.

# Reporting Issues & Making Suggestions

If you've spotted an error, omission or have a suggestion, raise an [issue](https://github.com/pinout-xyz/Pinout.xyz/issues). Feedback on every aspect of the site or this repository is welcome!

# Contributing

If you have a board you'd like to contribute, the preferred method for submission is to create a modified version of the overlay [template](https://github.com/pinout-xyz/Pinout.xyz/blob/master/draft/overlay/template.md) and create a pull request. Please ensure the files you submit are being pushed to the `/draft` folder, where it will be reviewed before publication.

Note that as part of the submission, a top-down view of the board in the form of a [png](https://github.com/pinout-xyz/Pinout.xyz/blob/master/draft/boards/template.png) is expected. If you can't produce the png file yourself, just duplicate and rename `template.png` but make sure to include a url somewhere in the overlay where we can fetch a suitable graphic.

Once your draft has been made, before filing a pull request, you should try to render the page and make sure it build and appears as intended. To do so:

```bash
python3 -m pinoutxyz boards publish myboard
make serve
```

And then open: http://127.0.0.1:8080 in your browser.

Once you are happy with the result, 

```bash
python3 -m pinoutxyz boards unpublish myboard
```
(this will file the overlay back into the draft folder, ready for review)

`make watch` serves the site and rebuilds it whenever anything under `src`, `common` or `resources` changes.

*note 1: you will need several python modules installed on your system to render and serve a local version of the site, run*  
*`pip install -r requirements.txt` from the top of the repository tree to install the required modules.*

*note 2: if you are facing issues with your preview (board not showing, text update not appearing, etc.), you can fix it by erasing your browser's cache (image and cache file only).*

If you feel that the requirements for submissions is beyond your current possibilities, you may raise an [issue](https://github.com/pinout-xyz/Pinout.xyz/issues) requesting the addition of a specific board instead and we'll consider it!


## Running in Docker

The webserver can also be run in a Docker container. To do this, you first need to build the Docker image:

```bash
docker build -t pinout.xyz .
```

Next, you can start the containerized webserver:

```bash
docker run -p 8080:8080 pinout.xyz
```

Now you can access the webserver at http://127.0.0.1:8080.

Set `PINOUT_LANG` to serve a language other than English:

```bash
docker run -p 8080:8080 -e PINOUT_LANG=de pinout.xyz
```

Optionally you can include a draft board in the image by setting the `PUBLISH_DRAFT` build argument:

```bash
docker build --build-arg PUBLISH_DRAFT=myboard -t pinout.xyz .
```

# Translating

If you would like to provide support for a language not yet in the repository you should start by duplicating the `src/en` directory to the appropriate [language-code](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes). For example, if you want to create a Czech translation you would create the folder `src/cs`. Note that there are no plans to support cultures (it would just get out of hand), so you can't have `src/fr-CA` (sorry!).

Set `language`, `locale` and `flag` in your `settings.yaml` so the language switcher can label and flag your language.

The first resources we recommend you translate are the language-specific strings found in the `settings.yaml` file, `pi-pinout.md`, `index.md`, `404.md` and the `footer.html` template, as well as the content of the `/pin` folder, preferably.

Once that's done, rename the `/overlay` folder to `/translate` and start translating the boards markdown files (pick any you fancy translating, it does not have to be the first board in alphabetical order). Move each finished translation into the `/overlay` folder, leaving the untranslated English copies in `/translate`.

`python3 -m pinoutxyz translations list` shows how much of each language is done, and `python3 -m pinoutxyz translations outstanding de` lists the overlays still waiting for a translation. Board metadata is shared, not translated, so `python3 -m pinoutxyz translations check` reports any frontmatter that has drifted away from `src/en`; only `name`, `description`, `page_url` and the pin `name` fields are yours to change.

Please do not attempt to translate the `/resources` folder, or anything not specifically mentioned in this section of the README - all files outside your *&lt;languagecode&gt;* directory are shared between the languages and are meant to be generic. Feel free to modify the template with links relevant to your country, and / or your own social handle however, but don't fiddle with the structure!

Once you've made your translation, you can build and preview it with, for example:

```bash
make serve LANG=de
```

And then open: http://127.0.0.1:8080/de/ in your browser.

The last step will be to submit your finished translation as a [pull request](https://github.com/pinout-xyz/Pinout.xyz/pulls) (this can include any number of boards, it does not have to be the entire line-up) and we'll get it live at its own pinout.xyz/*&lt;languagecode&gt;*/ path.

If you wish to provide a translation for a language that is already published, or correct a typo in an existing markdown file, just edit the file in place (leaving the files in the `translate` folder for review, if you are pushing a translation).

If you have a question about translations, raise an [issue](https://github.com/pinout-xyz/Pinout.xyz/issues) and we'll be happy to help you get past whatever hurdle you may face!


# Building

The builder is the `pinoutxyz` package at the root of this repository. `make` wraps the commands you'll want most often, but you can call it directly:

```bash
python3 -m pinoutxyz build              # every language, into output/<lang>
python3 -m pinoutxyz build en --site    # one language, assembled into output/site
python3 -m pinoutxyz serve --watch      # serve on :8080 and rebuild on change
python3 -m pinoutxyz translations list  # translation coverage per language
python3 -m pinoutxyz boards list        # drafts awaiting publication
```

Add `--help` to any of them for the full set of options. `pip install -e .` puts a `pinoutxyz` command on your path if you'd rather not type `python3 -m`.

# Roadmap &amp; wishlist

* Make translations true overlays of the English source, so board metadata lives in one place
* Add functionality to compare two or more boards, to visualise pin compatibility
* Tool to convert WiringPi to GPIO to BCM and back
* Add as many [boards](http://pinout.xyz/boards) as possible!

# Acknowledgement

Maintainers: [@Gadgetoid](https://github.com/Gadgetoid) and [@RogueM](https://github.com/RogueM)

GPIO Zero code examples by: [@bennuttall](https://github.com/bennuttall)

Notable contributions:

* [en](http://pinout.xyz/) - [@lurch](https://github.com/lurch), [@abelectronicsuk](https://github.com/abelectronicsuk) and [@francesco-vannini](https://github.com/francesco-vannini)
* [de](http://de.pinout.xyz/) - [@rdmueller](https://github.com/rdmueller) and [@KojoePi](https://github.com/KojoePi)
* [es](http://es.pinout.xyz/) - [@ResonantWave](https://github.com/ResonantWave) and [@IkerGarcia](https://github.com/IkerGarcia)
* [fr](http://fr.pinout.xyz/) - [@RogueM](https://github.com/RogueM) and [@smileyn64](https://github.com/smileyn64)
* [it](http://it.pinout.xyz/) - [@LizardM4](https://github.com/LizardM4)
* [tr](http://tr.pinout.xyz/) - [@Ardakilic](https://github.com/Ardakilic)
