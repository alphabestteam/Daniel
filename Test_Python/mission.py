from developer import Developer


class Mission:

    def __init__(self, mission_name, open_date, project_name, complexity, work_time, developer: object, salary) -> None:

        self._mission_name = mission_name
        self._open_date = open_date
        self._project_name = project_name
        self._complexity = complexity
        self._developer = developer
        self._salary = salary
        self._end_date = work_time
        self._finished = False

    @property
    def mission_name(self):
        return self._mission_name

    @property
    def open_date(self):
        return self._open_date

    @property
    def end_date(self):
        return self._end_date

    @property
    def project_name(self):
        return self.project_name

    @property
    def complexity(self):
        return self._complexity

    @property
    def work_time(self):
        return self._work_time

    @property
    def developer(self):
        return self._developer

    @property
    def finished(self):
        return self._finished

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, dev: Developer):
        sal = (self.complexity/self.mission_time())*dev.experience
        return sal

    @end_date.setter
    def end_date(self, days):
        return self._open_date + days

    def mission_time(self):
        miss_time = (self.end_date - self.open_date)
        return miss_time

    def finish_mission(self):
        self.finished = True
