# ⏱️ Time Calculator

This project includes a Python function that adds a time duration to a given start time and optionally includes the day of the week. It returns the updated time, including day shifts and formatting for readability.

## 🧠 What It Does

The function `add_time(start, duration, day=False)`:
- Adds a duration (in hours and minutes) to a start time in **12-hour AM/PM format**
- Optionally takes a starting **day of the week**
- Handles rollovers into the next day or multiple days later
- Returns a string formatted as a new time, with correct day and note of day count passed

### ✅ Example Calls

```python
add_time("3:00 PM", "3:10")
# Returns: "6:10 PM"

add_time("11:30 AM", "2:32", "Monday")
# Returns: "2:02 PM, Monday"

add_time("10:10 PM", "3:30")
# Returns: "1:40 AM (next day)"

add_time("6:30 PM", "205:12")
# Returns: "7:42 AM (9 days later)"
📌 Features
🕒 12-hour clock format (AM/PM)

🗓️ Optional support for weekday input/output

🧮 Handles multi-day duration rollover

❌ No external libraries used — 100% native Python

⚙️ Parameters
python
Copy
Edit
add_time(start, duration, day=False)
start: String — e.g., '3:00 PM'

duration: String — e.g., '3:10'

day: (optional) String — e.g., 'Monday'

🔧 Tech Used
Python 3

Manual string and time calculations

Conditional logic and date math
