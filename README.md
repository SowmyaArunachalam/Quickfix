
#### What each config file is for, and what breaks if you accidentally put a secret in common_site_config.json

site_config.json is used to store configuration of a specific site within the bench and holds the db_name, db_password, db_type, encryption_key to encrypt and decrypt sensitive data.

common_site_config.json holds the global configuration for all the sites for a particular bench. It holds socketio, redis(cache, queue, socketio) background and gunicorn worker configurations.

The config.py handles the fetching data from site_config and common_site_config files. If the same data available in both the json file, the data in site_config.json file is prefered. If bench has 2 sites and both the site needed access of a secret key which was only specified in common_site_config.json then it might cause security risks and all sites in the bench may use the same credentials, which can cause business errors and data leaks.
____

#### List the 4 processes bench start launches (web, worker, scheduler, socketio) and explain what happens to background jobs if the worker process crashes

Web will handle the Http Requests.
Worker will handle the background jobs from the Redis queue.
Scheduler will trigger the scheduled events.
Socket.io handle relation between server and client. The client will subscribe to an event and the server will publish the data to the client when an event occurs.

If the worker process crashes, the job will be queued in the redis, which cause delay or failure of the jobs but jobs are not get executed until the worker get restarted
____

#### When a browser hits /api/method/quickfix.api.get_job_summary - what Python function handles this request and how does Frappe find it?

Every request will enters to application() function in the frappe/app.py file ehich handles different type of requests. It first initialize the connection, authenticate the user and check for the type of request. The request starts with /api will be passed to API handler (handle() function) in the frappe/api/__init__.py.
____

#### When a browser hits /api/resource/Job Card/JC-2024-0001 - what happens differently compared to /api/method/?

The /api/method/ will call the whitelisted method and api/resource/Job Card/JC-2024-0001 it will denote specific record of a doctype these are handled in the handle() function in the frappe/api/__init__.py
___

#### When a browser hits /track-job - which file/function handles it and why?

The get_response() function in the serve.py file handles the Portal pages, Static Pages, List Pages etc. It was only used to render website based API calls.
____
#### Open your Frappe site in browser devtools. Find the X-Frappe-CSRF-Token in a POST request. Where does this value come from and what would happen if you omitted it?

The CSRF token can be found in the headers of a request in the Networks tab. When a user session is created, the token is generated in the generate_csrf_token() function in the sessions.py file. Ths CSRF token is used to verify the incoming request is from trusted website when the csrf token omitted security leaks can be obtained like unauthorized requests, data modification. 
_____

#### In bench console, run: import frappe; frappe.session.data and describe what it contains

It returns the details of the login user like user, email, name.
___
#### With developer_mode: 1 - trigger a Python exception in one of your whitelisted methods. What does the browser receive?

The browser receive the entire details of the errors with tracebacks
____
#### Set developer_mode: 0 - repeat. What does the browser receive now? Why is this important for production?

The browser receive the entire details of the errors with tracebacks. Because in the response.py file, on the os level the DEV_SERVER environment variable is set to 1 on the development server. So the tracebacks gets allowed even on the developer_mode to 0.

___
#### Where do production errors go if they are hidden from the browser?

In the response.py file, on the os level the DEV_SERVER environment variable is set to 1 on the development server. So the tracebacks gets allowed even on the production errors. The production errors are logged into the Error log.
___




