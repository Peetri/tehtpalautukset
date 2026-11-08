class Project:
    def __init__(self, name, description, dependencies, dev_dependencies, license, authors):
        self.name = name
        self.description = description
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies
        self.license = license
        self.authors = authors

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"

    def __str__(self):
        authors = ""
        for x in self.authors:
            authors += f"- {x}\n"

        dependencies = ""
        for x in self.dependencies:
            dependencies += f"- {x}\n"

        dev_dependencies = ""
        for x in self.dev_dependencies:
            dev_dependencies += f"- {x}\n"

        return (
            f"Name: {self.name.replace("-", " ").capitalize()}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license}"
            f"\n\nAuthors:\n{authors}"
            f"\nDependencies:\n{dependencies}"
            f"\nDevelopment dependencies:\n{dev_dependencies.rstrip()}"
        )
