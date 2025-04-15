<a id="readme-top"></a>
<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#{{ cookiecutter.project_name.lower().replace(' ', '-').replace('_', '-') }}">{{ cookiecutter.project_name }}</a>
    </li>
    <li><a href="#author">Author</a></li>
    <li><a href="#key-users">Key Users</a></li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#setup-environment">Setup Environment</a></li>
        <li><a href="#running">Running</a></li>
      </ul>
    </li>
    <li><a href="#key-users">Key Users</a></li>
    <li><a href="#data">Data</a></li>
    <li><a href="#structure">Structure</a></li>
  </ol>
</details>


# {{ cookiecutter.project_name }}

{{ cookiecutter.project_desc }}

## Adjusting .gitignore


Ensure you adjust the `.gitignore` file according to your project needs. For example, since this is a template, the `/data/` folder is commented out and data will not be exlucded from source control:

```plaintext
# exclude data from source control by default
# /data/
```

Typically, you want to exclude this folder if it contains either sensitive data that you do not want to add to version control or large files.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Author

- [{{ cookiecutter.full_name }}]({{ cookiecutter.email }})


<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Key Users

- [Nome](email)
- [Nome](email)
- [Nome](email)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Data

```
**TODO**
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Structure

```
.
├── LICENCE
├── README.md
├── data
│   ├── external
│   ├── interim
│   ├── processed
│   └── raw
├── models
├── notebooks
│   ├── azuremlconnections.py
│   └── general.py
├── pipe
│   ├── __pycache__
│   │   └── azureml_env_build.cpython-310.pyc
│   ├── azureml_env_build.py
│   ├── azureml_pipe_orchestrator.py
│   └── utils
│       ├── __init__.py
│       ├── __pycache__
│       │   ├── __init__.cpython-310.pyc
│       │   └── compare_env_version.cpython-310.pyc
│       └── compare_env_version.py
├── references
├── release
│   └── release_template.json
├── reports
│   └── figures
├── requirements.txt
└── src
    ├── 01_load_data.py
    ├── 02_preprocessing.py
    ├── 03_model_inference.py
    ├── 04_post_processing.py
    ├── __init__.py
    ├── config
    │   └── pipe_env
    │       └── env.yml
    ├── modeling
    │   └── __init__.py
    ├── services
    │   └── __init__.py
    └── utils
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


