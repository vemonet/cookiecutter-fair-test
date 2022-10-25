from fair_test import FairTestAPI


app = FairTestAPI(
    title='{{cookiecutter.package_name_stylized}}',
    metrics_folder_path='metrics',
    description="""{{cookiecutter.description}}

[Metrics Tests source code]({{cookiecutter.git_repository_url}}), built with the [**fair-test** library](https://maastrichtu-ids.github.io/fair-test)

[![Test Metrics]({{cookiecutter.git_repository_url}}/actions/workflows/test.yml/badge.svg)]({{cookiecutter.git_repository_url}}/actions/workflows/test.yml)
""",
    license_info = {
        "name": "MIT license",
        "url": "https://opensource.org/licenses/MIT"
    },
)
