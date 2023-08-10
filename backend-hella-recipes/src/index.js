import dotenv from 'dotenv';
dotenv.config();

import express from "express";
import cors from "cors"
import mongoose from "mongoose"

const app = express();

app.use(express.json());
app.use(cors());

mongoose.connect(process.env.DB_CONNECTION_STRING, {
    useNewUrlParser: true,
    useUnifiedTopology: true
})
    .then(() => console.log('Connected to MongoDB'))
    .catch(err => console.error('Could not connect to MongoDB', err));












app.listen(31337, () => console.log("Server running on PORT 31337"));
