import datetime


def main():
    import csv

    data_file = open("./q3/question3.csv")
    business_hours = csv.reader(data_file)
    ans = ""
    for idx, row in enumerate(business_hours):  # 各データに対して判定
        msg = check_data(row)
        print(idx + 1, msg)
        if("OK" in msg):
            ans += "0"
        else:
            ans += "1"
    print(ans, len(ans))
    print(int(ans, 2))  # 10進数に変換


def check_data(row):  # 各項目について判定
    # 24時間表記でない
    for time in row:
        if not is_collect_time_notation(time):
            return "NG_24notation"

    # Closeの片方しかない
    # for i in range(len(row)):
    #     if i % 2 == 0:
    #         if (row[i] == "") and not(row[i + 1] == ""):
    #             return "NG_only_close"

    # 分の時間表記
    for time in row:
        if not is_collect_minutes_notation(time):
            return "NG_minutes_notaion"

    # 閉店時間が24時を超える場合のみ24を超えてよい
    for i in range(len(row)):
        if i % 2 == 0:
            if row[i] != "":
                hh, mm = row[i].split(":")
                time = int(hh + mm)
                if time > 2400:
                    return "NG_start-time_24:00"

    # 終了時刻が30:00を超えていないか
    for i in range(len(row)):
        if i % 2 == 0:
            if row[i] != "":
                hh, mm = row[i].split(":")
                time = int(hh + mm)
                if time > 3000:
                    return "NG_30:00"

    # 逆転チェック
    for i in range(len(row)):
        if i % 2 == 0:
            if is_reverse(row[i], row[i + 1]):
                return "NG_reverse"

    # 重なり
    open_close_times = []
    for i in range(len(row)):
        if i % 2 == 0:
            if row[i] == "" or row[i + 1] == "":
                open_close_times.append(
                    [3000 + i, 3000 + i + 1])  # 重ならないようなダミーデータ
                continue
            s_hh, s_mm = row[i].split(":")
            c_hh, c_mm = row[i + 1].split(":")
            start_time = int(s_hh + s_mm)
            close_time = int(c_hh + c_mm)
            open_close_times.append([start_time, close_time])
    if (open_close_times[0][0] <= open_close_times[1][0] and open_close_times[1][0] <= open_close_times[0][1]):
        return "NG_overlap1"
    elif(open_close_times[1][0] <= open_close_times[2][0] and open_close_times[2][0] <= open_close_times[1][1]):
        return "NG_overlap2"

    if not(open_close_times[0][0] < open_close_times[1][0] and open_close_times[1][0] < open_close_times[2][0]):
        return "NG_sort"
    return "OK"


def is_reverse(start, close):
    if start == "" or close == "":
        return False
    s_hh, s_mm = start.split(":")
    c_hh, c_mm = close.split(":")

    start_time = int(s_hh + s_mm)
    close_time = int(c_hh + c_mm)
    if not start_time < close_time:
        return True
    return False


def is_collect_minutes_notation(time):
    if time == "":
        return True
    hh, mm = time.split(":")
    if len(mm) == 1:
        return False
    return True


def is_collect_time_notation(time):
    if time == "":
        return True

    #:でわかれていない
    try:
        hh, mm = time.split(":")
    except Exception as e:
        print(e)
        return False

    # 数字にキャスト不可=>文字列が含まれている
    try:
        hh = int(hh)
        mm = int(mm)
    except Exception as e:
        print(e)
        return False

    # 60分を超えている
    if mm >= 60:
        return False

    return True


if __name__ == "__main__":
    main()
