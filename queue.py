def find(tasks, time_slice):
    queue = []
    for i in range(len(tasks)):
        queue.append([i + 1, tasks[i]])  

    run_count = 0

    while len(queue) > 0:
        task = queue.pop(0)
        task_num = task[0]
        time_left = task[1]

        if time_left > time_slice:
            print("Task", task_num, "runs for", time_slice, "units.")
            queue.append([task_num, time_left - time_slice])
        else:
            print("Task", task_num, "runs for", time_left, "units.")

        run_count += 1

    print("Total runs taken:", run_count)


tasks = [10, 5, 8]
time_slice = 4

print("Output:\nTest Case 1:")
find(tasks, time_slice)
