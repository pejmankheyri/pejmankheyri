import datetime

def calculate_profile_age(creation_date):
    creation_date = datetime.datetime.strptime(creation_date, "%Y-%m-%d")
    today = datetime.datetime.now()
    age = today - creation_date
    return age.days // 365, (age.days % 365) // 30

def update_readme():
    creation_date = "2013-01-21"  # Replace with your GitHub profile creation date
    years, months = calculate_profile_age(creation_date)
    
    with open("README.md", "r") as readme_file:
        existing_content = readme_file.read()

    new_content = f"""
## Hello World! This is @Pejman 👋 I have been on GitHub for {years} years and {months} months!

{existing_content}
    """
    
    with open("README.md", "w") as readme_file:
        readme_file.write(new_content)

if __name__ == "__main__":
    update_readme()
