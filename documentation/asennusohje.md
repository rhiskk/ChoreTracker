# Asennusohje

## Asennus paikallisesti

- Asenna koneellesi Python3, mikäli sitä ei ole vielä asennettuna

- Lataa projekti koneellesi painamalla repositoriossa _Clone or download_ -nappia. Valitse sitten _Download ZIP_. Tämän jälkeen pura ladattu tiedosto koneellesi.

- Mene terminaalissa kansioon, johon purit tiedoston ja siirry ohjelman kansioon komennolla `cd ChoreTracker`

- Luo virtuaaliympäristö komennolla `python3 -m venv venv` ja aktivoi se komennolla `source venv/bin/activate`

- Asenna sovelluksen vaatimat riippuvuudet komennolla `pip install -r requirements.txt`

## Sovellus toimimaan Herokussa

- Asenna ohjelma paikallisesti

- Luo Herokun käyttäjätunnus, mikäli sinulla ei vielä ole sellaista

- Asenna Herokun työvälineet komentoriville ([Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)), mikäli niitä ei ole vielä asennettuna

- Siirry terminaalissa ohjelman kansioon ja aktivoi virtuaaliympäristö komennolla `source venv/bin/activate` 

- Luo sovellukselle paikka Herokuun komennolla `heroku create`, jota seuraa sovellukselle haluttu nimi

- Lisää paikalliseen versiohallintaan tieto Herokusta komennolla `git remote add heroku https://git.heroku.com/`__sovelluksen nimi__`.git`

- Lähetä projekti Herokuun suorittamalla komennot

  `git add .`

  `git commit -m "Initial commit"`

  `git push heroku master`
  
 - Lisää sovelluksen käyttöön tieto, etää sovellus on Herokussa komennolla `heroku config:set HEROKU=1`
 
 - Lisää Herokuun tietokanta komennolla `heroku addons:add heroku-postgresql:hobby-dev`
 
 
 
