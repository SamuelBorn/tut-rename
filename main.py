import os


def rename():
    for directory in get_dirs(os.getcwd()):
        full_path = os.path.join(os.getcwd(), directory)
        multiple_submissions = len(get_files(full_path)) > 1
        for idx, file in enumerate(get_files(full_path)):
            old_file = os.path.join(full_path, file)
            file_extension = os.path.splitext(old_file)[1]
            if multiple_submissions:  # rename with index when there are multiple submissions per person
                new_file = os.path.join(full_path, directory + f"_({idx})" + file_extension)
            else:
                new_file = os.path.join(full_path, directory + file_extension)
            os.rename(old_file, new_file)


def move_to_current():
    for directory in get_dirs(os.getcwd()):
        full_path = os.path.join(os.getcwd(), directory)
        for file in get_files(full_path):
            old_file = os.path.join(full_path, file)
            new_file = os.path.join(os.getcwd(), file)
            os.rename(old_file, new_file)


def move_to_corresponding():
    for file in get_files(os.getcwd()):
        for directory in get_dirs(os.getcwd()):
            if directory in file:  # check for substring because dir name is part of file name
                old_file = os.path.join(os.getcwd(), file)
                new_file = os.path.join(os.getcwd(), directory, file)
                os.rename(old_file, new_file)


def get_files(path):
    return [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]


def get_dirs(path):
    return [directory for directory in os.listdir(path) if not os.path.isfile(os.path.join(path, directory))]


def main():
    if os.getcwd() != "Abgaben":  # check that the user is in the correct directory
        raise Exception("You are in the wrong Directory, make sure you are in '.../Uebungsblatt X/Abgaben'")

    print("1 - rename all files")
    print("2 - move all files to current dir for easy imports")
    print("3 - move all files back to their corresponding dir (requires renamed files)")
    selection = input("Enter selection: ")

    match selection:
        case "1":
            rename()
        case "2":
            move_to_current()
        case "3":
            move_to_corresponding()
        case _:
            raise Exception("Not a valid option")


if __name__ == "__main__":
    main()
