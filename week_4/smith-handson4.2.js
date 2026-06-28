/*
Author: Cliff Smith
Date: June 21, 2026
File Name: smith-handson4.2.js
Description: This file contains MongoDB shell queries for Hands-On 4.2 -
MongoDB Database Setup and Querying with MongoDB Shell. Run these queries
inside the mongosh shell after connecting to the web335DB database.
*/

// a. Display all users in the collection
db.users.find();

// b. Display the user with the email address jbach@me.com
db.users.findOne({ email: 'jbach@me.com' });

// c. Display the user with the last name Mozart
db.users.findOne({ lastName: 'Mozart' });

// d. Display the user with the first name Richard
db.users.findOne({ firstName: 'Richard' });

// e. Display the user with employeeId 1010
db.users.findOne({ employeeId: '1010' });
