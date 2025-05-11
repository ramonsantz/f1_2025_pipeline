DROP TABLE IF EXISTS drivers;

CREATE TABLE drivers(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL
);

DROP TABLE IF EXISTS race_results;

CREATE TABLE race_results(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    track TEXT,
    driver_id INTEGER,
    team TEXT,
    position INTEGER,
    no INTEGER,
    starting_grid INTEGER,
    laps INTEGER,
    time_retired TEXT,
    points REAL,
    set_fastest_lap TEXT,
    fastest_lap_time TEXT,
    position_gain INTEGER,
    FOREIGN KEY(driver_id) REFERENCES drivers(id)
);

DROP TABLE IF EXISTS fastest_laps;

CREATE TABLE fastest_laps (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    grand_prix TEXT,
    driver_id INTEGER,
    driver_abbreviation TEXT,
    car TEXT,
    time TEXT,
    FOREIGN KEY(driver_id) REFERENCES drivers(id)
);
