from django.shortcuts import render
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = [
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive',
]
json_file_name = 'angelic-tracer-264105-2bd30234b387.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, scope)
gc = gspread.authorize(credentials)
spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1c-X7io-Y5EahzJGG4wVOZO4xGXjTeCgIy2xSMeMDWDA/edit#gid=0'
# 스프레스시트 문서 가져오기
doc = gc.open_by_url(spreadsheet_url)
# 시트 선택하기
worksheet = doc.worksheet('시트1')

# for i in range(1,3):
# row_data = worksheet.row_values(i)
# 범위(셀 위치 리스트) 가져오기


def point_list(request):
    range_list = worksheet.range('A1:D180')

    # 이제 여기서 html로 어떻게 값을 띄울것 인지 고민
    pointlist = []
    list = []
    i = 0
    for cell in range_list:
        if cell.value == '':
            break
        list.append(cell.value)
        i = i + 1
        if i == 4:
            pointlist.append(list)
            list = []
            i = 0

    return render(request, 'point/point.html', {'point': pointlist})

def point_list_mine(request):
    range_list = worksheet.range('A1:D180')
    pointlist = []
    list = []
    i = 0
    for cell in range_list:
        if cell.value == '':
            break
        list.append(cell.value)
        i = i + 1
        if i == 4:
            if list[0] == user.first_name + user.last_name:
                pointlist.append(list)
            list = []
            i = 0