import asyncio
import json
import sys
from threads_api.src.threads_api import ThreadsAPI

async def fetch_threads(username: str, output: str):
    api = ThreadsAPI()
    user_id = await api.get_user_id_from_username(username)
    if not user_id:
        raise SystemExit(f"User '{username}' not found")
    threads = await api.get_user_threads(user_id)
    with open(output, 'w', encoding='utf-8') as f:
        json.dump(threads.dict(), f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python threads_scraper.py <username> [output_file]')
        raise SystemExit(1)
    username = sys.argv[1].lstrip('@')
    output = sys.argv[2] if len(sys.argv) > 2 else f'{username}_threads.json'
    asyncio.run(fetch_threads(username, output))

