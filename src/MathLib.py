from src.MathRequests import MathRequest
from src.main import calculate


class Mathlib:

    def __init__(self, mathrequests: MathRequest, match_case):
        self.mathrequests = mathrequests
        self.calculate = match_case