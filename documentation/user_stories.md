## User stories

* **As a user** i want to **be able to register** so that i can **have my own account.**

* **As a user** i want to **be able to login** so that i can **use the application.**

* **As a parent** i want to **create a group** for my family so that i can **keep track on how much housework my kids are doing**.

* **As a cleanin enthusiast** i want to **add different cleaning tasks** so that i can **mark if i have done them**.

* **As a kid** i want to **upload chores i have done** so that **my parents will reward me**.

* **As a appreciative person** i want to **give different points to different chores** so that i can **appreciate people doing more laborious chores**.

* **As a flawed person** i want to **be able to edit a chore** so that i can **fix my mistake**.

* **As a person** i want to **be able to delete a chore** so that i **don't have unnecessary chores**.

* **As a musician** i want to **have different groups** so that i can **keep track of chores in my home and in my recording studio separately**.

* **As a student living in a shared flat** i want my roommates to **see how much housework i am doing** so that they can **realize they need to step up their game**.

## SQL-kyselyt

* Rekisteröityminen `INSERT INTO Account (date_created, date_modified, name, username, password, role) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, ?);`

* Kirjautuminen `SELECT * FROM Account WHERE Account.username = ? AND Account.password = ?;`

* Ryhmän lisäys `INSERT INTO Gang (date_created, date_modified, name, creator_id) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?)`

* Askareen lisäys `INSERT INTO Chore (date_created, date_modified, name, points, group_id) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?)`

* Askareen merkitseminen tehdyksi `INSERT INTO Instance (date, chore_id, account_id) VALUES (CURRENT_TIMESTAMP, ?, ?);`

* Askareen muokkaaminen `UPDATE Chore SET date_modified = CURRENT_TIMESTAMP, name = ?, points = ? WHERE id = ?;`

* Askareen poistaminen
`BEGIN;
  DELETE FROM Chore WHERE id = ?;
  DELETE FROM Instance WHERE chore_id = ?;
COMMIT;`

* Ryhmien listaus `SELECT Gang.name, Gang.id, Account.username FROM Account, Gang WHERE Gang.creator_id = Account.id;`

* Ryhmän jäsenten kokonaispisteiden näyttäminen
`SELECT Account.username, SUM(Chore.points) FROM Account
    LEFT JOIN Instance ON Instance.account_id = Account.id
    LEFT JOIN Chore ON Chore.id = Instance.chore_id
    WHERE Chore.group_id = :groupId
    ROUP BY Account.id`
