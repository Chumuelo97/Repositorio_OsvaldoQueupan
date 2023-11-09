import mongoose from 'mongoose';
import values from '../const/const.js';

const uriMongoLocal = 'mongodb://localhost:27017/BaseDatos' //pones la Url que te entrega en la app de mongo

mongoose.connect( uriMongoLocal, {
}).catch( error => 
   
    console.log(error) );

const connection = mongoose.connection;

connection.once( 'open', () => {
    console.log('Mongo Db conectado!');
});