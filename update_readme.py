import datetime

def calculate_profile_age(creation_date):
    creation_date = datetime.datetime.strptime(creation_date, "%Y-%m-%d")
    today = datetime.datetime.now()
    age = today - creation_date
    return age.days // 365, (age.days % 365) // 30

def update_readme():
    creation_date = "2013-01-21"  # Replace with your GitHub profile creation date
    years, months = calculate_profile_age(creation_date)
    
    with open("README.md") as f:
        lines = f.readlines()

    new_header = f"## Hello World! This is @Pejman 👋 I have been on GitHub for {years} years and {months} months!\n"

    if lines[0] != new_header:
        lines[0] = new_header
        with open("README.md", "w") as f:
            f.writelines(lines)

if __name__ == "__main__":
    update_readme()
