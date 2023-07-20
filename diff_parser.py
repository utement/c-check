class DiffParser:
    diff = ""
    changed = dict()
    added = dict()
    deleted = dict()

    def __init__(self, diff):
        if diff is None or diff == "":
            raise Exception("Diff must be provided")
        self.diff = diff

    def parse(self):
        pass
