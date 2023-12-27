import os
import asyncio
import aiohttp
import httpx
import json
import requests


class FileManager:
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode

    def __enter__(self):
        file = open(file=self.path, mode=self.mode)
        self.file = file
        return file

    def __exit__(self, *args, **kwargs):
        self.file.close()


if __name__ == '__main__':
    fruits = []

    for file in os.listdir(f'C:/Users/Sarvar/PycharmProjects/python5thmonth/exam5thmonth/descriptions'):
        data = {}
        file_data = []

        for line in FileManager(f'C:/Users/Sarvar/PycharmProjects/python5thmonth/exam5thmonth/descriptions{file}', 'r'):
            file_data = line.split("\n")
            data["name"] = file_data[0]
            data["price"] = int(file_data[1].split()[0])
            data["description"] = file_data[2]
            fruits.append(data)
        print(fruits)

    url = "http://164.92.64.76/desc/"
    response = requests.post(url).json()
    with FileManager('response.txt', 'w') as f:
        json.dump(response, f, indent=4)


async def send_request(url, client: aiohttp.ClientSession):
    response = await client.post(url)
    print("Status code", response.status_code)
