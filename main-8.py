def get_int(msg, low=None, high=None):
    while True:
        val = input(msg)
        try:
            val = int(val)
        except ValueError:
            print("Please enter a valid whole number.")
            continue
        if low is not None and val < low:
            print(f"Value should not be less than {low}.")
            continue
        if high is not None and val > high:
            print(f"Value should not be more than {high}.")
            continue
        return val


def get_total_and_attended():
    while True:
        total = get_int("Total classes: ", low=1)
        attended = get_int("Classes attended: ", low=0)
        if attended > total:
            print("Attended classes can't be more than total classes.\n")
            continue
        return total, attended


def current_percentage(total, attended):
    return (attended / total) * 100


def future_percentage(total, attended, extra_attend, extra_miss):
    new_total = total + extra_attend + extra_miss
    new_attended = attended + extra_attend
    if new_total == 0:
        return 0
    return (new_attended / new_total) * 100


def classes_needed(total, attended, target):
    curr = current_percentage(total, attended)
    if curr >= target:
        return 0

    count = 0
    t, a = total, attended
    while (a / t) * 100 < target:
        t += 1
        a += 1
        count += 1
        if count > 100000:
            break
    return count


def option_current():
    total, attended = get_total_and_attended()
    percent = current_percentage(total, attended)
    print(f"Current attendance: {percent:.2f}%")


def option_target():
    total, attended = get_total_and_attended()
    target = get_int("Target percentage: ", low=0, high=100)

    curr = current_percentage(total, attended)
    print(f"Current attendance: {curr:.2f}%")

    if curr >= target:
        print("You already meet the target, no extra classes needed.")
        return

    n = classes_needed(total, attended, target)
    print(f"Classes required to reach target: {n}")


def option_future():
    total, attended = get_total_and_attended()
    extra_attend = get_int("Upcoming classes you will attend: ", low=0)
    extra_miss = get_int("Upcoming classes you will miss: ", low=0)

    curr = current_percentage(total, attended)
    fut = future_percentage(total, attended, extra_attend, extra_miss)

    print(f"Current attendance: {curr:.2f}%")
    print(f"Predicted attendance: {fut:.2f}%")


def show_menu():
    print("\nATTENDANCE SCENARIO CALCULATOR")
    print("1. Calculate current attendance")
    print("2. Find classes needed for target")
    print("3. Predict future attendance")
    print("4. Exit")


def main():
    while True:
        show_menu()
        choice = input("Enter choice: ").strip()

        if choice == "1":
            option_current()
        elif choice == "2":
            option_target()
        elif choice == "3":
            option_future()
        elif choice == "4":
            print("Exiting. Bye!")
            break
        else:
            print("Invalid choice, try again.")


main()
