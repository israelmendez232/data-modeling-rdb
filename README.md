# PostgreSQL and Data Modeling RDS
###### [Israel Mendes](israelmendes.com.br)
This project has the purpose to make a data modeling by a Relational Data Systems. Using PostgresSQL and Python, I've  optimized for queries focused more in read and analysis for a business perspective.

---

## Table of Contents:
1. [Schema and Design](#schema-and-design)
2. [Steps](#steps)
3. [ETL](#etl)
4. 
5. 
6. 

## 1. Schema and Design
The main option was to use a Star Schema to concentrate the data and to provide better solutions for reading while querying. The **Fact Table** selected is _songplays_ that contains: records in log data associated with song plays i.e. records with page `NextSong`.
| songplays | types of data |
| --- | --- |
| songplay_id | INT |
| start_time | VARCHAR PRIMARY KEY |
| user_id | VARCHAR PRIMARY KEY |
| level | VARCHAR PRIMARY KEY |
| song_id | VARCHAR PRIMARY KEY |
| artist_id | VARCHAR PRIMARY KEY |
| session_id | VARCHAR PRIMARY KEY |
| location | VARCHAR PRIMARY KEY |
| user_agent | VARCHAR PRIMARY KEY |

The **Dimension Tables** are and the source of the data from:
- _users:_ users in the app;

| users | types of data |
| --- | --- |
| user_id | INT |
| first_name | VARCHAR PRIMARY KEY |
| last_name | VARCHAR PRIMARY KEY |
| gender | VARCHAR PRIMARY KEY |
| level | VARCHAR PRIMARY KEY |

- _songs:_ songs in music database;

| songs | types of data |
| --- | --- |
| song_id | INT |
| title | VARCHAR PRIMARY KEY |
| artist_id | VARCHAR PRIMARY KEY |
| year | VARCHAR PRIMARY KEY |
| duration | VARCHAR PRIMARY KEY |

- _artists:_ artists in music database;

| artists | types of data |
| --- | --- |
| artist_id | INT |
| name | VARCHAR PRIMARY KEY |
| location | VARCHAR PRIMARY KEY |
| latitude | VARCHAR PRIMARY KEY |
| longitude | VARCHAR PRIMARY KEY |
| artist_id | VARCHAR PRIMARY KEY |
| session_id | VARCHAR PRIMARY KEY |
| location | VARCHAR PRIMARY KEY |
| user_agent | VARCHAR PRIMARY KEY |

- _time:_ timestamps of records in songplays broken down into specific units.

| time | types of data |
| --- | --- |
| start_time | INT |
| hour | VARCHAR PRIMARY KEY |
| day | VARCHAR PRIMARY KEY |
| week | VARCHAR PRIMARY KEY |
| month | VARCHAR PRIMARY KEY |
| year | VARCHAR PRIMARY KEY |
| weekday | VARCHAR PRIMARY KEY |

Here is visualy:

![Tables for the PostgreSQL and Data Modeling RDS Project - By Israel Mendes.](/images/tables.png "Tables for the PostgreSQL and Data Modeling RDS Project - By Israel Mendes.")

## Steps

# ETL

