import asyncio
import logging
import os

import requests

log = logging.getLogger()
log.setLevel(logging.INFO)

console = logging.StreamHandler()
log.addHandler(console)

URL = 'https://api.thecatapi.com/v1/images/search'


async def get_response(url):
    return await loop.run_in_executor(None, requests.get, url)


async def download_cat(response, cat_id, cat_number):
    with open(f'cats/{cat_id}.png', 'wb') as file:
        file.write(response.content)
        log.info(f'Cat #{cat_number} is downloaded!')


async def get_cat_data(url, cat_number):
    response = await get_response(url)
    response_json = response.json()
    cat_url = response_json[0]['url']
    cat_id = response_json[0]['id']
    cat_response = await get_response(cat_url)

    log.info(f'Receiving data of cat #{cat_number}...')

    downloaded_cat = download_cat(response=cat_response,
                                  cat_id=cat_id,
                                  cat_number=cat_number)
    task = asyncio.create_task(downloaded_cat)
    await task


async def get_cats(amount: int, url: str):
    tasks = []

    for i in range(amount):
        cat_number = i + 1
        cat_data = get_cat_data(url=url, cat_number=cat_number)
        tasks.append(asyncio.create_task(cat_data))
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    if not os.path.exists('cats'):
        os.mkdir('cats')

    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_cats(amount=10, url=URL))
