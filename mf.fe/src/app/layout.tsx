import React from "react";
import type { Metadata } from "next";
import localFont from "next/font/local";
import{ Metal } from "next/font/google"
import "./globals.css";
import Script from "next/script";
import Head from "next/head";

import Footer from "./components/layout/footer";
import Game from "./Home/page";
import "./globals.css"



const geistSans = localFont({
  src: "./fonts/GeistVF.woff",
  variable: "--font-geist-sans",
  weight: "100 900",
});
const geistMono = localFont({
  src: "./fonts/GeistMonoVF.woff",
  variable: "--font-geist-mono",
  weight: "100 900",
});

export const metadata: Metadata = {
  title: "Create Next App",
  
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      
        <head>
          <script async src="https://telegram.org/js/telegram-web-app.js" ></script>
        </head>
      

        
      <body className={`${geistMono.className} antialiased`} >
      <main>
        {children}
        <Footer/>
      </main>
      </body>
    </html>
  );
}