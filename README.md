# BikePoint_TFL

# BikePoint TfL Pipeline

A data pipeline project using **Python** to extract live bike station data from the **TFL Bike Point API**. It's being built in stages, starting with the extract step.

---

## Python Script: `extract.py`
- Calls the TFL Bike Point API to get real-time data on every bike docking station in London
- Saves the response as a timestamped `.json` file in `data/`
- Creates a log file for each run in `logs/`
- Retries up to 3 times if the API has a server error

---

## How to Run

```bash
pip install -r requirements.txt
python extract.py
```

No API key is needed.

---

## Roadmap

- [x] Extract data from the API
- [x] Add logging and retry handling
- [ ] Load into cloud storage
- [ ] Transform in Snowflake
- [ ] Automate on a schedule

---

## Folder Structure

```bash
.
├── data/              # JSON files (gitignored)
├── logs/              # Log files (gitignored)
├── extract.py         # Extract script
└── requirements.txt   # Dependencies
```
~~~

Copy everything inside the box and paste it straight into the README text box on GitHub.
