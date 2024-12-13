import React from "react"
import Link from "next/link"


export default function Header(): JSX.Element {
    return (
        <header className="py-24 bg-gray-50 p-4">
            <nav className="container center">
                <ul className="flex gap-3">
                    <li>
                        <Link href="/">Home</Link>
                    </li>
                    <li>
                        <Link href="/earn">Earn</Link>
                    </li>
                    <li>
                        <Link href="/frens">Frens</Link>
                    </li>
                    <li>
                        <Link href="/airdrop">Airdrop</Link>
                    </li>
                    
                </ul>
            </nav>
        </header>
    
    )
}

