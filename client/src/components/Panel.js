import React from 'react'
import '../styles/Panel.css'
import { MdDashboard } from 'react-icons/md'
import { BsFillClipboardCheckFill } from 'react-icons/bs'
import { RiLockPasswordFill, RiLogoutBoxRFill } from 'react-icons/ri'

function Panel() {

    function logout() {
        localStorage.clear();
        window.location.href = '/';
    }

    return (

        <div className='optionPanel'>

            <div style={{paddingTop: '36px'}}></div>

            <a href='/' className='optionItems'> <MdDashboard size={21} />
                &ensp; Dashboard 
            </a>
            <a href='/admin-menu' className='optionItems'> <BsFillClipboardCheckFill />
                &ensp; Administration Menu 
            </a>
            <a href='/feedback' className='optionItems'> <BsFillClipboardCheckFill />
                &ensp; Feedback/Suggestion 
            </a>
            <a href='/program-report' className='optionItems'> <BsFillClipboardCheckFill />
                &ensp; Programme Wise Report 
            </a>
            <a href='' className='optionItems'> <BsFillClipboardCheckFill />
                &ensp; First Draft Report 
            </a>
            <a href='' className='optionItems'> <BsFillClipboardCheckFill />
                &ensp; View Draft (Course) 
            </a>
            <a href='' className='optionItems'> <BsFillClipboardCheckFill />
                &ensp; View Draft (Programmer) 
            </a>
            <a href='' className='optionItems'> <RiLockPasswordFill size={21} />
                &ensp; Change Password 
            </a>
            
            <a onClick={() => logout()} className='optionItems'> <RiLogoutBoxRFill size={21} />
                &ensp; Logout 
            </a>

        </div>

    )
}

export default Panel