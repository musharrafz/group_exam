from config import *
from func import *
from db import update_data, get_info_from_db


@app.on_message(filters.command(commands=['refresh'], prefixes='%'))
async def refresh(client, message: Message):
    update_data(await get_insertable_data())
    await message.reply('refresh tayyor ✅ ')


@app.on_message(filters.regex(r"^\%\d+$"))
async def search_groups(client, message: Message):
    lst = []
    for i in get_info_from_db(int(message.text[1:])):
        url = (await app.get_chat(i[-2])).invite_link
        lst.append(f"[{i[-1]}]({url})")
    await message.reply("\n".join(lst))


app.run()
