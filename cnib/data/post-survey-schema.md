# Post Survey Schema

Source: `post-survey-responses.csv` (33 responses)

| Column | Data Type |
|--------|-----------|
| ID | integer |
| Start time | datetime (M/D/YY H:MM:SS) |
| Completion time | datetime (M/D/YY H:MM:SS) |
| Email | text (all "anonymous") |
| Name | text (all blank) |
| Language | text (mostly blank; some "English (United States)?", "Français (Canada)?") |
| Last modified time | text (all blank) |
| Did you go through the entire 6 week Assistive Technology Academy program? | categorical binary — Yes / No |
| How much more confident do you feel using assistive technology in a work setting now compared to before the Assistive Technology Academy? | ordinal Likert — Not at all confident / Somewhat confident / Very confident / Extremely confident |
| How effective were the morning lectures in reinforcing your learning of assistive technology? | ordinal Likert — Not very effective / Somewhat effective / Very effective |
| Do you have any comments on our lectures…? | free text |
| How effective were the afternoon labs or Friday practice Labs in reinforcing your learning of assistive technology? | ordinal Likert — Not effective at all / Not very effective / Somewhat effective / Very effective |
| Do you have any comments on our labs…? | free text |
| Did the homework assignments, workbook and capstone project help reinforce your learning of assistive technology? | ordinal Likert — Not at all / Not really / Somewhat / Yes, definitely |
| Do you have any comments on our homework, workbook or capstone project…? | free text |
| How often did you practice using your assistive technology outside of the program sessions? | ordinal frequency — Never / Rarely / Several times a week / Daily |
| What was the most valuable part of the program for you? | free text |
| What could we improve to make future offerings of the Assistive Technology Academy more effective? | free text |
| Are there any additional resources or support that you would have liked during the Assistive Technology Academy? | free text |

## Summary

- 19 columns total
- 5 metadata (ID, timestamps, email, name, language)
- 4 ordinal Likert scales
- 1 binary categorical
- 5 open-ended free text
- 4 effectively empty/unused (Name, Language mostly, Last modified time, Email always "anonymous")
