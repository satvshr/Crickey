from bs4 import BeautifulSoup
import requests
import csv
import time

def write_csv_file(csv_file_path, data):
    file = open(csv_file_path, 'w', newline='')
    writer = csv.writer(file)
    writer.writerow(data)
    file.close()


def read_csv_file(csv_file_path):
        all_rows = []
        with open(csv_file_path, 'r') as file:
            csv_reader = csv.reader(file)

            for row in csv_reader:
                all_rows.append(row)

        return all_rows

while(1):

    url = 'https://www.espncricinfo.com/live-cricket-score'
    response = requests.get(url)
    detailList = []
    if response:
        html_content = response.content
        soup = BeautifulSoup(html_content, 'html.parser')
        match = soup.find('div', class_='ds-px-4 ds-py-3')
        details = match.find_all('div', class_='ci-team-score ds-flex ds-justify-between ds-items-center ds-text-typo ds-my-1')
        for detail in details:
             detailList.append(detail.text)
        write_csv_file('liveScores.csv', detailList)
        for detail in detailList:
            print(detail)
            print()
        

        time.sleep(10)
    else:
        print("Failed to fetch the webpage.")
        break
