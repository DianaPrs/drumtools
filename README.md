Drumtools
=========

With Drumtools you can find special drum notation for your favorite track in our database and create you're own laconic notation. Project was co-developed in my Learn Python course group. My main responsibillity was implementing the backend functionallity and some database component.The author of the idea and co-creator [Aleksandr Loschev](https://github.com/Loschev).

---
# Overview

Drumtools it is a web project, based on flask framework. Repo contains MVP web application, SQL database models, registration and authorization mechanism.

<img src="https://i.ibb.co/tJv10c7/Screenshot.png" alt="Screenshot" border="0">

# Basic functionality

Application indicate track name, artist, tempo of the composition and number of tacts. Every saving tact is uniq and contain notes. 

User can create a personal account with the ability to create and save tracks. Output feature was designed for comfortable printing result.

<a href="https://ibb.co/JvX7mCc"><img src="https://i.ibb.co/JvX7mCc/Screenshot-N.png" alt="Screenshot-N" border="0"></a>

# TODO

- Create advanced user interface for data input
- Feedback feature 
- Add MIDI support
- Notes recognition from pdf
- Import in other formats (.gp5 etc.)


# Local installation

To install localy clone repository and use `pip` comand

```
git clone https://github.com/DianaPrs/drumtools.git
pip install -r requirments.txt
```

