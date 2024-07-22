import datetime
import re

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
        first_line = readme_file.readline()


    print(first_line)

    new_header = f"## Hello World! This is @Pejman 👋 I have been on GitHub for {years} years and {months} months!\n"

    # replace the first line

    updated_content = existing_content.replace(first_line, new_header)

    # updated_content = new_header + existing_content

    # Regex to find the existing header and replace it
    # updated_content = re.sub(r"## Hello World! This is @Pejman 👋 I have been on GitHub for \d+ years and \d+ months!\n", new_header, existing_content)

    # If the header was not found and replaced, prepend it to the content
    # if updated_content == existing_content:
    #     updated_content = new_header + existing_content
    
    with open("README.md", "w") as readme_file:
        readme_file.write(updated_content)

if __name__ == "__main__":
    update_readme()
