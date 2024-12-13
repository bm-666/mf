import React from "react";
import {test} from "@/app/_actions"

export default function TestForm(){
    return (
        
        <form action={test()} >
            <input type="submit" value="test" className="max-w-sm bg-sky-500 hover:bg-sky-500/70 text-white  px-4 py-2  border rounded-full"/>
        </form>
    )
}