from bs4 import BeautifulSoup
import streamlit as st
import requests
import math
import csv

st.title("Hockey Teams")


pages = list(range(1, 26))
all_teams = []

for page_num in pages:
    url = f'https://www.scrapethissite.com/pages/forms/?page_num={page_num}'
    response = requests.get(url)
    html_template = BeautifulSoup(response.text, 'lxml')

    table_data = html_template.find('table', class_='table')
    table_rows = table_data.find_all('tr')[1:] 

    for row in table_rows:
        team_name_tag = row.find('td', class_='name')
        if not team_name_tag:
            continue
        team_name = team_name_tag.text.strip()
        team_year = row.find('td', class_='year').text.strip() if row.find('td', class_='year') else 'N/A'
        team_wins = row.find('td', class_='wins').text.strip() if row.find('td', class_='wins') else 'N/A'
        team_losses = row.find('td', class_='losses').text.strip() if row.find('td', class_='losses') else 'N/A'
        team_ot_losses = row.find('td', class_='ot-losses').text.strip() if row.find('td', class_='ot-losses') else 'N/A'

        pct_tag = row.find('td', class_='pct text-success') or row.find('td', class_='pct text-danger')
        team_pct = pct_tag.text.strip() if pct_tag else 'N/A'

        gf_tag = row.find('td', class_='gf')
        team_gf = gf_tag.text.strip() if gf_tag else 'N/A'

        diff_tag = row.find('td', class_='diff text-success') or row.find('td', class_='diff text-danger')
        team_diff = diff_tag.text.strip() if diff_tag else 'N/A'

        all_teams.append({
            "name": team_name,
            "year": team_year,
            "wins": team_wins,
            "losses": team_losses,
            "ot_losses": team_ot_losses,
            "pct": team_pct,
            "gf": team_gf,
            "diff": team_diff
        })


csv_file = "Hockey_Team.csv"

with open(csv_file, mode="w", newline='', encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "year", "wins", "losses", "ot_losses", "pct", "gf","diff"])
    writer.writeheader()
    
    for team in all_teams:
        writer.writerow(team)

team_names = ["All Teams"] + sorted(list({team['name'] for team in all_teams}))
selected_team = st.selectbox("Select a team:", team_names)

if selected_team == "All Teams":
    filtered_teams = all_teams
else:
    filtered_teams = [team for team in all_teams if team['name'] == selected_team]

teams_per_page = 5
total_pages = math.ceil(len(filtered_teams) / teams_per_page)
page_number = st.number_input("Page number:", min_value=1, max_value=total_pages, value=1, step=1)

start_index = (page_number - 1) * teams_per_page
end_index = start_index + teams_per_page
teams_to_show = filtered_teams[start_index:end_index]

for i, team in enumerate(teams_to_show, start=start_index+1):
    st.warning(f"Team {i}: {team['name']}")
    st.info(f"Year: {team['year']} | Wins: {team['wins']} | Losses: {team['losses']} | "
            f"OT Losses: {team['ot_losses']} | Pct: {team['pct']} | GF: {team['gf']} | Diff: {team['diff']}")

st.caption(f"Showing {start_index+1}-{min(end_index,len(filtered_teams))} of {len(filtered_teams)} teams")
