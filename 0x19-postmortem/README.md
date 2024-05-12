A postmortem
Requirements:

Issue Summary (that is often what executives will read) must contain:
duration of the outage with start and end times (including timezone)
what was the impact (what service was down/slow? What were user experiencing? How many % of the users were affected?)
what was the root cause
Timeline (format bullet point, format: time - keep it short, 1 or 2 sentences) must contain:

when was the issue detected
how was the issue detected (monitoring alert, an engineer noticed something, a customer complained…)
actions taken (what parts of the system were investigated, what were the assumption on the root cause of the issue)
misleading investigation/debugging paths that were taken
which team/individuals was the incident escalated to
how the incident was resolved
Root cause and resolution must contain:

explain in detail what was causing the issue
explain in detail how the issue was fixed
Corrective and preventative measures must contain:

what are the things that can be improved/fixed (broadly speaking)
a list of tasks to address the issue (be very specific, like a TODO, example: patch Nginx server, add monitoring on server memory…)
Be brief and straight to the point, between 400 to 600 words



Issue Summary:
Duration: May 10, 2024, 10:00 AM - May 10, 2024, 12:30 PM (UTC)
Impact: The user authentication service experienced intermittent outages, resulting in 30% of users being unable to log in during peak hours.
Root Cause: Database connection pool exhaustion due to a sudden increase in user activity.
Timeline:
10:00 AM: Issue detected through monitoring alerts indicating a spike in failed authentication attempts.
10:05 AM: The engineering team was notified of the issue.
10:10 AM: Investigation initiated, focusing on database performance and server logs.
10:30 AM: Initial assumption made that the issue might be related to a recent deployment.
11:00 AM: Escalation to database administrators for deeper analysis.
11:30 AM: Database administrators identified the database connection pool exhaustion as the root cause.
12:00 PM: Immediate measures were taken to increase the connection pool size and optimize database queries.
12:30 PM: Service is fully restored, and users can log in without any further issues.
Root Cause and Resolution:
Root Cause: The root cause of the issue was identified as database connection pool exhaustion. The sudden surge in user activity overwhelmed the existing connection pool capacity, leading to failed authentication attempts.
Resolution: To address the issue, the connection pool size was increased to accommodate higher traffic levels. Additionally, database queries were optimized to reduce the load on the database server during peak usage hours.




Corrective and Preventative Measures:
Improvements/Fixes:
Implement dynamic scaling for the database connection pool to automatically adjust based on traffic patterns.
Enhance monitoring and alerting systems to provide early detection of similar issues.
Conduct load testing to simulate peak traffic conditions and identify potential bottlenecks.
Tasks to Address the Issue:
Implement automated scaling for the database connection pool by next sprint.
Enhance monitoring alerts to include specific metrics related to database performance by end of the week.
Schedule regular load testing sessions to ensure system scalability and resilience by the end of the month.
