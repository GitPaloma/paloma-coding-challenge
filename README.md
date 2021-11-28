# Paloma Coding Challenge: Entertainment Library Manager

## Overview

This challenge is designed to test your full-stack programming skills, including

* Implementing front-end UI according to design specifications
* Building and modifying back-end APIs
* Working with databases
* Leveraging Third-party APIs

We're looking for code that is...

* Reusable
* Readable
* Extensible
* Modular

In this repository, we've initialized a full stack application and installed a few helpful frameworks that will hopefully avoid requiring you to reinvent the wheel. Below are the installed technologies, their role in the stack, and links to the parts of the documentation that can quickly get you up to speed on how they work if they are new to you:

* Flask - Backend API server [Quickstart & Basics](https://flask.palletsprojects.com/en/2.0.x/quickstart/) (10 min read)
* Tailwind - UI styling [Core Concepts](https://tailwindcss.com/docs/utility-first) (10 min read)
* NextJS - Basically React v16 w/ enhancements to improve routing and page load times [Tutorial](https://nextjs.org/learn/basics/create-nextjs-app?utm_source=next-site&utm_medium=nav-cta&utm_campaign=next-website) (\~15 min)
* React Query - Networking orchestration and client-side API data storage. [Overview and Simple Example](https://react-query.tanstack.com/overview) (5 min read)
* Axios - HTTP library for actually making the API (used by React Query)

Feel free to install or use other libraries as you see fit. If a knowledge gap in a pre-installed library becomes a blocker to completing the challenge, feel free to abandon it entirely. **We'd rather see a solution leveraging entirely different frameworks that meets all solution requirements, than a half-completed challenge that using only the pre-installed libraries.**

**If different commands or steps are required to install or run your final solution application, please add those instructions to the top of your solution README.**

### Submission

Once you've completed the challenge, please upload it to a public Github/Bitbucket and email the link to your interviewer. You must send over your solution at least 24hrs prior to the interview so that the interviewer has enough to review. Please also be able to run the solution locally so we can walk through your solution to the databases section on your machine (over screen share).

## Setup

### Fork the Repo

If you have not already, it is highly recommended you fork the original repository so you have your own version. You'll need to commit actual code and the original repository is **readonly**.

## Running the apps
### Using Docker
(from the root directory)
```bash
docker-compose up
```

### Running outside of docker
#### Install and Run Backend Development Server
(from the `flask-backend` directory)
```bash
cd flask-backend
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
export FLASK_APP=app.py
flask run
```

To restart the backend server after making code changes later on, you only need to run...
(from the `flask-backend` directory)
```bash
. venv/bin/activate
export FLASK_APP=app.py
flask run
```

#### Install and Run Frontend Development Server

If you don’t have Node.js installed, [install it from here](https://nodejs.org/en/). You’ll need Node.js version 10.13 or later.

(from the `react-frontend` directory)
```bash
npm ci
npm run dev
```

Then navigate to [http://localhost:3000](http://localhost:3000) to see the app.

### What you're starting with

You should see a list of movies and tv shows. Displaying this data to you involves provides examples of how each part of the stack works:

Before you even open your browser...

* The raw data for these titles is sitting in a static json file called `titles.json`
* Flask running on port 5000 has one API route implemented, `GET /api/content`, which serves up that data when called

When you navigate http://localhost:3000 in your browser...

* NextJS matches the route `/` based on file location within the `pages` directory, in this case matching to `index.js` and rendering the `Home` Component exported from that file
* React Query `useQuery` hook is orchestrating a call to the `api/content` API and storing the received data in its `queryClient` (leveraging Axios HTTP library to actually make the API call).
* The `entries` field of the received data is then styled (responsively) using Tailwind. (try changing your browser width!)

## The Challenge

You are the developer on Paloma's new Entertainment Library Manager! Users rely on the Entertainment Library Manager to know exactly what content is available on Blu-ray in the Paloma NYC offices (very cutting edge tech). Your task is to finish building the infrastructure and add some final high-value features to get the application ready for launch.

### Part One: Initialize and Load a Database

Start by initializing a development database and loading the data from `titles.json` into it. You can use any database language or type. The database does not have to be running locally on your computer, but you must be able to issue it commands and manipulate the data at will (i.e. no abstracted / WYSIWYG storage systems such as [Parse](https://parseplatform.org/)).

### Part Two: Application Enhancements

Next implement the below features enhancements into the application. The features should be built in this order, and each feature should get its own PR. The title of the PR should be the feature name, but the PRs don't need descriptions or anything else inside them.

* *Filtering:* Create two new API endpoints, `api/movies` and `api/tv`, which return only the titles with `programType` of `movie` and `series` respectively. Then, add a dropdown to the UI that allow users to filter either of the two types or show all titles.
* *Search:* Allow a `search` string phrase to be passed into any of the three API endpoints as a query param. When passed in, only return titles where the search phrase appears in the `title` or `description` fields. Add a search bar to the UI that allows the user to enter input to leverage this searching capability.
* *Search Error:* If `search` is passed into API but no titles match, return a 404 error. In the UI, show an error to the user "No titles found. Please try searching something else."
* *Connect to DB:* Refactor the Flask app to leverage the database you initialized in Part 1 instead of the static file.
* *Create new Title:* Add a "+" button to the UI that allows the user to input new titles to be added to the database. Users should be able to specify values for all the fields. Once the user finished submitting the information for my new title it should immediately show up in the list.
