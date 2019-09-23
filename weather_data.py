import re
import requests
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt
from matplotlib.ticker import EngFormatter

def main(url):
    result = requests.get(url)
    status = result.status_code

    assert status == 200, f"Site Error: Status Code {status}"

    data = get_data(result.content)
    draw_data(data)

def get_data(source):
    """
    Gets a html source (str) and parses it with BeautifulSoup
    :param source: str()
    :return: dict()
    """

    soup = BeautifulSoup(source, 'lxml')
    page_title = soup.title.text

    columns = soup.find_all('div', class_="oszlop")

    day_list = []
    temp_mins = []
    temp_maxes = []
    for col in columns:
        date_day = col.find('div', class_='nap')
        date_num = col.find('div', class_='datum')

        day_list.append(f'{date_num.text} {date_day.text}')

        max_temp = col.find('div', class_='max-homerseklet-default max')
        max_num = re.findall(r'\d+', max_temp.text)[0]
        temp_maxes.append(int(max_num))

        min_temp = col.find('div', class_='min-homerseklet-default max')
        min_num = re.findall(r'\d+', min_temp.text)[0]
        temp_mins.append(int(min_num))

    return {
        "title": page_title,
        "days" : day_list,
        "mins" : temp_mins,
        "maxes": temp_maxes
    }

def draw_data(data):
    """
    Gets a dictionary and draws a plot fron it's data
    :param data: dict()
    :return: None
    """

    fig_size = plt.rcParams["figure.figsize"]

    fig_size[0] = 16
    fig_size[1] = 7
    plt.rcParams["figure.figsize"] = fig_size

    plt.style.use("seaborn-whitegrid")

    title = data["title"]
    day_list = data["days"]

    minimums = data["mins"]
    maximums = data["maxes"]

    plt.plot(day_list, minimums, color="#3399FF", marker="o", label="Minimum")
    plt.plot(day_list, maximums, color="#FF6666", marker="o", label="Maximum")

    ay = plt.gca().get_yaxis()
    ay.set_major_formatter(EngFormatter(unit="°C"))

    plt.xticks(fontsize=9)

    plt.title(title + "\n")
    plt.legend()
    # plt.savefig(f'{title}.png')
    plt.show()

main('https://www.idokep.hu/30napos/Budapest')
# main('https://www.idokep.hu/30napos/Gy%C5%91r')