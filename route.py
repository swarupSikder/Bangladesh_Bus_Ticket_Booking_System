class Route:
    def __init__(self, start_point, end_point):
        self.start_point = start_point
        self.end_point = end_point

    def __repr__(self):
        return f'Route: [{self.start_point} - {self.end_point}]'