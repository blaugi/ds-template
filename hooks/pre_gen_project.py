"""
# We use a docstring here so that we have a valid Python file that allows us to access the Jinja2 templating engine

{{ cookiecutter.update({ "_name_git": get_user_name() }) }}
{{ cookiecutter.update({ "full_name": prompt_user("full_name", get_user_name())})}}
{% if cookiecutter._name_git == "Name" or cookiecutter._name_git != cookiecutter.full_name %}
{{ ask_to_save(cookiecutter.full_name, "name")}}
{% endif %}

{{ cookiecutter.update({ "_email_git": get_user_email()})}} #gets user git email
{{ cookiecutter.update({ "email": prompt_user("email", get_user_email())})}} #asks user to input email
{% if cookiecutter.email == "Email" or cookiecutter.email != cookiecutter._email_git %} #if no email was found or input email was different, ask to save that to git config
{{ ask_to_save(cookiecutter.email, "email")}}
{% endif %}

{{ cookiecutter.update({"use_git": prompt_user_yes_no("use_git")}) }}
"""
"""
{% if cookiecutter.use_git %}
{{ cookiecutter.update({"default_branch": branch_name("default_branch", "main")}) }}
{{ cookiecutter.update({"configure_remote": prompt_user_yes_no("configure_remote") }) }}
{% else %}
{{ cookiecutter.update({"default_branch": '' }) }}
{{ cookiecutter.update ({"configure_remote": '' }) }}
{% endif %}

{% if cookiecutter.configure_remote %}
{{ cookiecutter.update({"remote_url": prompt_user("remote_url", "remote")})}}
{% else %}
{{ cookiecutter.update({"remote_url": ''}) }}
{% endif %}

{{ cookiecutter.update({"init_uv": prompt_user_yes_no("init_uv")}) }}
"""

