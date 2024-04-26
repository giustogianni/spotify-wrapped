DROP TABLE IF EXISTS spotify.stream;
DROP SCHEMA IF EXISTS spotify;
CREATE SCHEMA spotify;
CREATE TABLE spotify.stream (
    ts VARCHAR(50), 
    username VARCHAR(50), 
    platform VARCHAR, 
    ms_played INT, 
    conn_country VARCHAR(30),
    ip_addr_decrypted VARCHAR(20), 
    user_agent_decrypted VARCHAR,
    master_metadata_track_name VARCHAR,
    master_metadata_album_artist_name VARCHAR,
    master_metadata_album_album_name VARCHAR,
    spotify_track_uri VARCHAR, 
    episode_name VARCHAR,
    episode_show_name VARCHAR, 
    spotify_episode_uri VARCHAR, 
    reason_start VARCHAR(50),
    reason_end VARCHAR(50), 
    shuffle BOOLEAN, 
    skipped BOOLEAN, 
    offline BOOLEAN, 
    offline_timestamp BIGINT,
    incognito_mode BOOLEAN
);