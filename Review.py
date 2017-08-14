# Create custom data structure Review to hold user reviews
class Review:
    def __init__(self, name, position, company, rating, goodies, day):
        self.name = name
        self.position = position
        self.company = company
        self.rating = rating
        self.goodies = goodies
        self.day = day

    def __repr__(self):
        return "Review(%s: %s, %s, %s, %s, %s)" % (self.name, self.position, 
                                                                  self.company, self.rating,
                                                                  self.goodies, self.day)

    