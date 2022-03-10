import asyncio
import logging
import os

import requests

log = logging.getLogger()
log.setLevel(logging.INFO)

console = logging.StreamHandler()
log.addHandler(console)

URL = 'https://api.thecatapi.com/v1/images/search'


async def download_cat(res, cat_id, cat_number):
    response = await res

    with open(f'cats/{cat_id}.png', 'wb') as file:
        file.write(response.content)
        log.info(f'Cat #{cat_number + 1} is downloaded!')


async def get_cat_data(res, cat_number):
    response = await res
    response_json = response.json()
    cat_url = response_json[0]['url']
    cat_id = response_json[0]['id']

    log.info(f'Receiving data of cat #{cat_number + 1}...')

    task = asyncio.create_task(
        download_cat(
            res=loop.run_in_executor(None, requests.get, cat_url),
            cat_id=cat_id,
            cat_number=cat_number
        )
    )
    await task


async def get_cats(amount):
    tasks = []

    for cat_number in range(amount):
        tasks.append(
            asyncio.create_task(
                get_cat_data(
                    res=loop.run_in_executor(None, requests.get, URL),
                    cat_number=cat_number
                )
            )
        )
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    if not os.path.exists('cats'):
        os.mkdir('cats')

    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_cats(10))
