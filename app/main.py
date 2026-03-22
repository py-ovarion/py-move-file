import os


def move_file(command_request: str) -> None:
    command_list = command_request.split(" ")
    if len(command_list) == 3:
        command = command_list[0]
        source_path = command_list[1]
        destination_path = command_list[2]

        if command == "mv":
            if destination_path.find("/") != -1:
                make_dirs(destination_path[:destination_path.rfind("/")])

            with (open(source_path, "r") as source_file_object,
                  open(destination_path, "w") as destination_file_object):
                destination_file_object.write(source_file_object.read())
            os.remove(source_path)


def make_dirs(path: str) -> None:
    dir_path = ""
    for dirname in path.split("/"):
        try:
            dir_path += dirname
            os.mkdir(dir_path)
        except FileExistsError:
            pass
        finally:
            dir_path += "/"
