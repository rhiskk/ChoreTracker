# Tietokantakaavio ja CREATE TABLE-lauseet

### Tietokantakaavio
<img src="https://github.com/HiskiR/ChoreTracker/blob/master/documentation/database_diagram.png">

### CREATE TABLE-lauseet
<pre>
  CREATE TABLE account (
	id INTEGER NOT NULL,
	date_created DATETIME,
	date_modified DATETIME,
	name VARCHAR(144) NOT NULL,
	username VARCHAR(144) NOT NULL,
	password VARCHAR(144) NOT NULL,
	role VARCHAR(144) NOT NULL,
	PRIMARY KEY (id),
	UNIQUE (username)
  );
</pre>

<pre>
CREATE TABLE gang (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	creator_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(creator_id) REFERENCES account (id)
);
</pre>

<pre>
CREATE TABLE chore (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	points INTEGER NOT NULL, 
	group_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(group_id) REFERENCES gang (id)
);
</pre>

<pre>
CREATE TABLE usergroup (
	user_id INTEGER, 
	group_id INTEGER, 
	FOREIGN KEY(user_id) REFERENCES account (id), 
	FOREIGN KEY(group_id) REFERENCES gang (id)
);
</pre>

<pre>
CREATE TABLE instance (
	id INTEGER NOT NULL, 
	date DATETIME, 
	account_id INTEGER NOT NULL, 
	chore_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(account_id) REFERENCES account (id), 
	FOREIGN KEY(chore_id) REFERENCES chore (id)
);
</pre>
