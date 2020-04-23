## User stories

* **As a user** I want to **be able to register** so that I can **have my own account.**

* **As a user** I want to **be able to login** so that I can **use the application.**

* **As a parent** I want to **create a group** for my family so that I can **keep track on how much housework my kids are doing**.

* **As a cleanin enthusiast** I want to **add different cleaning tasks** so that I can **mark if i have done them**.

* **As a kid** I want to **upload chores I have done** so that **my parents will reward me**.

* **As a part of a household** I want to **join a group** so that **I can be a part of it**.

* **As a flawed person** I want to **be able to edit a chore** so that I can **fix my mistake**.

* **As a person** I want to **be able to delete a chore** so that I **don't have unnecessary chores**.

* **As a student living in a shared flat** I want my roommates to **see how much housework I am doing** so that they can **realize they need to step up their game**.

## SQL-kyselyt

* Rekisteröityminen `INSERT INTO Account (date_created, date_modified, name, username, password, role) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, ?);`

* Kirjautuminen `SELECT * FROM Account WHERE Account.username = ? AND Account.password = ?;`

* Ryhmän lisäys `INSERT INTO Gang (date_created, date_modified, name, creator_id) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?)`

* Askareen lisäys `INSERT INTO Chore (date_created, date_modified, name, points, group_id) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?)`

* Askareen merkitseminen tehdyksi `INSERT INTO Instance (date, chore_id, account_id) VALUES (CURRENT_TIMESTAMP, ?, ?);`

* Ryhmään liittyminen `INSERT INTO Usergroup (user_id, group_id) VALUES (?, ?)`

* Askareen muokkaaminen `UPDATE Chore SET date_modified = CURRENT_TIMESTAMP, name = ?, points = ? WHERE id = ?;`

* Askareen poistaminen
`BEGIN;
  DELETE FROM Chore WHERE id = ?;
  DELETE FROM Instance WHERE chore_id = ?;
COMMIT;`

* Ryhmän jäsenten kokonaispisteiden näyttäminen
`SELECT Account.username, SUM(Chore.points) FROM Account
    LEFT JOIN Instance ON Instance.account_id = Account.id
    LEFT JOIN Chore ON Chore.id = Instance.chore_id
    WHERE Chore.group_id = :groupId
    GROUP BY Account.id`
