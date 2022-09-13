from typing import Optional

import httpx

from models.movie_model import MovieModel

from os.path import abspath
path_cacert_file = abspath('certs/cacert_companyCAchain.pem')
print(path_cacert_file)


async def get_movie(title_subtext: str) -> Optional[MovieModel]:
    url = f'https://movieservice.talkpython.fm/api/search/{title_subtext}'

    async with httpx.AsyncClient(verify=path_cacert_file) as client:
        resp: httpx.Response = await client.get(url)
        resp.raise_for_status()

        data = resp.json()

    results = data['hits']
    if not results:
        return None

    movie = MovieModel(**results[0])
    return movie
