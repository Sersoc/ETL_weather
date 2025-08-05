create_table_wind = """
CREATE TABLE wind(
    speed REAL,
    direction REAL,
    east_prop REAL,
    south_prop REAL,
    time_id INTEGER,
    location_id INTEGER,
    FOREIGN KEY (time_id) REFERENCES logging_time(id),
    FOREIGN KEY (location_id) REFERENCES location(id),
    UNIQUE(time_id,location_id)
);
"""

create_table_temp = """
CREATE TABLE temp(
    temperature REAL,
    time_id INTEGER,
    location_id INTEGER,
    FOREIGN KEY (time_id) REFERENCES logging_time(id),
    FOREIGN KEY (location_id) REFERENCES location(id),
    UNIQUE(time_id,location_id)
);
"""

create_table_rain = """
CREATE TABLE rain(
    precipitation REAL,
    humidity REAL,
    pty_code INTEGER,
    time_id INTEGER,
    location_id INTEGER,
    FOREIGN KEY (time_id) REFERENCES logging_time(id),
    FOREIGN KEY (location_id) REFERENCES location(id),
    UNIQUE(time_id,location_id)
);
"""

create_table_location = """
CREATE TABLE location(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nx REAL,
    ny REAL,
    location_name TEXT
);
"""

create_table_logging_time = """
CREATE TABLE logging_time(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    time DATETIME
);
"""

insert_table_location = """
INSERT OR IGNORE INTO  location (nx,ny) VALUES (?,?);
"""
insert_table_loggin_time = """
INSERT OR IGNORE INTO logging_time (time) VALUES (?);
"""
