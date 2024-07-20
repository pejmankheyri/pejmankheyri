import datetime
import os

def calculate_profile_age(creation_date):
    creation_date = datetime.datetime.strptime(creation_date, "%Y-%m-%d")
    today = datetime.datetime.now()
    age = today - creation_date
    return age.days // 365, (age.days % 365) // 30

def update_readme():
    creation_date = "2013-01-21"  
    years, months = calculate_profile_age(creation_date)
    
    age_info = f"I have been on GitHub for {years} years and {months} months!\n\n"

    with open("README.md", "r") as readme_file:
        lines = readme_file.readlines()
    
    new_content = []
    in_github_stats = False
    found_age_info = False
    for line in lines:
        if line.strip() == "## GitHub Statistics":
            in_github_stats = True
        if in_github_stats and "I have been on GitHub for" in line:
            found_age_info = True
            new_content.append(age_info)
        else:
            new_content.append(line)
    
    if not found_age_info and in_github_stats:
        new_content.insert(lines.index("## GitHub Statistics") + 1, age_info)
    
    with open("README.md", "w") as readme_file:
        readme_file.writelines(new_content)

    return found_age_info

if __name__ == "__main__":
    modified = update_readme()
    if modified:
        os.system('git add README.md')
        os.system('git commit -m "Update profile age in GitHub Statistics"')
        os.system('git push')
