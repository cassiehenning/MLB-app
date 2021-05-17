# MLB-app
Sends you a customized email every week, with information on your favorite MLB league, division and player.

## Setup
Fork this repo and clone it onto your local computer (for example to your Desktop), then navigate there from the command-line:

```sh
cd MLB-app
```

Create and activate a new Anaconda virtual environment, perhaps named "mlb-env":

```sh
conda create -n mlb-env python=3.7
conda activate mlb-env
```

Then, from within the virtual environment, install package dependencies:

```sh
pip install -r requirements.txt
```

Obtain API Keys from SendGrid services. Create a new file called ".env" in the root directory of this repo, and paste the following contents inside, using your own values as appropriate:

## .env example

```sh
APP_ENV="development" # or set to "production" on Heroku server
ALPHA_VANTAGE_API_KEY="___________"
SENDGRID_API_KEY="_______________"
MY_EMAIL_ADDRESS="hello@example.com"
MY_NAME="Jon Snow"
IMPORTANT: remember to save the ".env" file 
```

# Usage
From within the virtual environment, ensure you can run the following file and see it produce their desired results of sending an example email

```sh
python -m app.email_service # note the module-syntax invocation
```

#> SENDING EMAIL TO ...
NOTE: the Sendgrid emails might first start showing up in spam, until you designate them as coming from a trusted source (i.e. "Looks Safe")

As long as each of those scripts works by itself, you can send the email:

```sh
python -m app.service # note the module-syntax invocation
```

## Deployment to Heroku
Install Heroku CLI and login

# Server Setup
In the command-line, create a new application server:

```sh
heroku create mlb-app
```

# Verify the creation of the app:

heroku apps
Verify the local repo was associated with a remote address called "heroku":

```sh
git remote -v
```

# Server Configuration
Before we copy the source code to the remote server, we need to configure the server's environment in a similar way we configured our local environment.

Instead of using a ".env" file, we will directly configure the server's environment variables by either clicking "Reveal Config Vars" from the "Settings" tab in your application's Heroku dashboard, or from the command line (instructions below):
# or, alternatively...

# get environment variables:
heroku config # at this time, results might be empty-ish

# set environment variables:

```sh
heroku config:set APP_ENV="production"
heroku config:set SENDGRID_API_KEY="_________"
heroku config:set MY_EMAIL_ADDRESS="someone@gmail.com"
heroku config:set MY_NAME="Jon Snow"
```
At this point, you should be able to verify the production environment has been configured with the proper environment variable values:

```sh
heroku config
```

# Deploying
After this configuration process is complete, you are finally ready to "deploy" the application's source code to the Heroku server:

```sh
git push heroku master
```

NOTE: any time you update your source code, you can repeat this deployment command to upload your new code onto the server

# Running the Script
Once you've deployed the source code to the Heroku server, login to the server to see the files there, and take an opportunity to test your ability to run the script that now lives on the server:

heroku run bash # login to the server
... ls -al # optionally see the files, nice!
... python -m app.service # see the output, nice!
... exit # logout

## or alternatively, run it from your computer, in "detached" mode:

```sh
heroku run "python -m app.MLB"
```

## Scheduling the Script
Finally, provision and configure the server's "Heroku Scheduler" resource to run the notification script at specified intervals, for example once per day.

From the "Resources" tab in your application's Heroku dashboard, search for an add-on called "Heroku Scheduler" and provision the server with a free plan.

Finally, click on the provisioned "Heroku Scheduler" resource from the "Resources" tab, then click to "Add a new Job". When adding the job, choose to execute the designated python command (python -m app.MLB) at a scheduled interval (e.g. every week), and finally click to "Save" the job:

## Testing
Run tests
```sh
pytest
```