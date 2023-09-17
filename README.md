<p align="center"><img src="https://github.com/Ashwinshankar98/TeachersPetBot/blob/main/images/teacherspet.png" alt="alt text" width=200 height=200>
  
  <h1 align="center"> Teacher's Pet Bot</h1>
  
<h2 align="center"> Streamline Your Class Discord</h1>


[![DOI](https://zenodo.org/badge/429658277.svg)](https://zenodo.org/badge/latestdoi/429658277)
![Python](https://img.shields.io/badge/python-v3.7+-brightgreen.svg)
![GitHub](https://img.shields.io/github/license/salonishah01/TeachersPetBot)
![GitHub issues](https://img.shields.io/github/issues/salonishah01/TeachersPetBot)
![GitHub closed issues](https://img.shields.io/github/issues-closed/salonishah01/TeachersPetBot)
![Lines of code](https://tokei.rs/b1/github/salonishah01/TeachersPetBot)
[![codecov](https://codecov.io/gh/salonishah01/TeachersPetBot/branch/main/graph/badge.svg?token=QTKU51PZSO)](https://codecov.io/gh/salonishah01/TeachersPetBot)
![GitHub deployments](https://img.shields.io/github/deployments/Ashwinshankar98/TeachersPetBot/discord-bot-phase2)<br/>

<h2>Software Engineering Project for CSC 510</h2>


Teacher's Pet is a Discord Bot for class instructors to streamline their Discord servers. Discord is a great tool for communication, and its functionalities can be enhanced by bots and integrations.


<h4>Charts</h4>
Instructors (like TAs and Professors) can quickly make graphs and charts directly in Discord to share with students or users. Instructors can use this feature to share grade distributions, lecture participation and attendance, or other course statistics. All charts are named and stored in a JSON file when they are created. Students have access to a command that allows them to view previously presented charts.

<p align="left"><img width=65% src="https://github.com/chandur626/TeachersPetBot/blob/update-readme/docs/media/charts.gif"></p>

<h4>Email Configuration</h4>

This feature enables users to configure their email address in the system to receive important notifications, attachments from professors, and assignment reminders. Users can also update, view, and unconfigure a configured email address through the system.

<p align="left"><img width=65% src="https://github.com/chandur626/TeachersPetBot/blob/update-readme/docs/media/email-address.gif"></p>

<h4>Email Interaction</h4>

This feature notifies all students regarding the next assignment deadline, which is due in a day, through email.

<p align="left"><img width=65% src="https://github.com/chandur626/TeachersPetBot/blob/update-readme/docs/media/email-reminder.gif"></p>

<h4>Re-Grading</h4>

This feature provides a way for students to submit regrade requests, and Instructors can collect information of the requests submitted. There are various commands included to add, update, display, and remove regrade requests.
This use case was based on a regrade request submission for CSE 510 SE FALL21 mid examination.

<p align="left"><img width=65% src="https://github.com/chandur626/TeachersPetBot/blob/update-readme/docs/media/Regrade.gif"></p>


<h4>Link Saving</h4>

This feature is helpful to save all the messages that contain important URLs. we have built a user command "!send_links"  This command lets users access all messages that contain URLs. The messages Containing URLs are automatically get appended in a file and the file is attached when the "!send_links" command is input.

<p align="left"><img width=65% src="https://github.com/chandur626/TeachersPetBot/blob/update-readme/docs/media/link-saving.gif"></p>

<h4>Project Event</h4>

This feature allows instructors or teaching assistants to create a project event by providing information such as description, link for project submission and deadline. The deadline reminder is taken care of Email Interaction feature.

<p align="left"><img width=65% src="https://github.com/chandur626/TeachersPetBot/blob/update-readme/docs/media/project-event.gif"></p>


<h4>Spam Detection</h4>
This feature is used to detect spam in message channels. When a user tries to send too many messages in the channel, it gives a warning. This is useful when multiple users are trying to send mutiple messages. The warning lets the student know that they have sent too many messages. 

<p align="left"><img width=65% src="https://github.com/chandur626/TeachersPetBot/blob/update-readme/docs/media/Spam-Detection.gif"></p>

<hr />

<a name="instrun"></a>
<h2> Installation and Running </h2>

#### Tools and Libraries Used
In addition to the packages from [requirements.txt](https://github.com/Ashwinshankar98/TeachersPetBot/blob/main/requirements.txt) which need to be installed, please have the following installed on your machine:
* [Python 3.9.7](https://www.python.org/downloads/)
* [Sqlite](https://www.sqlite.org/download.html)

To install and run Teacher's Pet, follow instructions in the [Installation and Testing Guide](https://github.com/Ashwinshankar98/TeachersPetBot/blob/main/Installation.md).


<a name="testing"></a>

<h2>Testing </h2>

To run tests on the Teacher's Pet, follow instructions in the [Installation and Testing Guide](https://github.com/Ashwinshankar98/TeachersPetBot/blob/main/Installation.md#Run-Tests).

<hr />

<a name="commands"></a>
<h2> Bot Commands </h2>

<h3> Bot commands from iteration III </h3>


:open_file_folder: [!regrade-request command](https://github.com/chandur626/TeachersPetBot/blob/main/docs/Regrade/Regrade.md)

:open_file_folder: [!update-request command](https://github.com/chandur626/TeachersPetBot/blob/main/docs/Regrade/Regrade.md)

:open_file_folder: [!remove-request command](https://github.com/chandur626/TeachersPetBot/blob/main/docs/Regrade/Regrade.md)

:open_file_folder: [!display-requests command](https://github.com/chandur626/TeachersPetBot/blob/main/docs/Regrade/Regrade.md)

:open_file_folder: [!chart command](https://github.com/chandur626/TeachersPetBot/blob/update-readme/docs/charts/charts.md)

:open_file_folder: [!check_chart command](https://github.com/chandur626/TeachersPetBot/blob/update-readme/docs/charts/check_chart.md)

:open_file_folder: [!create_email_command](https://github.com/chandur626/TeachersPetBot/blob/update-readme/docs/email_address/create_email.md)

:open_file_folder: [!view_email_command](https://github.com/chandur626/TeachersPetBot/blob/update-readme/docs/email_address/view_email.md)

:open_file_folder: [!update_email_command](https://github.com/chandur626/TeachersPetBot/blob/update-readme/docs/email_address/update_email.md)

:open_file_folder: [!remove_email_command](https://github.com/chandur626/TeachersPetBot/blob/update-readme/docs/email_address/remove_email.md)

:open_file_folder: [!project_event command](https://github.com/chandur626/TeachersPetBot/blob/update-readme/docs/events/project_event.md)

<br>
<h3> Bot commands from iteration I and II </h3>

`!setInstructor <@member>` Set a server member to be an instructor (Instructor command)

`!removeInstructor <@member>` Remove a server member from the instructor role (Instructor command)

`!getInstructor` Get the current instructors in the server

`!attendance` Find attendance from voice channel (Instructor command)

`!ask "<question>"` Ask a question  

`!answer <question_number> "<answer>"` Answer a question

`!poll <command>` Run a poll for students (Instructor command)

`!create` Start creating an event (Instructor command) 

`!oh enter` Enter an office hour queue as an individual student  

`!oh enter <group_id>` Enter an office hour queue with a group of students  

`!oh exit` Exit the office hour queue  

`!oh next` Go to next student in queue as an instructor (Instructor command)

`!help` Gets the descriptions for all commands

`!help <command>` Describes a command in detail

`!ping` Find the latency of network

`!stats` Gets the statistics of system and softwares used

<hr />

<a name="fscope"></a>

<h2> Future Scope </h2>

This bot has endless possibilities for functionality. Features which we are interested in adding but did not have time for include but are not limited to:

  * Custom Events
  * Allow events to be edited
  * Show error information on discord
  * Make Instructor commands private
  * Add new roles
  * Track participation and user ranking
  * Refactor code to use cogs
  * Save data charts on DB rather than locally in json
  * Store data based on user emote reactions to instructor messages

For a detailed description of each of the above future enhancements listed visit [Future Scope](https://github.com/chandur626/TeachersPetBot/projects/2).

<hr />


<h3> Team Members </h3>

[Romil Shah](https://github.com/romil2807)

[Rushil Vegada](https://github.com/rushilv20)

[Sahil Changlani](https://github.com/sahilchanglani)

[Saloni Shah](https://github.com/salonishah01)

<h3> Previous Authors </h3>

#### Chandrahas Reddy Mandapati
#### Sri Pallavi Damuluri
#### Niraj Lavani
#### Harini Bharata
#### Sandesh Aladhalli Shivarudre Gowda
