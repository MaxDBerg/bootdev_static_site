import os
import shutil


def generate_public_dir():
    if os.path.exists("public/"):
        # print("deleting public dir...")
        shutil.rmtree("public/")
    # print("creating public directory...")
    os.mkdir("public/")
    copy_static_to_public("static/")


def copy_static_to_public(top_path):
    for sub_path in os.listdir(top_path):
        full_path = os.path.join(top_path, sub_path)
        # print(full_path)
        # print(os.path.isdir(full_path))
        if os.path.isdir(full_path):
            os.mkdir(full_path.replace("static", "public"))
            copy_static_to_public(full_path)
        else:
            shutil.copy(full_path, top_path.replace("static", "public"))
        # print("we have reached the bottom : " + full_path)
