class DiffParser:
    diff = ""
    changed = dict()
    added = dict()
    deleted = dict()

    def __init__(self, diff):
        if diff is None or diff == "":
            raise Exception("Diff must be provided")
        self.diff = diff

    def validate_data(self):
        return_value = False
        diff = self.diff.split("\n")

        if type(diff) is list and len(diff) > 2:
            return_value = True

        if diff[0][0:4] == "diff":
            return_value = True
        else:
            return_value = False

        return return_value

    def parse(self):
        if self.diff == "":
            return False
        return True
