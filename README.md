# Spotify Wrapped
Stream history wrapped. Play it ▶️

## Quick start
Start the services
```console
docker compose --env-file env up --build -d
```

Load data to Postgres
```console
docker exec -ti loader bash
python load_stream_data.py
```

Query database
```console
docker exec -ti warehouse bash
psql -U <user> -d <dbname> -c 'select * from spotify.stream limit 10'
```

Stop the application
```console
docker compose --env-file env down
```