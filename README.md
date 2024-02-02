# Skyscanner Scraper

Skyscanner Scraper is a Python script that allows you to scrape flight data from Skyscanner based on the URLs provided in a text file input and store the data in a CSV format.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## Features

- Scrapes flight data from Skyscanner based on input URLs.
- Stores the scraped data in a CSV file for easy analysis.
- Scraped data:
  - `Flight Number`: num_vuelo
  - `Departure Airport`: aeropuerto_salida
  - `Destination Airport`: aeropuerto_destino
  - `Layover Airport`: aeropuerto_escala
  - `Layover Time`: tiempo_escala
  - `Flight Date`: fecha_vuelo
  - `Departure Time`: hora_salida
  - `Arrival Time`: hora_llegada
  - `Search Date`: fecha_busqueda (current date and time)
  - `Search Year`: anyo_busqueda
  - `Search Month`: mes_busqueda
  - `Search Day of the Week`: dia_semana_busqueda
  - `Search Day of the Month`: dia_mes_busqueda
  - `Search Hour`: hora_busqueda
  - `Month Progress`: progreso_mes
  - `Week Progress`: progreso_semana
  - `Day Progress`: progreso_dia
  - `Price`: precio
  - `Seller`: vendedor



## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your machine.
- Python libraries: requests, BeautifulSoup, pandas (You can install them using `pip install -r requirements.txt`).

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/sainzunai/skyscanner_scraper.git

2. Change to the project directory:
   ```bash
   cd skyscanner_scraper

3. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt

## Usage

1. Create a text file (e.g., urls.txt) containing Skyscanner flight URLs, with each URL on a new line.
2. Run scrap_from_file.py
The script will start scraping the flight data and store it in the specified CSV file. You will see in real time how the scraper opens the browser and navigates through the page.
If interested, you can run the Jupyter Notebook file "data_analysis.ipynb" in order to generate price evolution graphs. Examples are included in the file.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or create a pull request.
