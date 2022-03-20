# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
# 빈 인벤토리 리스트를 작성해서 append 받을 수 있게 한다.
inven_list = []

def inventory_filter(item_type, inventory):
    # 인벤토리의 길이만큼 반복하는 반복문을 작성한다.
    for i in range(len(inventory)):
        # 아이템 타입이 인벤토리 안에 있는지 확인한다. 이 때, i번째의 type에 있는지 개별적으로 확인한다.
        if item_type in inventory[i]['type']:
            # i번째 인벤토리의 값을 모두 inven_list에 append 한다.
            inven_list.append(inventory[i])
    # 만들어진 inven_list를 리턴한다.
    return inven_list



# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    item_type = 'weapon'
    inventory = [
        {
            'id': 1,
            'name': 'Elder Wand',
            'type': 'weapon',
            'grade': 'legend',
        },
        {
            'id': 2,
            'name': 'Healing Potion',
            'type': 'potion',
            'grade': 'normal',
        },
        {
            'id': 3,
            'name': 'Steel Helmet',
            'type': 'armor',
            'grade': 'rare',
        },
        {
            'id': 4,
            'name': 'Long Sword',
            'type': 'weapon',
            'grade': 'normal',
        },
    ]
    print(inventory_filter(item_type, inventory)) 
    # [{'id': 1, 'name': 'Elder Wand', 'type': 'weapon', 'grade': 'legend'}, {'id': 4, 'name': 'Long Sword', 'type': 'weapon', 'grade': 'normal'}]
