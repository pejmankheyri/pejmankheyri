import datetime

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
            new_content.append(line)
            new_content.append(age_info)
            continue
        if in_github_stats and "I have been on GitHub for" in line:
            found_age_info = True
            continue
        new_content.append(line)
    
    if not found_age_info and in_github_stats:
        index = lines.index("## GitHub Statistics\n")
        new_content.insert(index + 1, age_info)
    
    with open("README.md", "w") as readme_file:
        readme_file.writelines(new_content)

    # Output the new content for debugging purposes
    print("New README content:")
    print("".join(new_content))

if __name__ == "__main__":
    update_readme()
