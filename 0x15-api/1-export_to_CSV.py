#!/usr/bin/python3
""" extend your Python script to export data in the CSV format. """


if __name__ == '__main__':
    import requests
    from sys import argv

    us_id = argv[1]
    url1 = "https://jsonplaceholder.typicode.com/users/{}".format(us_id)
    url2 = "https://jsonplaceholder.typicode.com/todos?userId={}".format(us_id)

    name_resp = requests.get(url1).json()
    EMPLOYEE_NAME = name_resp.get('username')
    tasks_resp = requests.get(url2).json()
    filename = "{}.csv".format(us_id)
    with open(filename, "w", encoding="utf-8") as MyFile:
        for i in tasks_resp:
            TASK_COMPLETED_STATUS = i.get("completed")
            TASK_TITLE = i.get("title")
            MyFile.write('"{}","{}","{}","{}"\n'.format(
					us_id, EMPLOYEE_NAME, TASK_COMPLETED_STATUS, TASK_TITLE))
