from configs.main_config import RapidAPI_Key


async def get_conf_for_gpt(arg: str) -> dict:
    """
    Возвращает конфиги для chatgpt-api от rapid-api
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
    return url, payload, headers

