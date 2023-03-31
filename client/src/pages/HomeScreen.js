import React from 'react';
import Navbar from '../components/Navbar';
import Panel from '../components/Panel';

import { RiVideoFill } from 'react-icons/ri'

import '../styles/HomeScreen.css'


function HomeScreen() {

    return (
        <div className='homeScreen'>

            <Navbar />

            <div className='screenWrapper'>

                <Panel />

                <div className='welcome'>


                    <h2>Revision of Under Graduate Courses - LOCF</h2>
                        
                    <div className='welcomeBox'>

                        <h2>UG Courses - Learning Outcomes - based Curriculum Framework (LOCF)</h2>

                        <h3>Last Date for constituting course revision committe 28 March 2023</h3>
                        <h3>Last Date for submission of the first draft 18 April 2023</h3>
                        
                        <div 
                            className='welcomeBoxBtn'
                            onClick={ () => window.open('https://www.youtube.com/watch?v=2lamQ-N95_s', '_blank') }
                        >
                            Help Video &nbsp; <RiVideoFill size={16} />
                        </div>


                    </div>

                </div>

            </div>

        </div>
    )
}

export default HomeScreen