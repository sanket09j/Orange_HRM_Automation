import json
import os


class JsonReader:

    @staticmethod
    def read_json(file_name):

        project_path = os.path.dirname(os.path.dirname(__file__))

        file_path = os.path.join(
            project_path,
            "TestData",
            file_name
        )

        with open(file_path, "r") as file:
            return json.load(file)