import pathlib

def create_project_directory(dir_name: str):
    # create a project sub-directory
    pathlib.Path(dir_name).mkdir(exist_ok=True)


def main():
    create_project_directory("test")
    create_project_directory("docs")

if __name__ == "__main__":
    main()
