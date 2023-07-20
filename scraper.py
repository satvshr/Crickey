from bs4 import BeautifulSoup
import requests
import csv

url = 'https://www.espncricinfo.com/live-cricket-score'
response = requests.get(url)

if response:
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    match = soup.find('div', class_='ds-flex ds-flex-col ds-mt-2 ds-mb-2')
    team1 = match.find('div', class_='ci-team-score ds-flex ds-justify-between ds-items-center ds-text-typo ds-opacity-50 ds-my-1')
    team1 = team1.find('div', class_='ds-flex ds-items-center ds-min-w-0 ds-mr-1')
    team1 = team1.find('p', class_='ds-text-tight-m ds-font-bold ds-capitalize ds-truncate')
    print(team1.text)
    team2 = match.find('div', class_='ci-team-score ds-flex ds-justify-between ds-items-center ds-text-typo ds-my-1')
    team2 = team2.find('div', class_='ds-flex ds-items-center ds-min-w-0 ds-mr-1')
    team2 = team2.find('p', class_='ds-text-tight-m ds-font-bold ds-capitalize ds-truncate')
    print(team2.text)

    details = soup.find('div', class_='ds-text-compact-xxs')
    details = details.find('p', class_='ds-text-tight-s ds-font-regular ds-truncate ds-text-typo')
    print(details.text)
    
    team2scores = match.find('div', class_='ci-team-score ds-flex ds-justify-between ds-items-center ds-text-typo ds-my-1')
    score2 = team2scores.find_all('strong')

    team1scores = match.find('div', class_='ds-text-compact-s ds-text-typo ds-text-right ds-whitespace-nowrap')
    score1 = team1scores.find_all('strong')

    file = open("liveScores.csv", 'w', newline='')
    writer = csv.writer(file)
    writer.writerow([team1.text, team2.text, details.text])
    print(score1)
    print(score2)
    for i in range(len(score1)):
        writer.writerow([score1[i].text.replace('&','').replace(' ', ''), score2[i].text.replace('&','').replace(' ', '')])
    file.close()
else:
    print("Failed to fetch the webpage.")
