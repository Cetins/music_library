from db.run_sql import run_sql
from models.album import Album
from models.artist import Artist

def save(album):
    sql = "INSERT INTO albums (title, year, artist_id) VALUES (%s, %s, %s) RETURNING id"
    values = [
        album.title,
        album.year,
        album.artist_id
    ]
    
    results = run_sql(sql, values)
    
    id = results[0]['id']
    album.id = id
    
    return album

def delete(id):
    sql = "DELETE FROM albums WHERE id=%s"
    values = [id]
    run_sql(sql, values)

def select(id):
    sql = "SELECT * FROM albums WHERE id=%s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        album = Album(
            result['title'],
            result['year'],
            result['artist_id'],
            result['id']
        )
    return album

def select_all():
    albums = []
    sql = "SELECT * FROM albums"
    results = run_sql(sql)
    
    for row in results:
        album = Album(
            row['title'],
            row['year'],
            row['artist_id'],
            row['id']
        )
        albums.append(album)
        
    return albums

def update(album):
    sql = "UPDATE albums SET (title, year, artist_id, id) = (%s, %s, %s, %s) WHERE id=%s"
    values = [
        album.title,
        album.year,
        album.artist_id,
        album.id
    ]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)

def select_by_artist(artist):
    albums = []
    sql = "SELECT * FROM albums WHERE artist_id=%s"
    values = [artist.id]
    
    results = run_sql(sql, values)
    
    for row in results:
        album = Album(
            row['title'],
            row['year'],
            row['artist_id'],
            row['id']
        )
        albums.append(album)
        
    return albums