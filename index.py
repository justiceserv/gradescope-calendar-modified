from gradescopecalendar.gradescopecalendar import GradescopeCalendar
import datetime
import logging
import os

# Personal note: GradeScopeCalendar Library has been modified. 
# Modified Files are: gradescopecalendar.py, gradescope/account.py, calendars/gcal.py

# Account Information (OS Envrionment Variables)
EMAIL = os.environ.get("GSC_PW")
PASSWORD = os.environ.get("GSC_EM")
GCAL_ID = os.environ.get("GSC_CI")
IS_INSTRUCTOR = False
LOGGING_ENABLED = True
LOGGING_LEVEL = logging.DEBUG

# Start Logging 
logger = logging.getLogger("gradescopecalendar" if LOGGING_ENABLED else None)
logger.setLevel(LOGGING_LEVEL)
logger.debug(f"Log of Gradescope Automation @ {datetime.datetime.now()}")

# GradeScope Active CIDS 
ACTIVE_CID = ["816017", "816467"]
calendar = GradescopeCalendar(EMAIL, PASSWORD, IS_INSTRUCTOR, ACTIVE_CID)
calendar.write_to_gcal(GCAL_ID)