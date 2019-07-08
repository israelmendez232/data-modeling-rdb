# PostgreSQL and Data Modeling RDS
##### [Israel Mendes](israelmendes.com.br)
This project has the purpose to make data modeling by Relational Data Systems. Using PostgreSQL and Python, I've optimized for queries focused more on reading and analysis for a business perspective.

---

## Table of Contents:
1. [Steps](#steps)
2. [Datasets](#datasets)
3. [Schema and Design](#schema-and-design)
4. [ETL](#etl)
5. [Validation](#validation)

---

## 1. Steps
The main steps to proceed in this process is:
- Design the schema of the data modeling;
- Create the tables at `create_tables.py`;
- Produce the main characteristics in `sql_queries.py`;
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
The main option was to use a Star Schema to concentrate the data and to provide better solutions for reading while querying. The **Fact Table** selected is:
- _songplays:_ that contains the records in log data associated with song plays i.e. records with page `NextSong`.

The **Dimension Tables** are and the source of the data from:
- _users:_ users in the app;
- _songs:_ songs in music database;
- _time:_ timestamps of records in songplays broken down into specific units.
- _artists:_ artists in music database;

Here is visually:

![Tables for the PostgreSQL and Data Modeling RDS Project - By Israel Mendes.](/images/tables.png "Tables for the PostgreSQL and Data Modeling RDS Project - By Israel Mendes.")

## 4. ETL
After all the work of creating the model and the tables, it's time to populate them. I used an Extract-Transform-Load process is at `etl.py` to pull the data from `data\log_data` and `data\song_data`. Remembering that the information it's in JSON format. 

## 5. Validation
Using ETL and pulling the data, I used the `test.ipynb` notebook to read the top 5 rows from each table to validate all the process. You can check it the [results here]().
