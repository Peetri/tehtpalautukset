from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        data = toml.loads(content)

        project_data = data["project"]

        name = project_data["name"]
        description = project_data["description"]
        dependencies = project_data["dependencies"]

        dev_dependencies = data["dependency-groups"]["dev"]

        license = project_data["license"]
        authors = project_data["authors"]

        dependencies_uusi = []

        for x in dependencies:
            osa = x.split(">=")
            dependencies_uusi.append(osa[0])

        dev_dependencies_uusi = []

        for x in dev_dependencies:
            osa = x.split(">=")
            dev_dependencies_uusi.append(osa[0])

        authors_uusi = []

        for x in authors:
            authors_uusi.append(x["name"])

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, dependencies_uusi, dev_dependencies_uusi, license, authors_uusi)
