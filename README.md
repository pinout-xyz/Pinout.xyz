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

Mount the repository over `/app` to work on the site without rebuilding the image. The container rebuilds whenever you edit anything under `src`, `common` or `resources`:

```bash
docker run -p 8080:8080 -v "$(pwd):/app" pinout.xyz
```

Set `PINOUT_LANG` to serve a language other than English:

```bash
docker run -p 8080:8080 -e PINOUT_LANG=de pinout.xyz
```

The image installs the builder, so the `pinoutxyz` command is on the path inside the container:

```bash
docker exec <container> pinoutxyz translations list
docker exec <container> pinoutxyz boards list
```

Optionally you can include a draft board in the image by setting the `PUBLISH_DRAFT` build argument:

```bash
docker build --build-arg PUBLISH_DRAFT=myboard -t pinout.xyz .
```

# Translating

Board metadata lives once, in `src/en/overlay`. A translation is an overlay on top of it: a file at `src/<languagecode>/overlay/<board>.md` holding only the text you have changed. Anything you leave out falls back to English, so a board with no file at all still gets a page in your language.

Only four things are yours to change: `name`, `description`, `page_url`, and the `name` of each pin or I2C device. A German translation of the Display-o-Tron is the whole of `src/de/overlay/display-o-tron.md`:

```markdown
<!--
---
description: Ein 3-zeiliges LCD mit RGB Hintergrundbeleuchtung und Joystick
pin:
  '7':
    name: Joystick Taste
  '11':
    name: Joystick links
-->
# Display-o-Tron 3000

Mit diesem Einzeiler installierst Du das Display-o-Tron 3000:
```

Pin numbers, modes, form factor, pin counts, images and links all come from English, and repeating them means they can drift. `pinoutxyz translations check` will tell you if you have copied something that isn't yours to change, and it runs in CI. Shop and documentation links are the one exception: you may point `url` or `buy` at a localised page of the same site.

If you would like to provide support for a language not yet in the repository, all you need is `src/<languagecode>/settings.yaml` with `language`, `locale` and `flag` set so the language switcher can label and flag it. Everything else falls back to English until you translate it: copy `template/localised.yaml`, `template/pinout.yaml`, `template/index.md`, `template/404.md`, `template/footer.html` and the files in `pin` out of `src/en` as and when you get to them. Note that there are no plans to support cultures (it would just get out of hand), so you can't have `src/fr-CA` (sorry!).

The flags in `resources/flags` come from [flag-icons](https://github.com/lipis/flag-icons); take the 4x3 SVG for your country and name it after the `flag` in your settings.

Please do not attempt to translate the `resources` folder, or anything not specifically mentioned in this section of the README - all files outside your *&lt;languagecode&gt;* directory are shared between the languages and are meant to be generic. Feel free to modify the template with links relevant to your country, and / or your own social handle however, but don't fiddle with the structure!

`pinoutxyz translations list` shows how much of each language is done and `pinoutxyz translations outstanding de` lists the boards with no German file at all. To build and preview your work:

```bash
make serve LANG=de
```

And then open: http://127.0.0.1:8080/de/ in your browser.

The last step will be to submit your finished translation as a [pull request](https://github.com/pinout-xyz/Pinout.xyz/pulls) (this can include any number of boards, it does not have to be the entire line-up) and we'll get it live at its own pinout.xyz/*&lt;languagecode&gt;*/ path.

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
