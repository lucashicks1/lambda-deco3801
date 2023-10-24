REAL_START = 17
REAL_END = 20
FAKE_START = 5
FAKE_END = 22.5

def in_minutes(hours):
    return(hours * 60)

if __name__ == "__main__":
    real_length = in_minutes(REAL_END) - in_minutes(REAL_START)
    fake_length = in_minutes(FAKE_END) - in_minutes(FAKE_START)

    minutes_per_minute = fake_length / real_length 

    
