class course:
    def __init__(self):
        self.name = ""
        self.number = 0
        self.points = 0
        self.dependencies = list()
        self.parallel = set()
        self.similarities = set()
        self.inclusive = set()

    def set_name(self, name):
        self.name = name

    def set_number(self, number):
        self.number = number

    def set_points(self, points):
        try:
            self.points = int(points)
        except ValueError:
            self.points = 0

    def add_inclusive(self, courses):
        self.inclusive.update(courses)

    def add_dependencies(self, courses):
        self.dependencies.extend(courses)

    def add_similarities(self, courses):
        self.similarities.update(courses)

    def add_parallel(self, courses):
        self.parallel.update(courses)

    def __repr__(self):
        repr = "שם הקורס: {} \n".format(self.name) \
               + "מספר קורס: {} \n".format(self.number) \
               + ("מס' נקודות: {} \n".format(self.points) if self.points > 0 else "") \
               + ("מקצועות קדם: {} \n".format(self.dependencies) if len(self.dependencies) > 0 else "") \
               + ("מקצועות צמודים: {} \n".format(self.parallel) if len(self.parallel) > 0 else "") \
               + ("מקצועות ללא זיכוי נוסף: {} \n".format(self.similarities) if len(self.similarities) > 0 else "") \
               + ("מקצועות ללא זיכוי נוסף (מוכלים): {} \n".format(self.inclusive) if len(self.inclusive) > 0 else "")
        return repr
