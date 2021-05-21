import vk
from modules.module_sql import write_info
from pprint import pprint
from datetime import date


ACCESS_TOKEN = input('Введите токен: ')
session = vk.Session(access_token=ACCESS_TOKEN)
vk_api = vk.API(session)


def get_groups_list():
    with open('groups.txt', 'r') as f:
        groups_list = [line.strip().split('/')[1] for line in f]
        return groups_list


def get_groups_info(vk_api):
    groups_list = ', '.join(get_groups_list())
    groups_by_id = vk_api.groups.getById(
        v='5.90', 
        group_ids=groups_list, 
        fields='members_count')
    return groups_by_id


def make_list(vk_api):
    today = date.today()
    row = []
    for group in get_groups_info(vk_api):
        result = (today.strftime("%m/%d/%Y"), group['id'], group['name'], group['screen_name'], group['members_count'])
        row.append(result)
    return row


def write_to_db():
    vk_api = vk.API(session)
    groups_info = make_list(vk_api)
    write_info(groups_info)