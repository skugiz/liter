SOURCES=sources/liter.glyphs scripts/build-family.py
FAMILY=$(shell python3 scripts/read-config.py --family )
DRAWBOT_SCRIPTS=$(wildcard documentation/*.py)
DRAWBOT_OUTPUT=$(DRAWBOT_SCRIPTS:.py=.png)

help:
	@echo "###"
	@echo "# Build targets for $(FAMILY)"
	@echo "###"
	@echo
	@echo "  make build:  Builds the fonts and places them in the fonts/ directory"
	@echo "  make test:   Tests the fonts with fontbakery"
	@echo "  make proof:  Creates HTML proof documents in the proof/ directory"
	@echo "  make images: Creates PNG specimen images in the documentation/ directory"
	@echo

build: build.stamp

venv: venv/touchfile

venv-test: venv-test/touchfile

customize: venv
	. venv/bin/activate; python3 scripts/customize.py

build.stamp: venv/touchfile sources/config.yaml $(SOURCES)
	venv/bin/python scripts/build-family.py
	touch build.stamp

venv/touchfile: requirements.txt requirements.in
	test -d venv || python3 -m venv venv
	venv/bin/python -m pip install -r requirements.txt
	touch venv/touchfile

venv-test/touchfile: requirements-test.txt requirements-test.in
	test -d venv-test || python3 -m venv venv-test
	venv-test/bin/python -m pip install -r requirements-test.txt
	touch venv-test/touchfile

test: venv-test build.stamp
	venv-test/bin/python scripts/validate-family.py
	mkdir -p out/fontbakery
	venv-test/bin/fontbakery check-universal fonts/ttf/*.ttf -l WARN --succinct --json out/fontbakery/static.json --html out/fontbakery/static.html
	venv-test/bin/fontbakery check-universal 'fonts/variable/Liter[wght].ttf' -l WARN --succinct --badges out/badges --json out/fontbakery/variable.json --html out/fontbakery/fontbakery-report.html

proof: venv build.stamp
	venv/bin/python scripts/proof-family.py

images: venv $(DRAWBOT_OUTPUT)

%.png: %.py build.stamp
	. venv/bin/activate; python3 $< --output $@

clean:
	rm -rf venv
	find . -name "*.pyc" -delete

update-project-template:
	npx update-template https://github.com/googlefonts/googlefonts-project-template/

update: venv venv-test
	venv/bin/pip install --upgrade pip-tools
	# See https://pip-tools.readthedocs.io/en/latest/#a-note-on-resolvers for
	# the `--resolver` flag below.
	venv/bin/pip-compile --upgrade --verbose --resolver=backtracking requirements.in
	venv/bin/pip-sync requirements.txt

	venv-test/bin/pip install --upgrade pip-tools
	venv-test/bin/pip-compile --upgrade --verbose --resolver=backtracking requirements-test.in
	venv-test/bin/pip-sync requirements-test.txt

	git commit -m "Update requirements" requirements.txt requirements-test.txt
	git push
