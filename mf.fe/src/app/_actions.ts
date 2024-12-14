import { url } from "inspector";
import { NextRequest, NextResponse } from "next/server";



export default async function request(url: string, method: string){
    //console.log(`URL------> ${url}`)
    
    const response = await fetch(url, 
        {
            method: method,
            headers: {'Content-Type': 'application/json'}
        })
    //console.log(response)    
    if (!response.ok) {
        throw new Error(response.statusText)
    }
    return await response.json();
        
}