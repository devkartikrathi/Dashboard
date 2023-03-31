import React from 'react'
import '../styles/AdminMenu.css'

import Navbar from '../components/Navbar'
import Panel from '../components/Panel'


function ProgramReport() {

  return (
    <div className='adminMenu'>

        <Navbar />

        <div className='screenWrapper'>

            <Panel />

            <div className='welcome'>

                Program Report

            </div>

        </div>

    </div>
  )
}

export default ProgramReport