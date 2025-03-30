//
// Copyright contributors to the agentic-ai-cyberres project
//

require('dotenv').config();

const mongoDBname = process.env.MONGODB_NAME;
const mongoDBcollection = process.env.MONGODB_COLLECTION_NAME;

// create connection string to connect to specific mongoDB database as specified in .env file by user
let connectionString = 'mongodb://localhost/' + mongoDBname; 

// connect to database
db = connect(connectionString);

// validate database which requires collection name
let validationString = 'db.' + mongoDBcollection + '.validate()'; 
printjson("Validating database " + mongoDBname + " and collection " + mongoDBcollection );
printjson( eval(validationString) );

