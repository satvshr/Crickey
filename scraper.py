from bs4 import BeautifulSoup
import requests
import csv

url = 'https://www.espncricinfo.com/live-cricket-score'
response = requests.get(url)

if response:
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    team1 = soup.find('p', class_='ds-text-tight-m ds-font-bold ds-capitalize ds-truncate')
    team2 = soup.find('p', class_='ds-text-tight-m ds-font-bold ds-capitalize ds-truncate !ds-text-typo-mid3')    
    overs = soup.find('span', class_= 'ds-text-compact-xs ds-mr-0.5')
    scores = soup.find('div', class_ = 'ci-team-score ds-flex ds-justify-between ds-items-center ds-text-typo ds-my-1')
    score = scores.find_all('strong')
    file = open("liveScores.csv", 'w')
    writer = csv.writer(file)
    writer.writerow(['Team 1', 'Team 2', 'Overs', 'Score'])
    writer.writerow([team1.text, team2.text, overs.text, score[0].text])
    file.close()
else:
    print("Failed to fetch the webpage.")


