#!/usr/bin/python3
""" Python script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress. """


if __name__ == "__main__":
    import requests
    from sys import argv

    us_id = argv[1]
    url1 = "https://jsonplaceholder.typicode.com/users/{}".format(us_id)
    url2 = "https://jsonplaceholder.typicode.com/todos?userId={}".format(us_id)

    name_resp = requests.get(url1).json()
    EMPLOYEE_NAME = name_resp.get('name')
    tasks_resp = requests.get(url2).json()
    TOTAL_NUMBER_OF_TASKS = len(tasks_resp)
    NUMBER_OF_DONE_TASKS = 0
    directory = []
    for i in tasks_resp:
        if i.get("completed") is True:
            directory.append(i.get("title"))
            NUMBER_OF_DONE_TASKS += 1
    print("Employee {} is done with tasks({}/{}):"
          .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for j in i:
        print("\t {}".format(j))
