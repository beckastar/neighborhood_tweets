neighborhood_tweets
===================

As of 9/11/2013:

This engine uses the Twitter Api to collect and analyze tweets originating from and about San Francisco, separates the text, and quantifies local preoccupations.

On a server, the code is scheduled using cronjobs, and teh data is scheduled (also on cronjobs) to be aggregated 
every week, month, and year to determine changes in local concerns. 

This project uses a Flask framework, with a backend in SQlite3, a frontend in Javascript with Google Charts, and the rest 
of the code in Python. 
