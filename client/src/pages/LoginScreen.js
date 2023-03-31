import React, { useState } from 'react';
import axios from 'axios';
import '../styles/LoginScreen.css';


function LoginScreen() {

    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [remember, setRemember] = useState(true);
    const [error, setError] = useState(false);

    function usernameRegex() {

        let regex = /^[a-zA-Z0-9]{5,15}$/;
        let test = regex.test(username);
        !test && alert('Invalid username! Username must be 5-15 characters, a-z, A-Z and 0-9!');
        return test;
        
    }

    function passwordRegex() {

        let regex = /^[a-zA-Z0-9!@#%*+=._-]{5,15}$/g;
        let test = regex.test(password);
        !test && alert('Password must be between 5-15 characters!');
        return test;
        
    }

    function submit() {

        if(!usernameRegex() || !passwordRegex()) { 
            return;
        } 

        axios.post('http://localhost:3001/login', {
            username: username,
            password: password
        })

        .then( res => {
            
            if(res.data === 401) {
                
                setError(true);
                return;

            }

            remember && localStorage.setItem('token', res.data);
            window.location.href = '/';

        })

        .catch( err => console.log(err) );

    }

    return (
        <div className='loginScreen'>
        
            <div className='panel'>
                <div className='loginWrapper'>
                    
                    <h1>Login to Dashboard</h1>

                    <input type="text" placeholder="Username" onChange={ (e) => setUsername(e.target.value) } />
                    <input type="password" placeholder="Password" onChange={ (e) => setPassword(e.target.value) } />
                    
                    <div className='remember'>
                        <input type='checkbox' checked={remember} onChange={() => setRemember(!remember)} /> &ensp;
                        <div>Remember me?</div>
                    </div>

                    {
                        error &&
                        <div className='error'>
                            Invalid username and password!
                        </div>
                    }
                    
                    <button onClick={ () => submit() }> Login </button>

                </div>
            </div>

            <div className='panel blue-side'>
                <div className='panel-img'/>
            </div>

        </div>
    )
}

export default LoginScreen