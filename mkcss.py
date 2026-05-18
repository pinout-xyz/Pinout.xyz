import sass

OUTPUT_FILE = "resources/pinout.scss.css"
INPUT_FILE = "resources/pinout.scss"

print(f"{INPUT_FILE} -> {OUTPUT_FILE}")

with open(OUTPUT_FILE, "w") as f:
    f.write(sass.compile(filename=INPUT_FILE, output_style="expanded"))

