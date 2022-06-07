import pdb

from models.artist import Artist
from models.album import Album
import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repositories

artist_repository.delete_all()
album_repositories.delete_all()

artist_1 = Artist("Beyonce", 40)
artist_repository.save(artist_1)

artist_2 = Artist("Jennifer Lopez", 52)
artist_repository.save(artist_2)

artist_3 = Artist("Alicia Keys", 41)
artist_repository.save(artist_3)

artist_repository.delete(22)

pdb.set_trace()