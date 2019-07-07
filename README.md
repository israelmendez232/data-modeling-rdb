# PostgreSQL and Data Modeling RDS
##### [Israel Mendes](israelmendes.com.br)
This project has the purpose to make a data modeling by a Relational Data Systems. Using PostgresSQL and Python, I've  optimized for queries focused more in read and analysis for a business perspective.

---

## Table of Contents:
1. [Steps](#steps)
2. [Datasets](#datasets)
3. [Schema and Design](#schema-and-design)
4. [ETL](#etl)
5. [Validation](#validation)

---

## 1. Steps
The main steps to proceed in this proccess is:
- Design the schema of the data modeling;
- Create the tables at `create_tables.py`;
- Produce the main caracteristics in `sql_queries.py`;
- Populate the model with real data from the `etl.py` process;
- Validate the load process in `test.ipynb`.

## 2. Datasets
Before creating any data model, we need to understand better the data. Here is a sample from the **Song Dataset** from the [Million Song Dataset](http://millionsongdataset.com/):
> song_data/A/A/B/TRAABJL12903CDCF1A.json

> {"num_songs": 1, "artist_id": "ARJIE2Y1187B994AB7", "artist_latitude": null, "artist_longitude": null, "artist_location": "", "artist_name": "Line Renaud", "song_id": "SOUPIRU12A6D4FA1E1", "title": "Der Kleine Dompfaff", "duration": 152.92036, "year": 0}

And from the **Log Dataset** from this [Event Data Simulator](https://github.com/Interana/eventsim):
> log_data/2018/11/2018-11-13-events.json (first row)

> {"artist":null,"auth":"Logged In","firstName":"Kevin","gender":"M","itemInSession":0,"lastName":"Arellano","length":null,"level":"free","location":"Harrisburg-Carlisle, PA","method":"GET","page":"Home","registration":1540006905796.0,"sessionId":514,"song":null,"status":200,"ts":1542069417796,"userAgent":"\"Mozilla\/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/36.0.1985.125 Safari\/537.36\"","userId":"66"} ...

## 3. Schema and Design
The main option was to use a Star Schema to concentrate the data and to provide better solutions for reading while querying. The **Fact Table** selected is _songplays_ that contains: records in log data associated with song plays i.e. records with page `NextSong`.
| songplays | types of data |
| --- | --- |
| songplay_id | INT |
| start_time | TIME |
| user_id | VARCHAR |
| level | VARCHAR |
| song_id | VARCHAR |
| artist_id | VARCHAR |
| session_id | INT |
| location | VARCHAR |
| user_agent | VARCHAR |

The **Dimension Tables** are and the source of the data from:
- _users:_ users in the app;

| users | types of data |
| --- | --- |
| user_id | INT |
| first_name | VARCHAR |
| last_name | VARCHAR |
| gender | VARCHAR |
| level | VARCHAR |

- _songs:_ songs in music database;

| songs | types of data |
| --- | --- |
| song_id | VARCHAR |
| title | VARCHAR |
| artist_id | VARCHAR |
| year | INT |
| duration | DECIMAL |

- _time:_ timestamps of records in songplays broken down into specific units.

| time | types of data |
| --- | --- |
| start_time | TIME |
| hour | INT |
| day | INT |
| week | INT |
| month | INT |
| year | INT |
| weekday | INT |

- _artists:_ artists in music database;

| artists | types of data |
| --- | --- |
| artist_id | VARCHAR |
| name | VARCHAR |
| location | VARCHAR |
| latitude | VARCHAR |
| longitude | VARCHAR |

Here is visualy:

![Tables for the PostgreSQL and Data Modeling RDS Project - By Israel Mendes.](/images/tables.png "Tables for the PostgreSQL and Data Modeling RDS Project - By Israel Mendes.")

## 4. ETL
The Extract-Transform-Load process is simple, after all the work from reading the 

## 5. Validation
Using the `test.ipynb` notebook to read the top 5 rows from each table to validate all the ETL process.
