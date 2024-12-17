class Album:
    def __init__(self, id, title, user_id):
        self.id = id
        self.title = title
        self.user_id = user_id 

    def __repr__(self):
        return f"Album(ID={self.id}, Title={self.title}, User_ID={self.user_id})"

class Photo:
    def __init__(self, id, title, url, thumbnail_url, album_id):
        self.id = id
        self.title = title
        self.url = url
        self.thumbnail_url = thumbnail_url
        self.album_id = album_id

    def __repr__(self):
        return f"Photo(ID={self.id}, Title={self.title}, URL={self.url}, Thumbnail_URL={self.thumbnail_url}, Album_ID={self.album_id})"

# Archivo: modelos.py
class BaseModel:
    def __init__(self, id=None, **kwargs):
        self.id = id
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dict(self):
        """Convierte el objeto en un diccionario para enviarlo a la API."""
        return self.__dict__

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"


class Album(BaseModel):
    def __init__(self, id=None, title=None, user_id=None):
        super().__init__(id=id, title=title, user_id=user_id)


class Photo(BaseModel):
    def __init__(self, id=None, title=None, url=None, thumbnail_url=None, album_id=None):
        super().__init__(id=id, title=title, url=url, thumbnail_url=thumbnail_url, album_id=album_id)


