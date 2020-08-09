import setuptools

from os import path

if __name__ == "__main__":
    this_directory = path.abspath(path.dirname(__file__))
    with open(path.join(this_directory, 'README.md'), encoding='utf-8') as readme_file:
        long_description = readme_file.read()

    setuptools.setup(
        name="datascience_project_0_github_guessnumber",
        version="0.1.0",
        platforms='any',
        description="Data science project 0: A guess number game example with primitive self-testing",
        long_description=long_description,
        long_description_content_type="text/markdown",
        author="Dmitry Vlasov",
        author_email="dmitry.v.vlasov@gmail.com",
        license="MIT",
        url="https://github.com/dmitry-v-vlasov/data-science-course/tree/master/module_0/datascience_project_0_github_guessnumber",
        keywords=["datascience", "essentials", "guessnumber"],
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent"
        ],
        install_requires=["setuptools", "wheel", "numpy"],
        packages=setuptools.find_packages(),
        entry_points={
            "console_scripts": ["datascience_guessnumber=datascience_project_0_github_guessnumber.command_line:run"]
        }
    )
