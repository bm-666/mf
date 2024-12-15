"use client"
import React, { useEffect, useState } from "react";
import { Product } from "../types";


export default function Earn(){
    const [tasks, setTasks] = useState<Product[]>([])
    
    async function getTasks(){
        const response = await fetch(
            "http://127.0.0.1:8000/api/v1/tasks/"
        ).then((response) => response.json())
        
        setTasks(response)
        
    }

    useEffect(() => {getTasks()}, []) 
    return (
        <section>
            <div className="earn container">
                <ul className="shrink-0 m-auto pt-10 max-w-md ">
                    {tasks.map(task =>
                        <li className="pt-5 text-center justify-center " key={task.id}>
                            <span> {task.name} </span>
                            <span className="m-10"> {task.reward} </span>
                            <a href={task.url} className="bg-blue-400 hover:bg-blue-500 text-white px-1 rounded-full"> start </a>
                        </li>
                    )}
                </ul>
            </div>
        </section>
    )
}