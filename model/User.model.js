const mongoose = require('mongoose');
const { Schema } = mongoose;
// const bcrypt = require('bcrypt');
const userSchema =new Schema({
    seller:String,
    lots: String,
    arrived: String,
    sold: String,
    max:String, //{ type: String,  required: true, },
    avg:String,// { type: String,  required: true, },
    time: String,
    day: String,
    month: String,
    year: String,
    date: String

}, {
    collection: 'today'
}  );

// userSchema.pre('save', async function (next) {
//     try {
//         // console.log("Bf Save")
//         const salt = await bcrypt.genSalt(10)
//         const hashedpassword = await bcrypt.hash(this.password, salt);
//         this.password = hashedpassword;

//     } catch (error) {
//         next(error)
//     }
// })
// userSchema.methods.isValidPassword = async function (password) {
//     try {
//         return await bcrypt.compare(password, this.password)
//     } catch (error) {
//         throw error
//     }
// }



// userSchema.post('save', async function (next) {
//     try {
//         console.log(" Date Saved")

//     } catch (error) {
//         next(error)
//    
// })






const today = mongoose.model('today', userSchema);





// User.find({day :15}, function(err, result) {
//     if (err) throw err;
//     if (result) 
//         consol.log(json(result))

// })

module.exports = today

// {

     
//         fetchData:function(callback){
//            var userData=userTable.find({});
//            userData.exec(function(err, data){
//                if(err) throw err;
//                return callback(data);
//            })
           
//         }
//    }
// }