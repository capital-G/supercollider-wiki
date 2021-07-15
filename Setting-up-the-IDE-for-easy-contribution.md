In order to simplify changing class files or help files and then contributing back the changes, it’s easier to work directly with the git class library and schelp files tracked by git instead of the ones in the installation folder.  
To do this we can use the _LanguageConfig_ feature:

In the IDE go to `edit` > `preferences` > `interpreter` then set the following options:

(in this example the username is `JohnDoe` and SuperCollider repository was checked out inside `sc-dev` directory, replace those with yours) 

#### OSX:

- include paths:

`/Users/JohnDoe/sc-dev/supercollider/SCClassLibrary`

- exclude paths:

`/Users/JohnDoe/sc-dev/supercollider/build/Install/SuperCollider/SuperCollider.app/Contents/Resources/SCClassLibrary`

#### Linux:

- include paths:

`/home/JohnDoe/sc-dev/supercollider/SCClassLibrary`

- exclude paths:

`/usr/local/share/SuperCollider/SCClassLibrary`