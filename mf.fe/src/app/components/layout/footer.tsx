import Link from "next/link"

export default function Footer(): JSX.Element {
    return (
        <footer className="flex-row flex-wrap items-center justify-center w-full py-6 text-center border-t gap-y-6 gap-x-12 border-slate-200 md:justify-between">
            <nav className="flex flex-wrap justify-center -mx-5 -my-2">
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
                    <li>
                        <Link href="/game">Game</Link>
                    </li>
                    
                </ul>
            </nav>
        </footer>
)
}