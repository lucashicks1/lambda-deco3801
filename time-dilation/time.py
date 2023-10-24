if __name__ == "__main__":
    time_now = input('what time is it now (hh:mm): ').split(':')
    time_new = input('what time should it be (hh:mm): ').split(':')

    time_now = (int(time_now[0]) * 60) + int(time_now[1])
    time_new = (int(time_new[0]) * 60) + int(time_new[1])

    time_diff = time_new - time_now

    print(time_diff * 60)
