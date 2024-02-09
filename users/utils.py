from django.contrib.auth.models import auth
from django.contrib.auth.models import Group

def find_spammer_group():
    '''уточняем под каким номером создана группа доступа spammer'''
    auth_group_list = Group.objects.all()
    #print(auth_group_list)  #для отладки
    for item in auth_group_list:
        if item.name == 'spammer':
            return item.id

    # spammer_group = Group.objects.filter(name='spammer')
    # print(spammer_group)  # для отладки
    # return spammer_group
