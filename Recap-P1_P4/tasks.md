## Scenario: 

- **You have been hired as the Data Engineer for a new music streaming startup called "Streamify".**

- **The CEO has given you a blank canvas.** 

- **Your job is to design the database from scratch and then write the analytics queries to help the company grow.**

---


## Part 1: Schema Design

`Task`: Write the DDL (CREATE TABLE) statements for these 4 tables. Ensure they are Normalized (3NF) and include appropriate Data Types and Constraints.


1. **users**

    - `user_id` (PK)

    - `email` (Unique, required)

    - `subscription_plan` (Must be 'Free', 'Premium', or 'Family')

    - `country` (2-letter code, e.g., 'US', 'FR')

2. **artists**

    - `artist_id` (PK)

    - `name` (Required)

    - `genre` (Text)

3. **songs**

    - `song_id` (PK)

    - `artist_id` (FK)

    - `title` (Required)

    - `duration_seconds` (Integer, must be positive)

    - `release_date` (Date)

4. **streams**

    - `stream_id` (PK)

    - `user_id` (FK)

    - `song_id` (FK)

    - `stream_date` (Timestamp, default Now)

    - `device_type` (Text)

---

## Part 2: The Builder

`Task:` Write the SQL for the following operations.

**The Seed Data:** Write INSERT statements to add:

- 2 Artists ("The Weeknd", "Daft Punk").

- 3 Songs (linked to those artists).

- 2 Users.

**The Safe Update:**

- Start a Transaction.

- Update a user's subscription from 'Free' to 'Premium'.

- Commit the change.

**The Upsert:**

- Try to insert a new user with email ceo@streamify.com.

- If that email already exists, do nothing (preserve the existing row).

---

## Part 3: The Analyst

**Task:** Write the queries to answer these business questions.

`The "Top Charts":`

- Find the Top 3 Songs by total play count. Display the Song Title, Artist Name, and Play Count.

- `The "Binge Listener"`:

- We want to find users who listen to music non-stop.

- For User ID 1, list their streams. Add a column called gap_seconds that shows the time difference (in seconds) between their current stream and their previous stream.

`The "Global Reach"`:

- Calculate the total number of streams per Country.

`The "Artist Growth"` :

- **Challenge:** Calculate the Running Total of streams for "The Weeknd", ordered by date.

- **Show:** stream_date, song_title, and cumulative_streams.

---