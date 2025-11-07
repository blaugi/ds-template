import os
import shutil
import subprocess

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
PYTHON_VERSION = "{{ cookiecutter.python_version }}"


# Set up git repository
def init_git():
    try:
        subprocess.check_call(
            ["git", "init", "-b", "{{ cookiecutter.default_branch }}"],
            cwd=PROJECT_DIRECTORY,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

        subprocess.check_call(
            ["git", "config", "--global", "--add", "safe.directory", PROJECT_DIRECTORY],
            cwd=PROJECT_DIRECTORY,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

        subprocess.check_call(
            ["git", "add", "."],
            cwd=PROJECT_DIRECTORY,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

        subprocess.check_call(
            ["git", "commit", "-m", "Initial commit from cookicutter."],
            cwd=PROJECT_DIRECTORY,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

        print("Git repository initialized successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error initializing git repository: {e}")


def copy_env():
    src = os.path.join(PROJECT_DIRECTORY, "src/config/.env.example")
    dst = os.path.join(PROJECT_DIRECTORY, "src/config/.env")
    try:
        shutil.move(src, dst)
        print(".env file created successfully!")
    except Exception as e:
        print(f"Error creating .env file: {e}")


def create_gitingore():
    gitignore_path = os.path.join(PROJECT_DIRECTORY, "data/.gitignore")
    content = "#Exclude everything except the gitignore\n*\n!.gitignore\n"
    try:
        os.makedirs(os.path.dirname(gitignore_path), exist_ok=True)
        with open(gitignore_path, "w") as f:
            f.write(content)
    except Exception as e:
        print(f"Error creating .gitignore file in data folder: {e}")


def init_uv():
    try:
        subprocess.check_call(
            ["uv", "init", "-p", PYTHON_VERSION, "--vcs", "none"],
            cwd=PROJECT_DIRECTORY,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        # subprocess.check_call(
        # ["uv", "python", "pin", version],
        # cwd=PROJECT_DIRECTORY,
        # stdout=subprocess.DEVNULL,
        # stderr=subprocess.DEVNULL,
        # )
        main_path = os.path.join(PROJECT_DIRECTORY, "main.py")
        os.unlink(main_path)
    except subprocess.CalledProcessError as e:
        print(f"Error initalizing uv: {e}")


def set_remote(url):
    try:
        subprocess.check_call(
            ["git", "remote", "add", "origin", url],
            cwd=PROJECT_DIRECTORY,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        subprocess.check_call(
            ["git", "push", "-u", "origin", "{{ cookiecutter.default_branch}}"],
            cwd=PROJECT_DIRECTORY,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    except subprocess.CalledProcessError as e:
        print(f"Error configuring remote: {e}")

def _cc_to_bool(val: str) -> bool:
    try:
        s = str(val).strip().lower()
    except Exception:
        return False
    return s in ("y", "yes", "true", "t", "1")


if __name__ == "__main__":
    create_gitingore()

    if _cc_to_bool("{{cookiecutter.init_uv}}"):
        init_uv()

    if _cc_to_bool("{{ cookiecutter.use_git }}"):
        init_git()

    if _cc_to_bool("{{ cookiecutter.configure_remote}}"):
        set_remote("{{ cookiecutter.remote_url}}")
    # copy_env()
