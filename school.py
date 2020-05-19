class School:
    def __init__(self, name, roster={}):
        self.name = name
        self.roster = roster

    def add_student(self, full_name, grade_level):
        if self.roster.get(grade_level) != None:
            # the grade already exists
            self.roster[grade_level].append(full_name)
        else:
            # the grade does not exist yet
            self.roster[grade_level] = [full_name]

    def grade(self, grade):
        grade_info = self.roster.get(grade)
        return grade_info

    def sort_roster(self):
        for key, value in self.roster.items():
            self.roster[key] = sorted(value)
        return self.roster
