import aiohttp

from configs.main_config import RapidAPI_Key


async def get_conf_for_gpt(arg: str) -> dict:
    """
    Запрос к rapid api
    """
    url = "https://chatgpt-api7.p.rapidapi.com/ask"
    payload = {
        "query": f'{arg}',
        "wordLimit": "4096"
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": RapidAPI_Key,
        "X-RapidAPI-Host": "chatgpt-api7.p.rapidapi.com"
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=payload, headers=headers) as response:
            result = await response.json()
    return result
