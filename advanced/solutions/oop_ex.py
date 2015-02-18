class Student(Person):
    def __init__(self, name, school = None):
        self.name = name
        self.school = school

    def WhereDoYouStudy(self):
        return self.school

class PhD(Employee, Student):
    title = 'PhD'

    def __init__(self, name, organization, major, school=None):
        Employee.__init__(self, name, organization)
        Student.__init__(self, name, school)
        self.major = major

    def WhatIsYourMajor(self):
        return self.major

    def WhereDoYouStudy(self):
        return super(PhD, self).WhereDoYouStudy() if self.school else self.WhereDoYouWork()

p4 = PhD('Chris','Aramco','EE','KAUST')
print '%s is a %s in %s at %s' % (p4.name, p4.title, p4.WhatIsYourMajor(), p4.WhereDoYouStudy())
