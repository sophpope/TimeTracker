# Time Tracker

#### A productivity time tracking application that automatically records how much time is spent in different applications and browser tabs.

#### The app tracks the active window on the user's computer. When switching to another application, website or tab the current session ends and a new session begins. Each session is saved to the database with the details i.e. 'Microsoft Word - Document 2' or 'Code - main.py TimeTracker' along with the durations in seconds and the start and end date and time.

#### The project is built to help users easily understand where there time goes during the day, whilst on their computers without the need of manually stopping and starting timers. 


## Features

* Automatically detects the active application or browser tab.
* Starts a new tracking session when the active window changes
* Stops previous session when the user switches windows
* Stores session data in the database
* Allows tracked data to be viewed later

## Example use case 

#### A user may spend their morning switching between VS Code, Chrome and documentation whilst working on a project.

#### This app will record the sessions 

#### Google Chrome | www.canva.com | 1500secs | 09:00 - 09:25 | 25-10-2025

#### Code | autotimer.py - TimeTracker | 1800secs | 09:25 - 09:55 | 25-10-2025

#### Microsoft Word | Document 1 | 900 secs | 09:55 - 10:10 | 25-10-2025

#### This helps the user see how much time was spent coding, researching, browsing etc. 

## Tech Stack

* Python
* MySQL

## Improvement Ideas

### Front End Dashboard

#### User-friendly dashboard, so the users can easily view the tracked time entries more easily

* View total time spent per application
* Filter sessions by day, week or month
* Filter sessions by application

### Grouping & Categories

#### Add the ability to group together related sessions, when working on a project

### Manual Editing

#### Allow users to edit or rename sessions if the sutomatic title is unclear.

