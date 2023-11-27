import datetime
from mission import Mission


class Project:

    def __init__(self, description, start_date) -> None:
        self._description = description
        self._start_date = start_date
        self._mission_list = []
        self._dev_list = []
        self._end_date = 0
        self._missions_to_perform = []
        self._finished_missions = []
        self._total_cost = 0
        self._perfectly_done = False

    @property
    def description(self):
        return self._description

    @property
    def mission_list(self):
        return self._mission_list

    @property
    def open_date(self):
        return self._start_date

    @property
    def end_date(self):
        return self._end_date

    @property
    def mission_to_perform(self):
        return self._missions_to_perform

    @property
    def finished_mission(self):
        return self._finished_missions

    @finished_mission.setter
    def finished_mission(self, mission):
        self.finished_mission.append(mission)
        self.mission_list.pop(mission)
        return self._finished_missions

    # I assumed that the user input will be days by number.
    @end_date.setter
    def end_date(self, days):
        return self._start_date + days

    def add_mission(self, mission: Mission):
        new_mission = ({mission.mission_name: {
                       "dev_name": mission.developer, "time": mission.mission_time()}})
        self._mission_list.append(new_mission)
        self.mission_to_perform.append(mission.mission_name)
        print(new_mission)
    # add project developer to list

    def add_project_dev(self, mission: Mission):
        self._dev_list.append(mission.developer)

    # calculate project time
    def calculate_proj_time(self, mission: Mission):
        for miss in self._mission_list:
            total_time = miss[mission.mission_name][mission.mission_time()]
            self.end_date = total_time
            return self.end_date

    def finish_mission(self, mission: Mission):
        self.finished_mission(mission.mission_name)
        self._total_cost += mission.salary
        if len(self.mission_list) == 0:
            self._perfectly_done = True
