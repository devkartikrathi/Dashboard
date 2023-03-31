import React, { useEffect, useState } from 'react'
import { BrowserRouter, Routes, Route } from 'react-router-dom'

import LoginScreen from './pages/LoginScreen'
import HomeScreen from './pages/HomeScreen'
import AdminMenu from './pages/AdminMenu'
import Feedback from './pages/Feedback'
import ProgramReport from './pages/ProgramReport'

const token = localStorage.getItem('token')

function App() {

    if(!token) {
        return <LoginScreen />
    }

    return (
        <BrowserRouter>
            <Routes>

                <Route path='/' exact element={ <HomeScreen /> } />
                <Route path='/admin-menu' element={ <AdminMenu /> } />
                <Route path='/feedback' element={ <Feedback /> } />
                <Route path='/program-report' element={ <ProgramReport /> } />

            </Routes>
        </BrowserRouter>
    )
}

export default App