import axios from 'axios'
import React, { useState, useEffect } from 'react'
import '../styles/Navbar.css'
import Loading from '../components/Loading';

import { MdDashboard } from 'react-icons/md'
import { BiUserCircle } from 'react-icons/bi'

const token = localStorage.getItem('token');

function Navbar() {

    const [data, setData] = useState('');
    const [loading, setLoading] = useState(true);

    useEffect( () => {

        axios.get("http://localhost:3001/home", { headers: { 'authorization': 'Bearer ' + token } })
        
        .then( res => {
            setData(res.data);
            setLoading(false);
        })

    }, []);


    if(loading) return <Loading />

    return (
        <div className='navbar'>

            <div className='logo'>
                <MdDashboard color='white' size={21} /> &nbsp; LOCF
            </div>

            <div className='items'>

                <BiUserCircle className='userImg' />

                <div className='userInfo'>
                    <h3> {data.user} <em> ({data.role}) </em> </h3>
                </div>

            </div>

        </div>  
  )
}

export default Navbar