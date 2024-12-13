//import { FormGame } from "@/components/form/Game"
"use client"
import React from "react";
import TestForm from "@/components/form/Test"
import FormGame from "../components/form/Game";
import request from "@/app/_actions"
export default function Game(){
    return (
        <div className="max-w-sm">
            <FormGame/>
        </div>
    )
}