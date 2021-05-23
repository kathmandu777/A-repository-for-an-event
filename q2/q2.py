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
