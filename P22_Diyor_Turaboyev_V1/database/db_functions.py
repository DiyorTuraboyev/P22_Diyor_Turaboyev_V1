from const import r
from datetime import datetime


def set_users_to_redis(user_id: str, name: str):
    date_time = str(datetime.now())
    date = date_time[:11]
    hour = date_time[11:16]
    user = {"name": name, "registered_date": date, "registered_time": hour}
    key = f"user_id={user_id}"
    r.hset(name=key, mapping=user)


def get_user_date(user_id):
    key = f"user_id={user_id}"
    data = r.hgetall(name=key)
    if data:
        decoded_data = {k.decode('utf-8'): v.decode('utf-8') for k, v in data.items()}
        return decoded_data
    else:
        return False


def get_all_user_ids():
    keys = r.keys('user_id=*')
    decoded_keys = [i.decode('utf-8') for i in keys]
    user_ids = []
    for user_id in decoded_keys:
        user_ids.append(user_id[8:])
    return user_ids

