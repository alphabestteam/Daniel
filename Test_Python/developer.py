# from mission import Mission
class Developer:

    def __init__(self, name) -> None:
        self._name = name
        self._finished_mission = []
        self._total_work_days = 0
        self._total_salary = 0
        self._mission_to_perform = 0
        self._experience = 1

    @property
    def name(self):
        return self._name

    @property
    def finished_mission(self):
        return self._finished_mission

    @property
    def total_work(self):
        return self._total_work_days

    @property
    def total_salary(self):
        return self._total_salary

    @property
    def mission_perform(self):
        return self._mission_to_perform

    @property
    def experience(self):
        return self._experience

    # @total_salary.setter
    # def total_sal(self, mission:Mission):
    #     self.total_sal += mission.salary
    #     return self.total_sal

    # def finish_mission(self,mission:Mission):
    #     if
