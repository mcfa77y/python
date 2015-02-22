x detect newly engaged paid users since the last successful run of the tool.
  - UserPreference
x send a request data to Delighted with a REST API. This will cause an NPS email to be sent
  - post request
x a log should be kept of when the tool was run, the number of records synced, and the status of the export run
  - new log
x send email with the above info when the tool is run on both success and failure. This does not have to be code; the cron can mail out the error messages
  - sendEmail
x provide flags to override the last successful run date and run-to date (which is normally "now".) This will allow the tool to be re-run for a certain date range.
  this is not a flag but rather a url that you can hit to initiate the cron job

x provide a verbose mode to debug the tool and API calls
  - added debug mode and verbose for failed

x the above query was used to do an initial NPS survey to ~550 users. The initial survey user list is in delighted_users_20130319.csv if you need to flag these as having received the NPS survey.

  - added markEmailAsSentFromCSV fn