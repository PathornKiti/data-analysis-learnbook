# Interest tracks and data sources

Pick the track closest to your interests, or mix them. Each track has starter questions at three levels
(*describe → compare → relate/predict*) and places to look for data.

> Always **check the licence/terms** of any dataset, and don't republish data you aren't allowed to share. Websites change,
> so if a link has moved, search the site's name plus "data".

## Where to find data (general)

| source | good for |
|---|---|
| [Our World in Data](https://ourworldindata.org/) | health, energy, climate, economics: downloadable CSVs |
| [World Bank Open Data](https://data.worldbank.org/) | country indicators over decades |
| [Gapminder](https://www.gapminder.org/data/) | life expectancy, income, population |
| [FRED](https://fred.stlouisfed.org/) | economic time series (US-centric, plus many international) |
| [data.gov](https://data.gov/) and national/city open-data portals | local government data |
| [UCI Machine Learning Repository](https://archive.ics.uci.edu/) | classic, well-documented datasets |
| [Kaggle datasets](https://www.kaggle.com/datasets) | huge variety (check each licence) |
| [FiveThirtyEight data](https://github.com/fivethirtyeight/data) | sports, politics, culture: CSVs with write-ups |
| Seaborn sample data (`sns.load_dataset("penguins")`, `"tips"`, `"diamonds"`) | practice before your own data |
| [Open-Meteo](https://open-meteo.com/) | weather history via a free API |
| [NASA GISS Surface Temperature (GISTEMP)](https://data.giss.nasa.gov/gistemp/) | global temperature record |
| [WHO Global Health Observatory](https://www.who.int/data/gho) | global health indicators |
| [StatsBomb open data](https://github.com/statsbomb/open-data) | football (soccer) event data |

## Tracks

### ⚽ Sports
* *Describe:* What's the typical number of goals/points per game this season?
* *Compare:* Do home teams score more than away teams?
* *Relate/Predict:* How well do shots on target predict goals? Can we predict match outcomes from team stats?
* Data: FiveThirtyEight, StatsBomb open data, league sites (check terms before scraping).

### 💰 Personal finance & economics
* *Describe:* How have prices of a basket of goods changed since 2000?
* *Compare:* Do inflation and unemployment differ between two countries?
* *Relate/Predict:* Is there a relationship between interest rates and house prices?
* Data: FRED, World Bank, national statistics offices.

### 🩺 Health & fitness
* *Describe:* What's my typical sleep/step count? (export your own phone or watch data, and keep it private)
* *Compare:* Are weekends different from weekdays?
* *Relate:* Does sleep relate to resting heart rate?
* Data: WHO GHO, Our World in Data, your own exports.

### 🌍 Climate & environment
* *Describe:* What's the long-run trend in annual temperature for my region?
* *Compare:* Are summers getting hotter faster than winters?
* *Relate/Predict:* How do rainfall and temperature relate to air-quality readings?
* Data: NASA GISTEMP, Open-Meteo, national weather agencies, city air-quality portals.

### 🎵 Music & media
* *Describe:* What do the top charts look like by genre?
* *Compare:* Are songs from different decades different in tempo or energy?
* *Predict:* Which audio features predict popularity?
* Data: Kaggle music datasets (check licences), Last.fm / MusicBrainz APIs (read their terms).

### 🎮 Games
* *Describe:* What's the distribution of player ratings or completion times?
* *Compare:* Do different characters/classes win at different rates?
* *Predict:* Can early-game stats predict who wins?
* Data: Kaggle game datasets, public game APIs, your own match history exports.

### 🏙️ Cities & society
* *Describe:* Where and when do bike-share trips happen?
* *Compare:* Do neighbourhoods differ in 311 complaint types?
* *Relate:* How do transport use and weather relate?
* Data: your city's open-data portal, national statistics, survey data (e.g. World Values Survey).

### 📚 Education & surveys
* *Describe:* What do respondents say about X?
* *Compare:* Do groups answer differently?
* *Relate:* Which survey items move together?
* Data: UCI, open survey data, or run **your own small survey** (get consent; keep it anonymous).

## Choosing well: a checklist
- [ ] I'm curious about the answer
- [ ] ≥ a few hundred rows and ≥ 5 columns
- [ ] a mix of numeric and categorical columns
- [ ] I'm allowed to use it and know its licence
- [ ] a missing value or two (realistic!), but not a disaster
