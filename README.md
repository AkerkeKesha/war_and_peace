##War and Peace: Master Thesis
Master Thesis on analysis of Tolstoy work: War and Peace.
Goal: detect passages about enemy and identify sentiments against/for the enemy.

#### Setup Local Environment

1 - Get this repo
```bash
git clone git@github.com:AkerkeKesha/war_and_peace.git
cd war_and_peace
```

2 - Create virtual environment and activate it, while in the project directory:
```bash
python3 -m venv .venv
source .venv/bin/activate
```
3 - Install packages into .venv
```bash
pip install -r requirements.txt
```
4 - Run tests
```bash
pytest
```

#### Clone and setup Bleualign lib in order to align original with translations
5 - Clone and setup Bleualign into project directory 
```bash
git clone https://github.com/rsennrich/Bleualign.git
python3 ./Bleaualign/setup.py install

```
6 - Run some sample to check it works
```bash
./Bleualign/bleualign.py -s sourcetext.txt -t targettext.txt --srctotarget sourcetranslation.txt -o outputfile
```
7 - Run actual 
```bash
./Bleualign/bleualign.py -s ./data/0.tolstoy.txt -t ./data/5.maude.txt --srctotarget ./data/tolstoy_translated.txt -o outputfile
```
I had fix manually the French text:
```bash
./Bleualign/bleualign.py -s ./data/0.tolstoy.txt -t ./data/5.maude.txt --srctotarget ./data/manually_fixed.txt -o ./data/secondtrial
```


#### Clone and setup GROBID lib in order to identify footnotes, text, etc
in a separate terminal window, run GROBID service:

```bash
./gradlew run
```

```bash
grobid_client --input ./raw_data/0.tolstoy processFulltextDocument
```


```bash
pip install -U pip setuptools wheel
pip install -U spacy
python -m spacy download en_core_web_sm
python -m spacy download fr_core_news_sm
python -m spacy download ru_core_news_sm
```


##### References:
- [Bleualign](https://github.com/rsennrich/Bleualign)
- [GROBID](https://github.com/kermitt2/grobid_client_python)
