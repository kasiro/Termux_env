import re
from datetime import date, datetime
from telethon import TelegramClient
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
from file_ import ff, _
from sys import exit
from pprint import pp

# Введите свои данные
api_id = 1964745
api_hash = '2d66ab73d2dbb39b00b27595c1f8b7b6'
phone_number = '89137759910'


client = TelegramClient('Kasiro', api_id, api_hash)

def expire(exp_date: str) -> bool:
    exp_date = _(exp_date).dict_replace({
        '\n': '', '\\n': ''
    })
    current_year = str(datetime.now().year)
    exp_date += f'.{current_year}'
    target_date = datetime.strptime(exp_date, '%d.%m.%Y').date()
    if target_date < date.today() or target_date == date.today():
        return True
    return False

# async def unsubscribe():
#     return await client.delete_dialog()

async def is_subscribe(channel: str) -> bool:
    try:
        e_ = await client.get_entity(channel)
    except ValueError:
        return False
    return not e_.left # type: ignore

async def main_():
    ...
    

async def main():
    # await client.start(phone_number) # type: ignore
    dialogs = await client.get_dialogs()
    
    l = 0 # noqa
    for line in ff('./last.txt').iter():
        name, date_ = line.split(': ')
        if name.startswith('@'):
            name = name[1:]

        l += 1 # noqa
        if expire(date_):
            entity_ = await client.get_entity(name)
            # await client.delete_dialog(entity_.entity.id)
            print('deleted: %s' % entity_.username) # type: ignore
            ff('./last.txt').deleteLine(l)
    print('channel count: %s' % len(dialogs))

with client:
    client.loop.run_until_complete(
        main_()
    )
