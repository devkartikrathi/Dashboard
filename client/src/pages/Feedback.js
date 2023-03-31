import React from 'react'
import '../styles/AdminMenu.css'

import Navbar from '../components/Navbar'
import Panel from '../components/Panel'


function Feedback() {

  return (
    <div className='adminMenu'>

        <Navbar />

        <div className='screenWrapper'>

            <Panel />

            <div className='welcome'>

                Feedback

            </div>

        </div>

    </div>
  )
}

export default Feedback