import mongoose from "mongoose";

const UserSchemma = new mongoose.Schema({
    username: { type: String, required: true, unique: true },
    password: { type: String, required: true },
})


export const UserModel = mongoosee.model("users", UserSchema)