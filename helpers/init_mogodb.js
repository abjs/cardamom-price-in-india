// const MongoClient = require('mongodb').MongoClient;
require('dotenv').config();
const uri =process.env.MONGODB_URL

// const util =require('util')
const mongoose = require('mongoose');
mongoose
.connect(uri,{
    dbName: process.env.DBNAME,
    useNewUrlParser: true ,
    useUnifiedTopology: true ,
    // useFindAndModify : true ,
    // useCreateIndex : true
})
// .then(() => {
//     console.log('mongoose connected')
// })
.catch((err)=>{
    console.log(err)
})
const connection = mongoose.connection
mongoose.connection.on('connected',()=>{
    console.log('mongoose connected')
})

mongoose.connection.on('error',(err)=>{
    console.log(err.message)
})

mongoose.connection.on('disconnected',(err)=>{
    console.log('mongoose disconnected')
})

process.on('SIGINT',async ()=>{
    await mongoose.connection.close()
    process.exit(0)
})

module.exports =connection