# main.py

import grades

# Student Identity Configuration
LAST_NAME = "Vargas"
STUDENT_ID = "TUPM-25-0698"

SEED_DIGIT = int(STUDENT_ID[-1])
ID_SUM = sum(int(d) for d in STUDENT_ID if d.isdigit())
NAME_LENGTH = len(LAST_NAME)

#Generate student-unique scores
scores = [
    SEED_DIGIT * 10,
    ID_SUM % 100,
    NAME_LENGTH * 7
]

average = grades.compute_average(scores)
grade = grades.assign_grade(average)
remark = grades.generate_remark(grade)

print("=" * 40)
print(f"Student: {LAST_NAME}")
print(f"Student ID: {STUDENT_ID}")
print(f"Generated Scores: {scores}")
print(f"Average: {round(average,2)}")
print(f"Grade: {remark}")
print(f"Remark: {remark}")
print("=" * 40)

# main.py

from access_control import compute_access_level, validate_access, audit_log

# Constants
SEED_NUM = 8
FAVORITE_ARTIST = "SUD"
CONTROL_NUM = max(1, SEED_NUM)

# Decorated function to handle authorization workflow
@audit_log
def authorize(control, artist):
    level = compute_access_level(control, artist)
    if validate_access(level, control):
        return "ACCESS GRANTED"
    else:
        return "ACCESS DENIED"

# Execute authorization
decision = authorize(CONTROL_NUM, FAVORITE_ARTIST)
print("Decision:", decision)

from media_engine import signal_shutdown, play_count_stream, monitor

# Constants
SEED_NUM = 8
FAVORITE_ARTIST = "SUD"
CONTROL_NUM = max(1, SEED_NUM)
limit = CONTROL_NUM + len(FAVORITE_ARTIST)  # 8 + 3 = 11

# Decorated function to process the stream
@monitor
def process_stream(limit):
    total_plays = 0
    records_processed = 0
    for play in play_count_stream(limit):
        print(f"Play count record: {play}")
        total_plays += play
        records_processed += 1
    return {
        "Total Plays": total_plays,
        "Number of Records Processed": records_processed
    }

# Execute streaming analytics
stream_data = process_stream(limit)

# Display summary
for key, value in stream_data.items():
    print(f"{key}: {value}")