-- Part 1 : Schema Design


-- user table
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    email TEXT UNIQUE NOT NULL,
    subscription_plan TEXT CHECK (subscription_plan in ('Free', 'Premium', 'Family')),
    country VARCHAR(2)
);

-- artists table
CREATE TABLE artists (
    artist_id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    genre TEXT
);

-- songs table
CREATE TABLE songs (
    song_id SERIAL PRIMARY KEY,
    artist_id INT REFERENCES artists(artist_id),
    title TEXT NOT NULL,
    duration_seconds INTEGER CHECK (duration_seconds > 0),
    release_date DATE
);

-- streams table
CREATE TABLE streams (
    stream_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id),
    song_id INT REFERENCES songs(song_id),
    stream_date TIMESTAMP DEFAULT NOW(),
    device_type TEXT
);

-- Part 2 : Builder

INSERT INTO artists (name, genre) VALUE ('The Weeknd', 'Pop'), ('Daft Punk', 'Electro');

INSERT INTO songs (artist_id, title, duration_seconds, release_date) VALUES (1, 'Blinding Lights', 204, '2020-08-23'), (1, 'Save your tears', 217, '2020-08-22'), (1, 'Call out my name', 229, '2018-02-26'), (2, 'Get lucky', 249, '2013-06-10'), (2, 'Instant crush', 340, '2013-06-13'), (2, 'I feel it coming', 298, '2016-02-12');

INSERT INTO users (email, subscription_plan, country) VALUES ('ceo@streamify.com', 'Family', 'MG'), ('cto@streamify.com', 'Free', 'FR');

BEGIN;
UPDATE user
SET subscription_plan = 'Premium'
WHERE user_id = 2;
COMMIT;

BEGIN;
INSERT INTO users (email, subscription_plan, country) VALUES ('ceo@streamify.com', 'Premium', 'GB')
ON CONFLICT (email) 
DO NOTHING;


-- Part 3 : The Analyst

-- Top 3 songs
SELECT 
    s.title,
    a.name AS artist_name,
    COUNT(st.stream_id) AS play_count
FROM streams st
JOIN songs s ON st.song_id = s.song_id
JOIN artists a ON s.artist_id = a.artist_id
GROUP BY s.title, a.name
ORDER BY play_count DESC
LIMIT 3;

-- The "Binge Listener"
SELECT 
    user_id,
    stream_date,
    EXTRACT(EPOCH FROM (stream_date - LAG(stream_date) OVER (PARTITION BY user_id ORDER BY stream_date))) as gap_seconds
FROM streams
WHERE user_id = 1;

-- The "Global reach"
SELECT 
    u.country,
    COUNT(st.stream_id) as total_streams
FROM streams st
JOIN users u ON st.user_id = u.user_id
GROUP BY u.country;


-- The "Artist Growth"

SELECT 
    st.stream_date,
    s.title,
    COUNT(st.stream_id) OVER (ORDER BY st.stream_date) as cumulative_streams
FROM streams st
JOIN songs s ON st.song_id = s.song_id
JOIN artists a ON s.artist_id = a.artist_id
WHERE a.name = 'The Weeknd'
ORDER BY st.stream_date;
