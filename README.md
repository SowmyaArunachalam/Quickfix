
#### What each config file is for, and what breaks if you accidentally put a secret in common_site_config.json

site_config.json is used to store configuration of a specific site within the bench and holds the db_name, db_password, admin_password configuration.

common_site_config.json holds the global configuration for all the sites in that particular bench. It holds socketio, redis(cache, queue, socketio) background and gunicorn worker configurations.

Placing a secret in the common_site_config.json can cause security risks, and all sites in the bench may use the same credentials, which can cause business errors and data leaks.
____

#### List the 4 processes bench start launches (web, worker, scheduler, socketio) and explain what happens to background jobs if the worker process crashes

Web will handle the Http Requests.
Worker will handle the background jobs from the Redis queue.
Scheduler will trigger the scheduled events.
Socket.io handle relation between server and client. The client will subscribe to an event and the server will publish the data to the client when an event occurs.

If the worker process crashes, the job will be queued in the redis, which cause delay or failure of the jobs but jobs are not get executed until the worker get restarted
____

