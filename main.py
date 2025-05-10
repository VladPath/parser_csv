import json
from sys import argv


res = dict()
# You can add more allowed report hire
allowed_report = ['payout']
arr = argv
data = []

for arg_idx in range(1, len(arr)):
    if arr[arg_idx] == '--report':
        if arr[arg_idx+1] in allowed_report:
            REPORT = arr[arg_idx+1]
            break
        else:
            # if user input wrong type of report
            raise ValueError(f'{arr[arg_idx+1]} is wrog report, just {allowed_report} is allowed')
    # raise error if user input wrong flag
    elif arr[arg_idx][0:1] == '-':
        raise TypeError('Just --report')
    # raise error if user input wrong type of data
    elif arr[arg_idx][-3:] != 'csv':
        raise TypeError('Just .csv files')

    data.append(arr[arg_idx])

# Function for get possition for curr csv file
def get_name_pos(data: list) -> int:
    title = data[0].split(',')
    for i in range(len(title)):
        if title[i] == 'name':
            return i

def get_department_pos(data: list) -> int:
    title = data[0].split(',')
    for i in range(len(title)):
        if title[i] == 'department':
            return i

def get_hours_pos(data: list) -> int:
    title = data[0].split(',')
    for i in range(len(title)):
        if title[i] in ['rate','salary','hourly_rate']:
            return i

def get_rate_pos(data: list) -> int:
    title = data[0].split(',')
    for i in range(len(title)):
        if title[i] == 'hours_worked':
            return i

# Creating func for calculations
def calculation_payout(x: int,y: int):
    return x*y

# Main func where we are create json file
def create_json_file(csv: str,  report: str):

    with open(csv,'r') as d:
        data = list(map(str,d.read().split('\n')))
        position_name = get_name_pos(data)
        position_dep = get_department_pos(data)
        position_hours = get_hours_pos(data)
        position_rate = get_rate_pos(data)


        for i in data[1:]:
            if i:
                stroke = i.split(',')
                pos = stroke[position_dep]
                name = stroke[position_name]
                hours = stroke[position_hours]
                rate = stroke[position_rate]

                # you can add more reports if you need
                if REPORT == 'payout':
                    res.setdefault(pos,[]).append({'name': name,'hours': hours,'rate': rate,
                                report: calculation_payout(int(hours), int(rate)),
                                })


# creating json data for all csv files
for csv in data:
    create_json_file(csv, REPORT)

# creating json file
with open('json_file.json','w') as file:
        json.dump(res, file, indent=4)






















