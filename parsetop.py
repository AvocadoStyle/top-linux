import csv
import json
from exceptions.Ilegalarg import IlegalArgumentException


class Parser:
    def __init__(self, csv_file_path, json_file_path):
        self.csv_file_path = csv_file_path
        self.json_file_path = json_file_path
        self.users = []
        self.TOPIC = ['PID', 'USER', '%MEM', 'COMMAND']
        self.MEM_MAX = 5 #include 0

    def __load_csv_file_into_arr(self):
        """
        loads the csv file into the users array
        complexity:
        1.) time complexity of O(N)
        2.) space complexity of O(N) with array, so the data is in sequence inside the memory.
            option to make the space complexity better O(1): i could
            not using `self.users` and save the data directly to the `.json` file and make the space complexity to O(1).
            the reason i did that its because i want to save the data inside a `buffer` for farther usage
        :return:
        """
        with open(self.csv_file_path) as csv_file:
            csv_read_row = csv.DictReader(csv_file)
            for rows in csv_read_row:
                self.users.append(rows)

    def create_json_file(self):
        """
        uses `__load_csv_file_into_arr(self)` method
        complexity:
        1.) as i wrote there
        2.) as i wrote there
        :return:
        """
        self.__load_csv_file_into_arr()
        with open(self.json_file_path, 'w') as json_file:
            json_file.write(json.dumps(self.users, indent=4))

    def __is_valid_topic(self, by_topic_value):
        """
        is it a valid topic inside `self.TOPIC final property`
        :param by_topic_value:
        :return: boolean
        """
        return by_topic_value in self.TOPIC

    def print_topic(self, by_topic_value):
        """
        Generic method print all the values of a topic.
        :return:
        """
        if not self.__is_valid_topic(by_topic_value):
            raise IlegalArgumentException("not a right topic name")

        print(str.lower(by_topic_value)+ "s are: ")
        for topic in self.users:
            print(topic[by_topic_value])

    def __print_command_for_specific_topic(self, by_topic_value, specific_id_topic):
        """
        Generic function, "by_topic_value" is gonna decide by what section we will print the commands.
        (for example the question asked from us by the `USER`, or by `PID`, or by `MEM`).
        :param by_what: `USER` or `PID` or `MEM`
        :return:
        """
        if not self.__is_valid_topic(by_topic_value):
            raise IlegalArgumentException("not a right topic name")

        print("for " + str.lower(by_topic_value) + " named " + specific_id_topic)
        for attended in self.users:
            if attended[by_topic_value] == specific_id_topic:
                print(attended[self.TOPIC[3]])
    def print_commands_for_specific_pid_topic(self, specific_id_topic):
        self.__print_command_for_specific_topic('PID', specific_id_topic)

    def __get_mem(self, mem):
        return mem.get('%MEM')

    def print_top_five_mem_usage(self):
        length = self.MEM_MAX
        if len(self.users) < self.MEM_MAX:
            length = len(self.users)
        self.users.sort(key=self.__get_mem, reverse=True)
        # print(self.users, end='\n\n')
        print("top 5 %MEM commands: ")
        for i in range(length):
            print(self.users[i][self.TOPIC[3]])

