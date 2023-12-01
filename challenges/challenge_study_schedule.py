def study_schedule(permanence_period, target_time):
    try:
        students = 0

        for start, end in permanence_period:
            if start <= target_time <= end:
                students += 1

        return students

    except TypeError:
        return None
