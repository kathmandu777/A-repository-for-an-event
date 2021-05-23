from pprint import pprint


def main():
    restaurants = []
    while True:  # データ入力
        data = input()
        if(data == ""):
            break
        name, id, lunch, dinner, want_to_go, has_private_room, has_counter, can_smoke, can_use_paypay = data.split(
            ",")
        restaurant = {
            "name": name,
            "id": id,
            "lunch": int(lunch),
            "dinner": int(dinner),
            "want_to_go": int(want_to_go),
            "has_private_room": True if int(has_private_room) == 1 else False,
            "has_counter": True if int(has_counter) == 1 else False,
            "can_smoke": True if int(can_smoke) == 1 else False,
            "can_use_paypay": True if int(can_use_paypay) == 1 else False,
        }
        restaurants.append(restaurant)
    # paypay使用不可の店を排除
    searched_restaurants = [
        dic for dic in restaurants if dic["can_use_paypay"] == True]
    # 行きたい数でソート
    sorted_restaurants = sorted(
        searched_restaurants, key=lambda x: x["want_to_go"], reverse=True)

    pprint(sorted_restaurants)


if __name__ == "__main__":
    main()

"""
うどん 丸香, 100000000614, 1000, 2500, 198, 0, 1, 0, 1
つじ半, 100000729115, 1000, 2000, 240, 0, 1, 0, 1
ほんだ, 100000785336, 1500, 5000, 285, 1, 1, 1, 1
あなご屋 銀座ひらい, 100000821612, 2000, 5000, 290, 1, 0, 1, 1
かあさん 新宿駅前店, 100000093866, 1000, 3000, 265, 0, 1, 1, 1
いいおか 潮騒ホテルレストラン, 100001510561, 2000, 4000, 212, 1, 1, 1, 1
おきなわ家, 100000949764, 1000, 3000, 232, 1, 1, 1, 0
どい亭 ヒコボシ, 100000917872, 1500, 2500, 202, 1, 1, 0, 1

"""
