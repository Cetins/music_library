from db.run_sql import run_sql
from models.artist import Artist

def save(artist):
    sql = "INSERT INTO artists (name, age) VALUES (%s, %s) RETURNING id"
    values = [artist.name, artist.age]
    
    results = run_sql(sql, values)
    
    id = results[0]['id']
    artist.id = id
    
    return artist

def delete(artist):
    pass

def select(id):
    pass

def select_all():
    pass

def update():
    pass

def delete_all():
    pass