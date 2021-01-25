import React from 'react'
import { Link } from 'react-router-dom'

export const Navbar = () => (
    <div>
        <Link to="/">Flask & React</Link>
        <button type="button">
            click me!
        </button>
        <div id="navbarNav">
            <ul>
                <li>
                    <Link to="/about">About</Link>
                </li>
            </ul>
        </div>
    </div>
)