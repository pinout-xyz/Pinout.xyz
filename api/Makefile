all: directories images json md

directories:
	mkdir -p v1/detail
	mkdir -p v1/md
	mkdir -p v1/img

images:
	./mkimages.py

json:
	./mkindexjson.py > v1/index.json
	./mkjson.py

md:
	cp ../src/en/overlay/*.md v1/md

clean:
	rm -rf v1
	rm -rf img