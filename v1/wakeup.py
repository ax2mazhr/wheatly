# Case: Work, Sleep, Appointment, Nap
#
# I/O:
#     > Work || Current: I/ Time, Margin(OPTIONAL), Slot(OPTIONAL), Bus(OPTIONAL)
#                        O/ Set Multiple Alarms, Lights, Media, Phone Volume
#
#            || Present: O/ Alarms, Weather, ETA, Time Left, Reminders, E-Mails, News, Media
# ============================================================================================
#     > Appointment || Current: I/ Arrival Time, Location, Margin(OPTIONAL)
#                               O/ Set Multiple Alarms, Lights, Media, Phone Volume
#
#                   || Present: O/ Alarms, Weather, ETA, Time Left, Reminders, E-Mails, News, Media
# ============================================================================================
#     > Sleep || Current: I/ Time
#                         O/ Set Multiple Alarms, Lights, Media, Phone Volume
#
#             || Present: O/ Alarms, Weather, Reminders, E-Mails, News, Media
# ============================================================================================
#     > Nap || Current: I/ Time, Duration(OPTIONAL)
#                       O/ Set Multiple Alarms, Lights, Media, Phone Volume
#
#           || Present: O/ Alarms, Reminders, Media
#
# Notes:
#   *When woken up and speak, greet and output.
#   *Cancel All alarms in range
