"use client"
import React, { useState } from "react";


export default function FormGame(){
    async function buttonGameAction(){
        //"use server"
        
        const url = "http://127.0.0.1:8000/api/v1/products/"
        
        const response = await fetch(
            url,
            {method:"POST", headers: {"Content-Type": "applicaiton/json"}}
        )
        console.log(response)        
        if (!response.ok){
            throw new Error(response.statusText)
        }
        const data = await response.json()
        console.log(data)
        setProducts(data)
        return data
    }
    const [products, setProducts] = useState([])   
    return (
        <section>
        <div className="" id="products">{products.map(product => product.category)}</div>
        <div>
            <form action={buttonGameAction} method="post">
                <input type="submit" value="test" className="max-w-sm bg-sky-500 hover:bg-sky-500/70 text-white  px-4 py-2  border rounded-full"/>
            </form>
        </div>
        
        </section>
        
    );
}