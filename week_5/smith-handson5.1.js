/*
Author: Cliff Smith
Date: July 4, 2026
File Name: smith-handson5.1.js
Description: This file contains MongoDB shell queries for Hands-On 5.1 -
MongoDB Document Manipulation and Projections. Run these queries inside
the mongosh shell after connecting to the web355DB database.
*/

// a. Add a new user to the users collection
user = {firstName: 'Bryce', lastName: 'Wane', employeeId: 'BW123', email: 'bryce.wane@supermail.com', dateCreated: new Date()};
db.users.insertOne(user);

// Prove the new user was added successfully
db.users.findOne({firstName: 'Bryce'});

// b. Update Mozart's email address to mozart@me.com
db.users.updateOne({lastName: 'Mozart'}, {$set: {email: 'mozart@me.com'}});

// Prove Mozart's document was updated successfully
db.users.findOne({lastName: 'Mozart'});

// c. Display all users in the collection using projections
// Only show firstName, lastName, and email address
db.users.find({}, {firstName: 1, lastName: 1, email: 1});
