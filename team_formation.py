import csv
import random

def read_csv(file_path):
    data = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append({'name': row[0].strip(), 'role': row[1].strip()})
    return data

def assign_roles(teams, team_number, name):
    teams[team_number].append(name)
    return teams

def shuffle_members(members):
    random.shuffle(members)
    return members

def divide_teams(data, num_teams, min_members_per_team=4):
    teams = {f'Team {i+1}': [] for i in range(num_teams)}

    product_managers = [person['name'] for person in data if person['role'] == 'Product Manager']
    engineers = [person['name'] for person in data if person['role'] == 'Software Engineer']
    enthusiasts = [person['name'] for person in data if person['role'] == 'Product Enthusiast']

    product_managers = shuffle_members(product_managers)
    engineers = shuffle_members(engineers)
    enthusiasts = shuffle_members(enthusiasts)

    for team_number in teams:
        teams = assign_roles(teams, team_number, product_managers.pop())
        teams = assign_roles(teams, team_number, engineers.pop())

    remaining_members = shuffle_members(product_managers + engineers + enthusiasts)

    while remaining_members:
        for team_number in teams:
            if remaining_members and len(remaining_members)>0:
               teams[team_number].append(remaining_members.pop())

    return teams

def main():
    file_path = 'att/day1.csv'  
    num_teams = 2  

    data = read_csv(file_path)
    teams = divide_teams(data, num_teams)

    print(teams)

if __name__ == "__main__":
    main()
