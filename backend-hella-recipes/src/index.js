import express from "express";
import cors from "cors"
import mongoose from "mongoose"

const app = express();

app.use(express.json());
app.use(cors());

app.listen(31337, () => console.log("Server running on PORT 31337"));
