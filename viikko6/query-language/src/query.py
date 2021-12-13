from matchers import All, PlaysIn, HasAtLeast, HasFewerThan, And


class QueryBuilder:
    def __init__(self, matcher = And()):
        self.matcher = matcher

    def build(self):
        return self.matcher

    def playsIn(self, team):
        return QueryBuilder(PlaysIn(team))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(HasAtLeast(value, attr))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(HasFewerThan(value, attr))