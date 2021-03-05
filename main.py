import sys
from datetime import datetime as dt
from datetime import timedelta
import calendar

# 引数チェック（2つ以外はエラー）
def argv_check():
    if len(sys.argv) != 3:
        print('引数が少なすぎるか多すぎます。')
        exit()


# メイン処理
def main():
    # 西暦と月を入力値から取得
    im_year = sys.argv[1]
    im_month = sys.argv[2]

    if len(im_month) == 1:
        im_month = '0' + im_month

    start_date = im_year + '-' + im_month + '-' + '01'

    end_day = calendar.monthrange(int(im_year), int(im_month))[1]
    end_date = im_year + '-' + im_month + '-' + str(end_day)

    strdt = dt.strptime(start_date, '%Y-%m-%d')
    enddt = dt.strptime(end_date, '%Y-%m-%d')
    days_num = ( enddt - strdt ).days + 1

    datelist = []
    for i in range(days_num):
        datelist.append(strdt + timedelta(days=i))

    i = 0
    for delete_date in datelist:
        if delete_date.weekday() == 5 or delete_date.weekday() == 6:
            del datelist[i]
        i += 1

    # 確認用
    for d in datelist:
        print(d.strftime("%Y-%m-%d (%A)"))




argv_check()
main()
