from db.run_sql import run_sql
from models.artist import Artist

def save(artist):
    sql = "INSERT INTO artists (name, age) VALUES (%s, %s) RETURNING id"
    values = [artist.name, artist.age]
    
    results = run_sql(sql, values)
    
    id = results[0]['id']
    artist.id = id
    
    return artist

def delete(id):
    sql = "DELETE FROM artists WHERE id=%s"
    values = [id]
    run_sql(sql, values)

def select(id):
    sql = "SELECT * FROM artists WHERE id=%s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        artist = Artist(
            result['name'],
            result['age'],
            result['id']
        )
    return artist

def select_all():
    artists = []
    sql = "SELECT * FROM artists"
    results = run_sql(sql)
    
    for row in results:
        artist = Artist(
            row['name'],
            row['age'],
            row['id']
        )
        artists.append(artist)

def update(artist):
    sql = "UPDATE artists SET (name, age, id) = (%s, %s, %s) WHERE id = %s"
    values = [
        artist.name,
        artist.age,
        artist.id
    ]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM artists"
    run_sql(sql)