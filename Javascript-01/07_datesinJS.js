// Dates in JS

/**
 * Documentaion
 * @param {date} myDate - A date variable
 * @param {object} myNewDate - A custom date variable 
 */


// date is an object in js

let myDate = new Date();
console.log(myDate);
console.log(myDate.toDateString());
console.log(myDate.toISOString());
console.log(myDate.toLocaleDateString());
console.log(myDate.toString());
console.log();
// creating a new date
let myCreatedDate =  new Date(2023,0,8,6,10);
console.log(myCreatedDate.toString());
let myNewDate= new Date("08-01-2023")
console.log(myNewDate.toLocaleString());
console.log(myNewDate.getUTCDay());
//
let myTimeStamp = Date.now()
console.log(myTimeStamp);
console.log(myNewDate.getTime()); // return date in miliseconds
console.log("Time in seconds:");
console.log(Math.floor(Date.now()/1000)) // divide the date by 1000 to get it in seconds.
//Using floor to get a non-decimal number.
// 
// Date is an object.

console.log(`${myDate.getDay()} and time is idk XD`);
"This is a string"



