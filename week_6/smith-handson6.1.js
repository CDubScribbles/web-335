/*
Author: Cliff Smith
Date: July 25, 2026
File Name: smith-handson6.1.js
Description: This file contains MongoDB shell queries for Hands-On 6.1 -
Aggregate Queries. These queries operate on the houses and students
collections, loaded via houses.js. Run these queries inside the mongosh
shell after connecting to the web355DB database.
*/

// a. Display all students
db.students.find();

// b. Add a new student to the students collection
newStudent = {"firstName": "Gladwynne", "lastName": "Merdraine", "studentId": "s1019", "houseId": "h1010"};
db.students.insertOne(newStudent);

// Prove the new student was added successfully
db.students.findOne({firstName: 'Gladwynne'});

// c. Update one of the new student's properties (transfer to Ravenclaw)
db.students.updateOne({firstName: 'Gladwynne'}, {$set: {houseId: 'h1009'}});

// Prove the property was updated successfully
db.students.findOne({firstName: 'Gladwynne'});

// d. Delete the student created in step b
db.students.deleteOne({firstName: 'Gladwynne'});

// Prove the student was removed successfully
db.students.findOne({firstName: 'Gladwynne'});

// e. Display all students by house (Houses -> Students)
db.houses.aggregate([
  { $lookup: { from: "students", localField: "houseId", foreignField: "houseId", as: "students" } }
]);

// f. Display all students in house Gryffindor (Gryffindor -> Students)
db.houses.aggregate([
  { $match: { houseId: 'h1007' } },
  { $lookup: { from: "students", localField: "houseId", foreignField: "houseId", as: "students" } }
]);

// g. Display all students in the house with an Eagle mascot (House -> Students)
db.houses.aggregate([
  { $match: { mascot: 'Eagle' } },
  { $lookup: { from: "students", localField: "houseId", foreignField: "houseId", as: "students" } }
]);
