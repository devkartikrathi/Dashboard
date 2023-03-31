import React from 'react'
import '../styles/AdminMenu.css'

import Navbar from '../components/Navbar'
import Panel from '../components/Panel'


function AdminMenu() {

  return (
    <div className='adminMenu'>

        <Navbar />

        <div className='screenWrapper'>

            <Panel />

            <div className='welcome'>

                Administration Menu

            </div>

        </div>

    </div>
  )
}

export default AdminMenu