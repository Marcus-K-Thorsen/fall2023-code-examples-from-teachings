# Åben en GitBash Terminal inde i VS Code ("Terminal" - "New Terminal" - "➕V" - "Git Bash")
# KOMMANDOER: 
# "pwd" XXX (printer den direkte file path til det Directory man arbejder/står i)
# "ls" og "ls -a" XXX (printer en liste af alle filer og folders/dictories der er i det directory man arbejder/står i)
# "cd <folder_navn>" og "cd .." XXX (skifter det directory man arbejder/står i til et directory kaldt <folder_navn> eller til et directory højere oppe)
# "python -m venv .venv" XXX (skaber et virtual environment, venv, kaldt for '.venv' i det directory man arbejder/står i)
# "source ./.venv/Scripts/activate" XXX (aktiverer et virtualt environment kaldt '.venv' som er i det directory man arbejder/står i)
# "deactivate" XXX (deaktiverer det virtualt environment der er aktivt og tager brug af et venv på højere niveau, som der hvor man har python installeret)
# "pip list" XXX (printer en liste af alle de Packages/Moduler som det virtual environment der er aktivt har tilrådighed)
# "pip install X" XXX (installerer en package/modul til det virtual environment (venv) der er aktivt)
# "pip freeze > requirements.txt" XXX (skaber eller overidder en tekst fil med navnet 'requirements', der har alle de packages/moduler det aktive venv skal bruge, i det directory man arbejder/står i)
# "pip  install -r requirements.txt" XXX (installere alle de packages/moduler, som står i 'requirements.txt' inde i det directory man står i, for det venv der er aktivt)

import requests
from bs4 import BeautifulSoup

def what_is_this(thing, descriptive_text):
    print()
    print(f"Thing: {thing}")
    print()
    print(f"Type: {type(thing)}")
    try:
        print(f"Length: {len(thing)}")
    except:
        print(f"Length: Has not lenght.")
    print(descriptive_text)
    print()

print('Hello from script')
URL = "https://realpython.github.io/fake-jobs/"
#what_is_this(URL, "A URL to a webpage")

page = requests.get(URL)
#what_is_this(page, "A webpage from the internet.")


soup = BeautifulSoup(page.content, "html.parser")
#what_is_this(soup, "A BeautifulSoup.")

results = soup.find(id="ResultsContainer")
#what_is_this(results, "The results of finding id = 'ResultsContainer'.")

pretty_results = results.prettify()
#what_is_this(pretty_results, "Results after .prettify()")

job_elements = results.find_all("div", class_="card-content")
#what_is_this(job_elements, "div elements with class='card-content' pulled from results.find_all()")


python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)
#what_is_this(python_jobs, "python_jobs = resultset.find_all")

python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]
what_is_this(python_job_elements, "python_job_elements = [h2_element.parent.parent.parent for h2_element in python_jobs]")

what_is_this(python_job_elements[0].find("a"), "python_job_elements[0].find('a').")

